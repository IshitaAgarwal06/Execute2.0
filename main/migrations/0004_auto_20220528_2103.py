# Generated by Django 3.1.3 on 2022-05-28 15:33

from django.db import migrations, models
import main.models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_details_theinfo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='details',
            name='theinfo',
            field=models.FileField(default='images/default.pdf', upload_to='', validators=[main.models.validate_file_extension]),
        ),
    ]
