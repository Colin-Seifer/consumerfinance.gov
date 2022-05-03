#############################################################################
# This is a standalone file. Running it will create a test page in Wagtail.
# This file must be run from Wagtail admin. The test page should only be
# created during test runtime, and should not be created as a live page.
#############################################################################

import json
from datetime import date

from django.core.exceptions import ValidationError
from django.db import models

from wagtail.core import blocks
from wagtail.core.models import Site
from wagtail.images.blocks import ImageChooserBlock

from cfgov.v1.atomic_elements import molecules, organisms
from v1.models.test_page import TestPage


# Populates provided page with test data
def populate_test_data(page):
    # Populate header panel
    page.header = json.dumps(
        [
            {
                "hero": {
                    "is_overlay": True,
                    "is_bleeding": True,
                },
                "article_subheader": "Test subheader text",
                "text_introduction": {
                    "eyebrow": "Test H5 eyebrow text",
                    "heading": "Test H1 heading text",
                    "intro": "Test intro text",
                    "body": "Test body text",
                    "links": [
                        {
                            "text": "Reload",
                            "aria_label": "Reloads current page",
                            "url": "/",
                        },
                        {
                            "text": "Reload 2",
                            "aria_label": "Reloads current page",
                            "url": "/",
                        },
                    ],
                    "has_rule": True,
                },
                "item_introduction": {
                    "show_category": True,
                    "heading": "Test heading text",
                    "paragraph": "Test paragraph text",
                    "date": date.today(),
                    "has_social": True,
                },
                "featured_content": {
                    "heading": "Test heading text",
                    "body": "Test body text",
                    "post": blocks.PageChooserBlock(),
                    "show_post_link": True,
                    "post_link_text": "Reload",
                    "image": {
                        "upload": ImageChooserBlock(),
                        "alt": "Test alt text",
                    },
                    "links": [
                        {
                            "text": "Reload",
                            "aria_label": "Reloads current page",
                            "url": "/",
                        },
                        {
                            "text": "Reload 2",
                            "aria_label": "Reloads current page",
                            "url": "/",
                        },
                    ],
                    "video": {
                        "video_id": "1V0Ax9OIc84",
                        "thumbnail_image": ImageChooserBlock(),
                    },
                },
                "notification": {
                    "type": "information",
                    "message": "Test information message text",
                    "explanation": "Test explanation text",
                    "links": [
                        {
                            "text": "Reload",
                            "aria_label": "Reloads current page",
                            "url": "/",
                        },
                        {
                            "text": "Reload 2",
                            "aria_label": "Reloads current page",
                            "url": "/",
                        },
                    ],
                },
                "jumbo_hero": {
                    "is_50_50": True,
                },
                "features": {
                    "format": "50-50",
                    "heading": {
                        "level": "h2",
                        "icon": "help-round",
                    },
                    "intro": "Test intro text",
                    "link_image_and_heading": True,
                    "has_top_rule_line": True,
                    "lines_between_items": True,
                    "info_units": {
                        "image": {
                            "upload": ImageChooserBlock(),
                            "alt": "Test alt text",
                        },
                        "heading": {
                            "level": "h2",
                            "icon": "help-round",
                        },
                        "body": "Test body text",
                        "links": [
                            {
                                "text": "Reload",
                                "aria_label": "Reloads current page",
                                "url": "/",
                            },
                            {
                                "text": "Reload 2",
                                "aria_label": "Reloads current page",
                                "url": "/",
                            },
                        ],
                    },
                    "sharing": {
                        "shareable": True,
                        "share_blurb": "Test blurb text",
                    },
                },
            }
        ]
    )

    # populate misc panels
    page.preview_title = "Test preview title text"
    page.preview_subheading = "Test preview subheading text"
    page.preview_description = "Test preview description text"
    page.secondary_link_url = "/"
    page.secondary_link_text = "Reload"
    page.date_filed = date.today
    page.comments_close_by = "John Doe"
    page.public_enforcement_action = "Test public enforcement action text"
    page.initial_filing_date = date.today
    page.settled_or_contested_at_filing = "Settled"
    page.court = "Test court text"

    # populate event page. Basically its own page within the test page.
    page.body = "Test body text"
    page.archive_body = "Test archive body text"
    page.live_body = "Test live body text"
    page.future_body = "Test future body text"
    page.persistent_body = json.dumps(
        [
            {
                "content": "Test content text",
                "content_with_anchor": {
                    "content_block": "Test content block text",
                    "anchor_link": molecules.AnchorLink(),
                },
                "heading": {
                    "level": "h2",
                    "icon": "help-round",
                },
                "image": {
                    "upload": ImageChooserBlock(),
                    "alt": "Test alt text",
                },
                "table_block": organisms.AtomicTableBlock(
                    table_options={"renderer": "html"}
                ),
                "reusable_text": "Test reusable text",
            }
        ]
    )
    page.start_dt = models.DateTimeField("Start", date.today)
    page.end_dt = models.DateTimeField("End", date.today)
    page.future_body = "Test future body text"
    page.archive_image = json.dumps(
        {
            "upload": ImageChooserBlock(),
            "alt": "Test alt text",
        }
    )
    page.video_transcript = "REPLACE"  # TODO document
    page.speech_transcript = "REPLACE"  # TODO document


# Attempts to save an publish provided page as a child of parent
# Returns url path relative to the current site
def save_and_publish_test_page(page, parent, site):
    try:
        parent.add_child(instance=page)
        page.save_revision().publish()
    except ValidationError:
        return

    return parent.get_url(None, site)


# Creates and publishes a test page.
# Returns url path relative to the current site.
def create_test_page():
    # get the current site and gets root
    site = Site.objects.get(is_default_site=True)
    root = site.root

    # create page and add it as a child of root
    page = TestPage()

    # populate test page with data
    populate_test_data(page)

    # publish test page and return the route
    return save_and_publish_test_page(page, root, site)
