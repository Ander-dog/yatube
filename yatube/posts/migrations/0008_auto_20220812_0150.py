# Generated by Django 2.2.16 on 2022-08-12 01:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0007_auto_20220812_0112'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-created']},
        ),
        migrations.RenameField(
            model_name='post',
            old_name='pub_date',
            new_name='created',
        ),
    ]
