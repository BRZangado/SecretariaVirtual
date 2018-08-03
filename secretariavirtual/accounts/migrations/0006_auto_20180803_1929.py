# Generated by Django 2.0.7 on 2018-08-03 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20180803_1724'),
    ]

    operations = [
        migrations.AddField(
            model_name='solicitation',
            name='classs',
            field=models.CharField(default='turma não informada', help_text='Turma do Estudante', max_length=20, verbose_name='Turma'),
        ),
        migrations.AlterField(
            model_name='solicitation',
            name='student_semester',
            field=models.CharField(help_text='Período do Estudante', max_length=15, verbose_name='Período'),
        ),
    ]
