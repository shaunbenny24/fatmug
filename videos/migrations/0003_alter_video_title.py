# Generated by Django 5.1.1 on 2024-09-12 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0002_remove_video_uploaded_at_alter_video_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='title',
            field=models.CharField(max_length=255),
        ),
    ]
