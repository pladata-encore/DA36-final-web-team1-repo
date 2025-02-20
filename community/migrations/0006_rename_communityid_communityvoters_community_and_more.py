# Generated by Django 5.1.4 on 2025-02-20 05:44

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("community", "0005_rename_authorid_community_author_and_more"),
        ("users", "0008_userdetail_email"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameField(
            model_name="communityvoters",
            old_name="communityId",
            new_name="community",
        ),
        migrations.RenameField(
            model_name="communityvoters",
            old_name="voterId",
            new_name="voter",
        ),
        migrations.AlterField(
            model_name="community",
            name="author",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="User_community",
                to="users.userdetail",
            ),
        ),
        migrations.AlterUniqueTogether(
            name="communityvoters",
            unique_together={("voter", "community")},
        ),
    ]
