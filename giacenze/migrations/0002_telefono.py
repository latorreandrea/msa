# Generated by Django 4.1.2 on 2022-10-27 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('giacenze', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Telefono',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seriale', models.CharField(max_length=50)),
                ('codice_interno', models.CharField(max_length=50)),
                ('modello', models.CharField(max_length=254)),
                ('assegnazione', models.DateField()),
                ('note', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'Cellulari',
            },
        ),
    ]
