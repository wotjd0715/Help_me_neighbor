# Generated by Django 3.0.6 on 2020-05-27 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.EmailField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]