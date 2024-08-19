# Generated by Django 4.0.1 on 2022-10-08 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DetectedUsers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=100)),
                ('action', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(blank=True, upload_to='static/profile_image'),
        ),
    ]
