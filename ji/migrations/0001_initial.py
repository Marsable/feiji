# Generated by Django 3.0.5 on 2020-04-20 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ji',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='序列号')),
                ('banhao', models.CharField(max_length=200, verbose_name='航班号')),
                ('status', models.CharField(choices=[(0, '停用'), (1, '启用')], default=0, max_length=1)),
            ],
            options={
                'verbose_name': '飞机航班',
                'verbose_name_plural': '飞机航班',
                'db_table': 'ji',
            },
        ),
    ]
