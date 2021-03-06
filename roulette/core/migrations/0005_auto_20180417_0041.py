# Generated by Django 2.0.4 on 2018-04-17 00:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_project'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='user',
        ),
        migrations.AlterField(
            model_name='idea',
            name='thumbnail',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='idea',
            name='url',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='language',
            name='thumbnail',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='language',
            name='url',
            field=models.URLField(blank=True),
        ),
    ]
