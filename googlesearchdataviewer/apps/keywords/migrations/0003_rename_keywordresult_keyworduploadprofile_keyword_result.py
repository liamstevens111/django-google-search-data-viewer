# Generated by Django 4.0.3 on 2022-03-31 01:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('keywords', '0002_alter_keywordupload_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='keyworduploadprofile',
            old_name='KeywordResult',
            new_name='keyword_result',
        ),
    ]
