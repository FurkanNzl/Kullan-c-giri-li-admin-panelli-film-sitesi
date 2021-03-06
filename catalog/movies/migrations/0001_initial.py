# Generated by Django 3.2.5 on 2021-07-30 23:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Film Adı')),
                ('description', models.TextField(verbose_name='Film Açıklaması')),
                ('image', models.CharField(max_length=50, verbose_name='Fotoğraf')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Kayıt oluşturma Tarihi')),
                ('genred', models.CharField(max_length=15, verbose_name='Tür')),
            ],
        ),
    ]
