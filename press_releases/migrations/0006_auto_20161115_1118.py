# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('icekit_plugins_image', '0009_auto_20161026_2044'),
        ('icekit_press_releases', '0005_auto_20161110_1531'),
    ]

    operations = [
        migrations.AddField(
            model_name='pressreleaselisting',
            name='boosted_search_terms',
            field=models.TextField(blank=True, help_text='Words (space-separated) added here are boosted in relevance for search results increasing the chance of this appearing higher in the search results.'),
        ),
        migrations.AddField(
            model_name='pressreleaselisting',
            name='hero_image',
            field=models.ForeignKey(related_name='+', blank=True, null=True, help_text=b'The hero image for this content.', to='icekit_plugins_image.Image'),
        ),
        migrations.AddField(
            model_name='pressreleaselisting',
            name='list_image',
            field=models.ImageField(blank=True, help_text=b"image to use in listings. Default image is used if this isn't given", upload_to=b'icekit/listable/list_image/'),
        ),
    ]
