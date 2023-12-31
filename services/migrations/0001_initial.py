# Generated by Django 4.2.4 on 2023-09-05 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Titulo')),
                ('subtitle', models.CharField(max_length=100, verbose_name='Subtitulo')),
                ('image', models.ImageField(upload_to='Services', verbose_name='imagen')),
                ('content', models.TextField(verbose_name='Contenido')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion')),
                ('update', models.DateTimeField(auto_now=True, verbose_name='Fecha de modificacion')),
            ],
            options={
                'verbose_name': 'Servicios',
                'ordering': ['-created'],
            },
        ),
    ]
