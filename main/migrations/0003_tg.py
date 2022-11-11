# Generated by Django 4.1.3 on 2022-11-11 00:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_faq'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tg_id', models.CharField(max_length=200, verbose_name='tg_id')),
                ('datetime', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'TG ID',
                'verbose_name_plural': 'TG IDs',
            },
        ),
    ]
