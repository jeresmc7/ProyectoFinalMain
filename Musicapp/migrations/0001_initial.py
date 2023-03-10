# Generated by Django 4.1.7 on 2023-03-03 19:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('genero', models.CharField(choices=[('rock', 'Rock'), ('pop', 'Pop'), ('clasica', 'Clasica'), ('punk', 'Punk'), ('trap', 'Trap'), ('reggaeton', 'Reggaeton'), ('cumbia', 'Cumbia'), ('otro', 'Otro')], default='Rock', max_length=15)),
                ('descripcion', models.TextField(blank=True, null=True)),
                ('fechaPublicacion', models.DateTimeField(auto_now_add=True)),
                ('imagenBlog', models.ImageField(blank=True, null=True, upload_to='imagenes/')),
                ('usuario', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['usuario', '-fechaPublicacion'],
            },
        ),
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('mensaje', models.TextField(blank=True, null=True)),
                ('fechaComentario', models.DateTimeField(auto_now_add=True)),
                ('comentario', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comentarios', to='Musicapp.blog')),
            ],
            options={
                'ordering': ['-fechaComentario'],
            },
        ),
    ]
