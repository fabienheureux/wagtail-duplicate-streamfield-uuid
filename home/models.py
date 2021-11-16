from django.db import models

from wagtail.core.blocks import (
    RichTextBlock,
    StructBlock,
    StreamBlock
)
from wagtail.core.fields import StreamField
from wagtail.core.models import Page
from wagtail.admin.edit_handlers import StreamFieldPanel

class ThirdLevelBlock(StreamBlock):
    text = RichTextBlock()

class SecondLevelBlock(StructBlock):
    body = ThirdLevelBlock()

class FirstLevelBlock(StructBlock):
    extended_answer = SecondLevelBlock()

class ExampleBlock(StreamBlock):
    simple_question = FirstLevelBlock()

class HomePage(Page):
    blocks = StreamField(ExampleBlock())
    content_panels = Page.content_panels + [StreamFieldPanel("blocks")]
