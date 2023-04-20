# Generated by Django 4.1.7 on 2023-04-18 07:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import store.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('store', '0019_alter_chinacomment_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='HindiComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_body', models.TextField()),
                ('comment_image', models.ImageField(blank=True, null=True, upload_to=store.models.get_file_path_hindi)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('commenter_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='store.hindicategory')),
            ],
        ),
    ]
