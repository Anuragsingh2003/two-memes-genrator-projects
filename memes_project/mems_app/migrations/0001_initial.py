# Generated by Django 4.2.2 on 2023-07-02 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CaptionImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caption1', models.CharField(max_length=100)),
                ('caption2', models.CharField(max_length=100)),
                ('caption3', models.CharField(max_length=100)),
                ('caption_color1', models.CharField(max_length=7)),
                ('caption_background_color1', models.CharField(max_length=7)),
                ('caption_color2', models.CharField(max_length=7)),
                ('caption_background_color2', models.CharField(max_length=7)),
                ('caption_color3', models.CharField(max_length=7)),
                ('caption_background_color3', models.CharField(max_length=7)),
                ('position1', models.CharField(blank=True, max_length=10, null=True)),
                ('position2', models.CharField(blank=True, max_length=10, null=True)),
                ('position3', models.CharField(blank=True, max_length=10, null=True)),
                ('image', models.ImageField(upload_to='uploads/')),
            ],
        ),
    ]
