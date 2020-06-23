# Generated by Django 2.2.5 on 2020-06-23 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vps', '0016_auto_20200623_1512'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='connect_pid',
            field=models.BooleanField(choices=[(0, '否'), (1, '是')], default=1, verbose_name='是否需要连接PID'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='pid',
            field=models.IntegerField(blank=True, default=0, verbose_name='PID'),
        ),
    ]