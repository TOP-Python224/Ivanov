# Generated by Django 4.2.3 on 2023-07-28 08:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sitebot', '0003_tguser'),
    ]

    operations = [
        migrations.CreateModel(
            name='MessageUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(null=True, verbose_name='Текст комментария')),
                ('create_data', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Дата создания')),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='sitebot.tguser', verbose_name='Пользователь')),
                ('command', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='sitebot.listcommand', verbose_name='Сообщение от пользователя')),
            ],
        ),
    ]
