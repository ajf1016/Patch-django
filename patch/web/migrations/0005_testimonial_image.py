# Generated by Django 5.0.2 on 2024-03-20 01:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0004_faq'),
    ]

    operations = [
        migrations.AddField(
            model_name='testimonial',
            name='image',
            field=models.ImageField(default='https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.britannica.com%2Fbiography%2FElon-Musk&psig=AOvVaw1ncHuArk9jvnm9QMs5PQ28&ust=1710985385712000&source=images&cd=vfe&opi=89978449&ved=0CBIQjRxqFwoTCOjq17LbgYUDFQAAAAAdAAAAABAE', upload_to='testimonials/'),
            preserve_default=False,
        ),
    ]
