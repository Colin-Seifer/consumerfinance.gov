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

import json

from django.core.exceptions import ValidationError

# from wagtail.core import blocks
from wagtail.core.models import Site

from yaml import load

# from v1.atomic_elements import molecules, organisms
from v1.models.test_page import TestPage


# from datetime import date


# from email.mime import audio


# from django.db import models


# from wagtail.images.blocks import ImageChooserBlock


class TestPageData:
    page = TestPage(title="Test Page", slug="test-page")

    def populate_test_data(self):
        # read yaml file into page_data object
        stream = open("./cfgov/v1/tests/wagtail_pages/page_map.yaml", "r")
        page = load(stream)
        stream.close()

        definitions = page["definitions"]
        page_data = definitions["page"]

        # self.page.header = page_data["header"]
        self.page.preview_title = page_data["preview_title"]
        self.page.preview_subheading = page_data["preview_subheading"]
        self.page.preview_description = page_data["preview_description"]
        self.page.secondary_link_url = page_data["secondary_link_url"]
        self.page.secondary_link_text = page_data["secondary_link_text"]
        # self.page.preview_image = page_data["preview_image"]
        self.page.date_published = page_data["date_published"]
        # self.page.date_filed = page_data["date_filed"]
        # self.page.comments_close_by = page_data["comments_close_by"]
        self.page.public_enforcement_action = page_data[
            "public_enforcement_action"
        ]
        # self.page.initial_filing_date = page_data["initial_filing_date"]
        self.page.settled_or_contested_at_filing = page_data[
            "settled_or_contested_at_filing"
        ]
        self.page.court = page_data["court"]
        self.page.body = page_data["body"]
        self.page.archive_body = page_data["archive_body"]
        self.page.live_body = page_data["live_body"]
        self.page.future_body = page_data["future_body"]
        # self.page.persistent_body = page_data["persistent_body"]
        self.page.start_dt = page_data["start_dt"]
        self.page.end_dt = page_data["end_dt"]
        # self.page.archive_image = page_data["archive_image"]
        self.page.archive_video_id = page_data["archive_video_id"]
        self.page.live_stream_availability = page_data[
            "live_stream_availability"
        ]
        self.page.live_video_id = page_data["live_video_id"]
        # self.page.live_stream_date = page_data["live_stream_date"]
        self.page.venue_coords = page_data["venue_coords"]
        self.page.venue_name = page_data["venue_name"]
        self.page.venue_street = page_data["venue_street"]
        self.page.venue_suite = page_data["venue_suite"]
        self.page.venue_city = page_data["venue_city"]
        self.page.venue_state = page_data["venue_state"]
        self.page.venue_zipcode = page_data["venue_zipcode"]
        self.page.venue_image_type = page_data["venue_image_type"]
        self.page.post_event_image_type = page_data["post_event_image_type"]
        # self.page.post_event_image = page_data["post_event_image"]
        # self.page.agenda_items = page_data["agenda_items"]
        self.page.content = json.dumps(
            [
                {
                    "type": "well",
                    "value": page_data["content"]["well"],
                }
            ]
        )
        # self.page.content = page_data["content"]
        # self.page.sidebar_breakout = page_data["sidebar_breakout"]
        self.page.secondary_nav_exclude_sibling_pages = page_data[
            "secondary_nav_exclude_sibling_pages"
        ]
        self.page.share_and_print = page_data["share_and_print"]

    # Attempts to save an publish provided page as a child of parent
    # Returns url path relative to the current site
    def save_and_publish_test_page(self, parent, site):
        try:
            parent.add_child(instance=self.page)
            self.page.save_revision().publish()
        except ValidationError as e:
            print(e)
            return

        return parent.get_url(None, site)

    # Creates and publishes a test page.
    # Returns url path relative to the current site.
    def create_test_page(self):
        # get the current site and gets root
        site = Site.objects.get(is_default_site=True)
        root = site.root_page

        # populate test page with data
        self.populate_test_data()

        # publish test page and return the route
        return self.save_and_publish_test_page(root, site)


data = TestPageData()
data.create_test_page()
