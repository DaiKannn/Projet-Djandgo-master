# Generated by Django 4.0.4 on 2022-05-16 19:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Major',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Universite', models.CharField(max_length=100)),
                ('Region', models.CharField(max_length=100)),
                ('Departement', models.IntegerField(blank=True, null=True)),
                ('nombres_de_livres', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='CSGO',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nom_du_Major', models.CharField(max_length=100)),
                ('auteur', models.CharField(max_length=100)),
                ('date_parution', models.DateField(blank=True, null=True)),
                ('nombres_pages', models.IntegerField()),
                ('resume', models.TextField(blank=True, null=True)),
                ('bibliotheque', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='csgo.major')),
            ],
        ),
    ]