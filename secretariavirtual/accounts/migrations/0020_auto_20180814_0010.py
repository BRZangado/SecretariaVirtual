# Generated by Django 2.0.7 on 2018-08-14 00:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0019_auto_20180810_1910'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='solicitation',
            name='attachment_school_conclusion_historic',
        ),
        migrations.AddField(
            model_name='solicitation',
            name='attachment_academic_bond_certificate',
            field=models.FileField(blank=True, help_text='Declaração de Vínculo Acadêmico', null=True, upload_to='anexos/%Y/%m/academic-bond-certificate/', verbose_name='Declaração de Vínculo Acadêmico'),
        ),
        migrations.AddField(
            model_name='solicitation',
            name='attachment_degree',
            field=models.FileField(blank=True, help_text='Diploma da graduação', null=True, upload_to='anexos/%Y/%m/degrees/', verbose_name='Diploma'),
        ),
        migrations.AddField(
            model_name='solicitation',
            name='attachment_discipline_menu',
            field=models.FileField(blank=True, help_text='Ementas das disciplinas cursadas na IES de origem', null=True, upload_to='anexos/%Y/%m/discipline-menus/', verbose_name='Ementas das disciplinas'),
        ),
        migrations.AddField(
            model_name='solicitation',
            name='attachment_school_historic',
            field=models.FileField(blank=True, help_text='Histórico Escolar Anexado pelo estudante', null=True, upload_to='anexos/%Y/%m/school-historic/', verbose_name='Histórico Escolar'),
        ),
    ]