# Generated by Django 2.2.6 on 2019-10-14 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formulas', '0002_formula_published_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='formula',
            name='title',
            field=models.CharField(max_length=40, null=True),
        ),
    ]
