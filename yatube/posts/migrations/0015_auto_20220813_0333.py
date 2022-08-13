# Generated by Django 2.2.16 on 2022-08-13 03:33

from django.db import migrations, models
import django.db.models.expressions


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0014_auto_20220813_0323'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='follow',
            name='do not selffollow',
        ),
        migrations.AddConstraint(
            model_name='follow',
            constraint=models.CheckConstraint(check=models.Q(user=django.db.models.expressions.F('author')), name='do not selffollow'),
        ),
    ]