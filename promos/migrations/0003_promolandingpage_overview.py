# Generated by Django 2.0.5 on 2018-06-14 00:04

from django.db import migrations
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('promos', '0002_auto_20180613_1151'),
    ]

    operations = [
        migrations.AddField(
            model_name='promolandingpage',
            name='overview',
            field=wagtail.core.fields.RichTextField(blank=True, null=True),
        ),
    ]