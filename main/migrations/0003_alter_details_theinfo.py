# Generated by Django 4.0.3 on 2022-05-28 12:46

from django.db import migrations, models
import main.models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_details_theinfo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='details',
            name='theinfo',
            field=models.FileField(default='images/default.pdf', help_text='Please enter your name', upload_to='', validators=[main.models.validate_file_extension]),
        ),
    ]
