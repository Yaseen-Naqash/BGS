# Generated by Django 5.0 on 2024-02-18 12:50

import django.core.validators
import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_user_purchases_user_rating_user_sells'),
    ]

    operations = [
        migrations.AddField(
            model_name='boardgame',
            name='name',
            field=models.CharField(default='no name entered', max_length=200),
        ),
        migrations.AddField(
            model_name='deal',
            name='buyer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='buyer', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='deal',
            name='buyerToughts',
            field=models.TextField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='deal',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='deal',
            name='dealDate',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='deal',
            name='description',
            field=models.TextField(blank=True, max_length=1500, null=True),
        ),
        migrations.AddField(
            model_name='deal',
            name='seller',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='seller', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='deal',
            name='sellerToughts',
            field=models.TextField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='deal',
            name='status',
            field=models.CharField(choices=[('0', 'OPEN DEAL'), ('1', 'SOLD'), ('2', 'SEMI SOLD'), ('3', 'UNKNOWN')], default=0, max_length=1),
        ),
        migrations.AddField(
            model_name='deal',
            name='title',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='deal',
            name='totalPrice',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(100000000), django.core.validators.MinValueValidator(50000)]),
        ),
        migrations.AddField(
            model_name='deal',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
