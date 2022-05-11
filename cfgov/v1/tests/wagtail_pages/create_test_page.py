#############################################################################
# Author: Colin Seifer
# This is a standalone file. Running it will publish a test page in Wagtail.
# The test data is auto populated from the provided test page. The test page
# object template is broken down into fields and data types with expected
# data formats. Each field is then populated from the appropriate data stub.
# Certain stubs are expected to exist at the provided path which can be
# modified by calling the set_stubs method. Stubs whose path is expected to
# exist are marked as such.
#############################################################################

# import json
# from datetime import date

from django.core.exceptions import ValidationError

# from wagtail.core import blocks
from wagtail.core.models import Site

# from v1.atomic_elements import molecules, organisms
from v1.models.test_page import TestPage


# from yaml import dump, load


# from email.mime import audio


# from django.db import models


# from wagtail.images.blocks import ImageChooserBlock


class TestPageData:
    # # path constants. Change to modify where stubs look for data.
    # STUB_IMAGE_PATH = "/"
    # STUB_VIDEO_PATH = "/"
    # STUB_DOCUMENT_PATH = "/"
    # STUB_TABLE_PATH = "/"
    # STUB_FLICKR_PATH = "/"
    # STUB_AUDIO_PATH = "/"
    # STUB_CHART_PATH = "/"
    # STUB_MAP_PATH = "/"

    # # set any stubs that will be used
    # def set_stubs(
    #     self,
    #     image_url="/",
    #     video_url="/",
    #     document_url="/",
    #     table_url="/",
    #     flickr_url="/",
    #     audio_url="/",
    #     chart_url="/",
    #     map_url="/",
    # ):
    #     self.STUB_IMAGE_PATH = image_url
    #     self.STUB_VIDEO_PATH = video_url
    #     self.STUB_DOCUMENT_PATH = document_url
    #     self.STUB_TABLE_PATH = table_url
    #     self.STUB_FLICKR_PATH = flickr_url
    #     self.STUB_AUDIO_PATH = audio_url
    #     self.STUB_CHART_PATH = chart_url
    #     self.STUB_MAP_PATH = map_url

    # # Populates provided page with test data
    # def populate_test_data(self, page):
    #     stub_boolean = True
    #     # completely arbitrary and replaceable
    #     stub_integer = 5
    #     # completely arbitrary and replaceable
    #     stub_float = 0.33333
    #     stub_string = "Test text data"
    #     stub_relative_path = "/"
    #     stub_aria_label = "Test aria label"
    #     stub_date = date.today()
    #     # CFPB Address
    #     stub_street_address = "1700 G Street NW"
    #     stub_city = "Washington"
    #     stub_state = "DC"
    #     stub_zipcode = "20552"
    #     # end address
    #     # the following stubs expect a path to exist
    #     stub_image = self.STUB_IMAGE_PATH
    #     stub_video = self.STUB_VIDEO_PATH
    #     stub_document = self.STUB_DOCUMENT_PATH
    #     stub_table = self.STUB_TABLE_PATH
    #     stub_flickr_url = self.STUB_FLICKR_PATH
    #     stub_audio = self.STUB_AUDIO_PATH
    #     stub_chart = self.STUB_CHART_PATH
    #     stub_map = self.STUB_MAP_PATH

    #     # dump page to yaml format
    #     page_yaml = dump(page)

    # replace fields with stubs based on key name
    # resolve stubs that require a path
    # resolve booleans
    # resolve integers
    # resolve float / double
    # resolve strings that require a street address
    # resolve strings that require a city
    # resolve strings that require a state
    # resolve strings that require a zipcode
    # resolve strings that require an aria label
    # resolve strings that require a general path
    # resolve all other strings
    # resolve to None if not caught

    # Populate header panel
    # page.header = json.dumps(
    #     [
    #         {
    #             "hero": {
    #                 "is_overlay": True,
    #                 "is_bleeding": True,
    #             },
    #             "article_subheader": "Test subheader text",
    #             "text_introduction": {
    #                 "eyebrow": "Test H5 eyebrow text",
    #                 "heading": "Test H1 heading text",
    #                 "intro": "Test intro text",
    #                 "body": "Test body text",
    #                 "links": [
    #                     {
    #                         "text": "Reload",
    #                         "aria_label": "Reloads current page",
    #                         "url": "/",
    #                     },
    #                     {
    #                         "text": "Reload 2",
    #                         "aria_label": "Reloads current page",
    #                         "url": "/",
    #                     },
    #                 ],
    #                 "has_rule": True,
    #             },
    #             "item_introduction": {
    #                 "show_category": True,
    #                 "heading": "Test heading text",
    #                 "paragraph": "Test paragraph text",
    #                 "date": date.today(),
    #                 "has_social": True,
    #             },
    #             "featured_content": {
    #                 "heading": "Test heading text",
    #                 "body": "Test body text",
    #                 "post": blocks.PageChooserBlock(),
    #                 "show_post_link": True,
    #                 "post_link_text": "Reload",
    #                 "image": {
    #                     "upload": ImageChooserBlock(),
    #                     "alt": "Test alt text",
    #                 },
    #                 "links": [
    #                     {
    #                         "text": "Reload",
    #                         "aria_label": "Reloads current page",
    #                         "url": "/",
    #                     },
    #                     {
    #                         "text": "Reload 2",
    #                         "aria_label": "Reloads current page",
    #                         "url": "/",
    #                     },
    #                 ],
    #                 "video": {
    #                     "video_id": "1V0Ax9OIc84",
    #                     "thumbnail_image": ImageChooserBlock(),
    #                 },
    #             },
    #             "notification": {
    #                 "type": "information",
    #                 "message": "Test information message text",
    #                 "explanation": "Test explanation text",
    #                 "links": [
    #                     {
    #                         "text": "Reload",
    #                         "aria_label": "Reloads current page",
    #                         "url": "/",
    #                     },
    #                     {
    #                         "text": "Reload 2",
    #                         "aria_label": "Reloads current page",
    #                         "url": "/",
    #                     },
    #                 ],
    #             },
    #             "jumbo_hero": {
    #                 "is_50_50": True,
    #             },
    #             "features": {
    #                 "format": "50-50",
    #                 "heading": {
    #                     "level": "h2",
    #                     "icon": "help-round",
    #                 },
    #                 "intro": "Test intro text",
    #                 "link_image_and_heading": True,
    #                 "has_top_rule_line": True,
    #                 "lines_between_items": True,
    #                 "info_units": {
    #                     "image": {
    #                         "upload": ImageChooserBlock(),
    #                         "alt": "Test alt text",
    #                     },
    #                     "heading": {
    #                         "level": "h2",
    #                         "icon": "help-round",
    #                     },
    #                     "body": "Test body text",
    #                     "links": [
    #                         {
    #                             "text": "Reload",
    #                             "aria_label": "Reloads current page",
    #                             "url": "/",
    #                         },
    #                         {
    #                             "text": "Reload 2",
    #                             "aria_label": "Reloads current page",
    #                             "url": "/",
    #                         },
    #                     ],
    #                 },
    #                 "sharing": {
    #                     "shareable": True,
    #                     "share_blurb": "Test blurb text",
    #                 },
    #             },
    #         }
    #     ]
    # )

    # # populate misc panels
    # page.preview_title = "Test preview title text"
    # page.preview_subheading = "Test preview subheading text"
    # page.preview_description = "Test preview description text"
    # page.secondary_link_url = "/"
    # page.secondary_link_text = "Reload"
    # page.date_filed = date.today
    # page.comments_close_by = "John Doe"
    # page.public_enforcement_action = "Test public enforcement action text"
    # page.initial_filing_date = date.today
    # page.settled_or_contested_at_filing = "Settled"
    # page.court = "Test court text"

    # # populate event page. Basically its own page within the test page.
    # page.body = "Test body text"
    # page.archive_body = "Test archive body text"
    # page.live_body = "Test live body text"
    # page.future_body = "Test future body text"
    # page.persistent_body = json.dumps(
    #     [
    #         {
    #             "content": "Test content text",
    #             "content_with_anchor": {
    #                 "content_block": "Test content block text",
    #                 "anchor_link": molecules.AnchorLink(),
    #             },
    #             "heading": {
    #                 "level": "h2",
    #                 "icon": "help-round",
    #             },
    #             "image": {
    #                 "upload": ImageChooserBlock(),
    #                 "alt": "Test alt text",
    #             },
    #             "table_block": organisms.AtomicTableBlock(
    #                 table_options={"renderer": "html"}
    #             ),
    #             "reusable_text": "Test reusable text",
    #         }
    #     ]
    # )
    # page.start_dt = models.DateTimeField("Start", date.today)
    # page.end_dt = models.DateTimeField("End", date.today)
    # page.future_body = "Test future body text"
    # page.archive_image = json.dumps(
    #     {
    #         "upload": ImageChooserBlock(),
    #         "alt": "Test alt text",
    #     }
    # )
    # page.video_transcript = "REPLACE"  # TODO document
    # page.speech_transcript = "REPLACE"  # TODO document

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
    def create_test_page(self):
        # get the current site and gets root
        site = Site.objects.get(is_default_site=True)
        root = site.root

        # create page and add it as a child of root
        page = TestPage()

        # populate test page with data
        self.populate_test_data(page)

        # publish test page and return the route
        return self.save_and_publish_test_page(page, root, site)
