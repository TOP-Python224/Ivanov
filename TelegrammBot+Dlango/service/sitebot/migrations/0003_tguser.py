# Generated by Django 4.2.3 on 2023-07-28 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitebot', '0002_listcommand_content'),
    ]

    operations = [
        migrations.CreateModel(
            name='TgUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_tg_user', models.BigIntegerField(unique=True, verbose_name='Пользователь TG')),
                ('name', models.CharField(max_length=50, verbose_name='Имя')),
                ('first_name', models.CharField(max_length=50, verbose_name='Фамилия')),
                ('user_name', models.CharField(blank=True, max_length=50, verbose_name='Логин')),
            ],
        ),
    ]
