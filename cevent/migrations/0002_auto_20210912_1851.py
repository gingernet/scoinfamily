# Generated by Django 2.2.7 on 2021-09-12 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cevent', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='check_time',
            field=models.DateTimeField(blank=True, db_index=True, null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='solve_time',
            field=models.DateTimeField(blank=True, db_index=True, null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='status',
            field=models.CharField(choices=[('WAIT_CHECK', 'WAIT_CHECK'), ('WAIT_SOLUTE', 'WAIT_SOLUTE'), ('WAIT_BACK', 'WAIT_BACK'), ('FINISH', 'FINISH')], default='WAIT_CHECK', max_length=100, verbose_name='事件状态'),
        ),
    ]
