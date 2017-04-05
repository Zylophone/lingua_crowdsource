# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-02 16:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cabinet', '0002_auto_20170325_1624'),
    ]

    operations = [
        migrations.CreateModel(
            name='MarkUp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=100, verbose_name='Слово')),
                ('grammem', models.CharField(max_length=100, verbose_name='Часть речи')),
                ('animacy', models.CharField(max_length=100, verbose_name='Одушевленность')),
                ('aspect', models.CharField(max_length=100, verbose_name='Вид')),
                ('case', models.CharField(max_length=100, verbose_name='Падеж')),
                ('gender', models.CharField(max_length=100, verbose_name='Род')),
                ('involvement', models.CharField(max_length=100, verbose_name='Говорящий')),
                ('mood', models.CharField(max_length=100, verbose_name='Наклонение')),
                ('number', models.CharField(max_length=100, verbose_name='Число')),
                ('person', models.CharField(max_length=100, verbose_name='Лицо')),
                ('tense', models.CharField(max_length=100, verbose_name='Время')),
                ('transitivity', models.CharField(max_length=100, verbose_name='Переходность')),
                ('voice', models.CharField(max_length=100, verbose_name='Залог')),
                ('count', models.IntegerField(verbose_name='Встречается в тексте')),
                ('lit_work', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cabinet.LitWork', verbose_name='Произведение')),
            ],
        ),
    ]