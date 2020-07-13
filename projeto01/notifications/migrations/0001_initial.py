# Generated by Django 2.2 on 2020-07-13 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Livro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('subtitulo', models.CharField(max_length=200)),
                ('autor', models.CharField(max_length=200)),
                ('presso', models.FloatField()),
                ('data_publicacao', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
