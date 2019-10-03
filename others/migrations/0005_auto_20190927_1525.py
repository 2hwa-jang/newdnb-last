# Generated by Django 2.2.5 on 2019-09-27 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('others', '0004_auto_20190927_1523'),
    ]

    operations = [
        migrations.AlterField(
            model_name='culture',
            name='content',
            field=models.TextField(verbose_name='내용'),
        ),
        migrations.AlterField(
            model_name='culture',
            name='finish_time',
            field=models.DateField(verbose_name='종료 날짜'),
        ),
        migrations.AlterField(
            model_name='culture',
            name='start_time',
            field=models.DateField(verbose_name='시작 날짜'),
        ),
        migrations.AlterField(
            model_name='culture',
            name='title',
            field=models.CharField(max_length=200, verbose_name='제목'),
        ),
        migrations.AlterField(
            model_name='culture',
            name='write_date',
            field=models.DateTimeField(auto_now=True, verbose_name='작성한 날짜'),
        ),
    ]