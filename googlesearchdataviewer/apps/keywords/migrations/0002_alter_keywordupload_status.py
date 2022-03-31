# Generated by Django 4.0.3 on 2022-03-31 01:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('keywords', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='keywordupload',
            name='status',
            field=models.IntegerField(choices=[(0, 'Awaiting Processing'), (1, 'In-Progress'), (2, 'Completed')], db_index=True, default=0, verbose_name='Status'),
        ),
    ]