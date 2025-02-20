from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from review.entity.models import ReviewForm
from review.service.review_service import ReviewServiceImpl
from django.http import JsonResponse

review_service = ReviewServiceImpl()
def review_main(request):
    return render(request, 'review/review_main.html', {'review_main':review_main})

@login_required(login_url='users:login')
def review_write(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            pass
        else:
            print('form.errors=',form.errors)
    else:
        form = ReviewForm()

    return render(request, 'review/review_form.html', {'ReviewForm': ReviewForm})


@login_required()
def review_likes(request, review_id):
    try:
        review, liked = review_service.review_likes(review_id, request.user)
        likes_count = review.likes.count() if hasattr(review, 'likes') else 0

        print('review.likes.count() =', likes_count)
        return JsonResponse({
            'result': 'success',
            'likes_count': likes_count,
            'liked': liked,
        })
    except Exception as e:
        return JsonResponse({
            'result': 'error',
            'message': str(e)
        }, status=400)

