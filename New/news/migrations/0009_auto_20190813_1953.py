# Generated by Django 2.2.4 on 2019-08-13 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0008_auto_20190813_1952'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='post_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
