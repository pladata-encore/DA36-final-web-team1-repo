from django.shortcuts import redirect, render
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required


from review.entity.models import ReviewForm, Review, ReviewRecommender
from review.service.review_service import ReviewServiceImpl
from django.http import JsonResponse
from django.contrib import messages
from django.urls import reverse

from review.service.upload_service import S3Client

review_service = ReviewServiceImpl()
s3_client = S3Client()

def review_main(request):
    return render(request, 'review/review_main.html', {'review_main':review_main})


@login_required(login_url='users:login')
def review_write(request):
    product_id = request.GET.get("product_id", "")  # GET 요청에서 product_id 가져오기

    if request.method == 'POST':
        form = ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            review = form.save(commit=False)
            review.author_id=request.user.id

            if 'reviewImageUrl' in request.FILES:
                obj_url = s3_client.upload_review_image(request.FILES['reviewImageUrl'])
                if obj_url:
                    review.reviewImageUrl = obj_url

            product_id = request.POST.get("product_id")
            if product_id:
                review.product_id = product_id
            review_service.create(review)
            return redirect('product:product_detail', product_id=product_id)
        else:
            print('form.errors=',form.errors)
    else:
        form = ReviewForm()

    return render(request, 'review/review_form.html', {'form': form, 'product_id': product_id})


@login_required(login_url='users:login')
def review_recommend(request, review_id):
    review = review_service.find_by_review_id(review_id)
    if request.user.id == review.author_id:
        return JsonResponse({
            'result': 'false'
        })
    try:
        review,recommended = review_service.add_remove_recommend(review_id, request.user)
        recommender_count = review.recommender.count() if hasattr(review, 'recommender') else 0

        print('product.recommender_count() =', recommender_count)
        return JsonResponse({
            'result': 'success',
            'recommender_count': recommender_count,
            'recommended':recommended
        })
    except Exception as e:
        return JsonResponse({
            'result': 'error',
            'message': str(e)
        }, status=400)



