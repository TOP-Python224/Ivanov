# Generated by Django 4.2.3 on 2023-07-27 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitebot', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='listcommand',
            name='content',
            field=models.TextField(null=True, verbose_name='Сообщение от бота'),
        ),
    ]
