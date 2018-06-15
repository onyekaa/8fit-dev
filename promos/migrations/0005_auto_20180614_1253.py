# Generated by Django 2.0.5 on 2018-06-14 12:53

from django.db import migrations, models
import wagtail.contrib.table_block.blocks
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.documents.blocks
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('promos', '0004_auto_20180614_1019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='promolandingpage',
            name='body',
            field=wagtail.core.fields.StreamField([('content', wagtail.core.blocks.StructBlock([('heading', wagtail.core.blocks.CharBlock()), ('content', wagtail.core.blocks.RichTextBlock(features=['h4', 'bold', 'italic', 'link', 'ol', 'ul'])), ('screenshot', wagtail.images.blocks.ImageChooserBlock(required=False))]))]),
        ),
        migrations.AlterField(
            model_name='promolandingpage',
            name='currency',
            field=models.CharField(choices=[('USD', '$'), ('GBP', '£'), ('EUR', '€')], max_length=3),
        )
    ]
