# Generated by Django 2.2.1 on 2019-05-31 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0005_auto_20190530_2019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectspecs',
            name='preview',
            field=models.ImageField(default='default.png', upload_to='previews'),
        ),
    ]
