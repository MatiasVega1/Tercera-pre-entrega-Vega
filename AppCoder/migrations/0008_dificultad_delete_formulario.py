# Generated by Django 4.1.5 on 2023-02-03 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0007_formulario'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dificultad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('difficulty', models.CharField(choices=[('facil', 'Facil'), ('normal', 'Normal'), ('dificil', 'Dificil')], default='normal', max_length=10)),
            ],
        ),
        migrations.DeleteModel(
            name='Formulario',
        ),
    ]