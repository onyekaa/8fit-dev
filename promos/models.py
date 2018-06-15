from django.db import models

from modelcluster.fields import ParentalKey

from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock
from wagtail.core.models import Page, Orderable
from wagtail.core.fields import RichTextField, StreamField
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel, InlinePanel, StreamFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.search import index
from wagtail.snippets.models import register_snippet
from wagtailcolumnblocks.blocks import ColumnsBlock


@register_snippet
class PromoPlan(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=500)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Promo plan'
        verbose_name_plural = 'Promo Plans'


# Content blocks that will be used in the columngrid block
class CommonBlocks(blocks.StreamBlock):
    content = blocks.RichTextBlock(group="Common")

# Column Types
class ColumnBlocks(blocks.StreamBlock):
    column_1_1 = ColumnsBlock(
        CommonBlocks(),
        ratios=(1, 1),
        label="Two halves",
        group="Columns",
    )
    column_2_1 = ColumnsBlock(
        CommonBlocks(max_num=1),
        ratios=(2, 1),
        label="Two thirds/One third",
        group="Columns",
    )
    column_1_1_1 = ColumnsBlock(
        CommonBlocks(),
        ratios=(1, 1, 1),
        label="Three thirds",
        group="Columns",
    )


class AllBlocks(ColumnBlocks, CommonBlocks):
    pass



""" Highlight Colors:

    Used for changing colours of headers/links to liven up pages
    It's also possible to make these dynamically created choices.
"""
COLOR_CHOICES = (
    ('green', 'Green'),
    ('orange', 'Orange'),
    ('red', 'Red'),
)

class ContentBlock(blocks.StructBlock):
    heading = blocks.CharBlock()
    content = blocks.RichTextBlock(features=['h4', 'bold', 'italic', 'link', 'ol', 'ul'])
    screenshot = ImageChooserBlock(required=False)
    highlight_color = blocks.ChoiceBlock(choices=COLOR_CHOICES, blank=True, null=True)

    class Meta:
        icon = 'user'
        form_classname = 'content-block struct-block'


class FeatureBlock(blocks.StructBlock):
    heading = blocks.CharBlock()
    summary = blocks.RichTextBlock(features=['h4', 'bold', 'italic', 'link', 'ol', 'ul'])
    image = ImageChooserBlock(required=False)
    rounded = models.BooleanField(default=False, help_text="Make the featured image a circle.")


    class Meta:
        icon = 'user'
        form_classname = 'content-block struct-block'



class PromoLandingPage(Page):
    TMP_CURRENCIES = (
        ('USD', '$'),
        ('GBP', '£'),
        ('EUR', '€'),
    )
    hero_title = models.CharField(max_length=200)
    overview = StreamField(
        blocks.StreamBlock([
        ('freeform', blocks.RichTextBlock()),
        ('two_three_column_grid', ColumnBlocks())
    ], max_num=3)
    )
    body = StreamField(
        blocks.StreamBlock([
        ('content', ContentBlock())
    ], max_num=3)
    )

    hero_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    plan = models.ForeignKey(
        PromoPlan,
        null=True,
        blank=True,
        on_delete=models.SET_NULL
    )
    price = models.DecimalField(decimal_places=2, max_digits=10)
    currency = models.CharField(max_length=3, choices=TMP_CURRENCIES)
    promo_duration = models.DateTimeField(help_text="Set the time when you want this to expire. Leave empty for permanent promo page")
    coupon = models.CharField(max_length=50, blank=True, null=True)

    CTA = models.CharField(max_length=200, default="Start Your Plan Now.")

    created_date = models.DateTimeField(editable=False, auto_now_add=True)
    modified_date = models.DateTimeField(editable=False, db_index=True, auto_now=True)

    content_panels = [
        FieldPanel('title'),
        FieldPanel('hero_title'),
        StreamFieldPanel('overview'),
        StreamFieldPanel('body'),
        ImageChooserPanel('hero_image'),
        MultiFieldPanel(
        [
            FieldPanel('plan'),
            FieldPanel('price'),
            FieldPanel('currency'),
            FieldPanel('coupon'),
            FieldPanel('promo_duration')
        ],
        heading="Promo Plan Details",
        classname="collapsible"
        ),
    ]
