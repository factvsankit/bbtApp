from decimal import Decimal

from django.db import models
from django.utils import translation
from django.utils.html import format_html

from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.fields import StreamField, RichTextField
from wagtail.wagtailcore import blocks
from wagtail.wagtailimages.blocks import ImageChooserBlock
from wagtail.wagtailadmin.edit_handlers import FieldPanel, StreamFieldPanel

from wagtailmedia.blocks import AbstractMediaChooserBlock


class TranslatedField(object):
    def __init__(self, en_field, np_field):
        self.en_field = en_field
        self.np_field = np_field

    def __get__(self, instance, owner):
        en = getattr(instance, self.en_field)
        np = getattr(instance, self.np_field)

        if translation.get_language() == 'ne':
            return np
        else:
            return en


class AudioBlock(AbstractMediaChooserBlock):
    def render_basic(self, value):
        if not value:
            return ''

        if value.type == 'audio':
            player_code = '''
            <div>
                <audio controls>
                    <source src="{0}" type="audio/mpeg">
                    Your browser does not support the audio element.
                </audio>
            </div>
            '''
        else:
            player_code = '''
            <div>
                <video width="320" height="240" controls>
                    <source src="{0}" type="video/mp4">
                    Your browser does not support the video tag.
                </video>
            </div>
            '''

        return format_html(player_code, value.file.url)


class ContentPage(Page):
    name = models.CharField(max_length=60, blank=True, default='')
    improved_technique = models.BooleanField(blank=True, default=True)

    body_en = StreamField([
        ('paragraph', blocks.RichTextBlock(icon="pilcrow")),
        ('image', ImageChooserBlock(icon="picture")),
        ('media', AudioBlock(icon='media')),
        # ('media', AudioVideoBlock(icon="media"))
    ])
    body_np = StreamField([
        ('paragraph', blocks.RichTextBlock(icon="pilcrow")),
        ('image', ImageChooserBlock(icon="picture")),
        ('media', AudioBlock(icon='media')),
        # ('media', AudioVideoBlock(icon="media"))

    ])
    body = TranslatedField(
        'body_en',
        'body_np',
    )

    content_panels = [
        FieldPanel('title'),
        FieldPanel('name'),
        FieldPanel('improved_technique'),
        StreamFieldPanel('body_en'),
        StreamFieldPanel('body_np'),

    ]


class ContentIndexPage(Page):
    intro = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('intro', classname="full"),
    ]


'''
class BlogPageWithMedia(Page):
    author = models.CharField(max_length=255)
    date = models.DateField("Post date")
    body = RichTextField(blank=False)
    media = models.ForeignKey(
        'wagtailmedia.Media',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    content_panels = Page.content_panels + [
        FieldPanel('author'),
        FieldPanel('date'),
        FieldPanel('body'),
        MediaChooserPanel('media'),
    ]
'''
