# Generated by Django 4.2.3 on 2023-07-20 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Laboratoire', '0008_auto_20230720_2130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='laboratoire',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
