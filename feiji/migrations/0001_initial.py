# Generated by Django 3.0.5 on 2020-04-20 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feiji',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='序列号')),
                ('uid', models.CharField(max_length=200, verbose_name='用户id')),
                ('jid', models.CharField(max_length=200, verbose_name='飞机id')),
                ('zuowei', models.CharField(max_length=200, verbose_name='座位号')),
            ],
            options={
                'verbose_name': '飞机票',
                'verbose_name_plural': '飞机票',
                'db_table': 'feiji',
            },
        ),
    ]