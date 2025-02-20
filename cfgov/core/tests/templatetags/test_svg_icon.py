import os
from unittest.mock import patch

from django.template import Context, Template
from django.test import TestCase, override_settings
from django.utils.safestring import SafeData

from core.templatetags.svg_icon import SVG_REGEX, load_svg, svg_icon


VALID_SVG = (
    '<svg width="100" height="100">\n'
    '  <circle cx="50" cy="50" r="40" stroke="green" fill="yellow" />\n'
    "</svg>\n"
)


class SvgRegexTests(TestCase):
    def test_empty_svg_matches(self):
        self.assertTrue(SVG_REGEX.match("<svg></svg>"))

    def test_case_insensitive_matching(self):
        self.assertTrue(SVG_REGEX.match("<sVg></SvG>"))

    def test_valid_svg_matches(self):
        self.assertTrue(SVG_REGEX.match(VALID_SVG))

    def test_valid_svg_with_extra_whitespace_matches(self):
        self.assertTrue(SVG_REGEX.match(" " + VALID_SVG + "\n\n"))

    def test_invalid_svg_does_not_match(self):
        self.assertFalse(SVG_REGEX.match('<script type="malicious"></script>'))

    def test_nested_invalid_svg_does_not_match(self):
        self.assertFalse(
            SVG_REGEX.match(
                "<svg></svg>"
                '<script type="this looks valid but is malicious"></script>'
                "<svg></svg>"
            )
        )


@override_settings(
    MOCK_STATICFILES_PATTERNS={},
    STATICFILES_DIRS=[
        os.path.join(
            os.path.dirname(os.path.dirname(__file__)), "staticfiles"
        ),
    ],
)
class SvgIconTests(TestCase):
    def test_assert_renders_valid_svg_from_staticfiles_icons(self):
        self.assertEqual(svg_icon("test"), VALID_SVG)

    def test_svg_icon_result_marked_safe_for_rendering(self):
        self.assertIsInstance(svg_icon("test"), SafeData)

    def test_invalid_svg_raises_value_error(self):
        with self.assertRaises(ValueError):
            load_svg("invalid")

    def test_missing_svg_raises_file_not_found_error(self):
        with self.assertRaises(FileNotFoundError):
            load_svg("missing")

    def test_template_tag(self):
        template = Template('{% load svg_icon %}{% svg_icon "test" %}')
        self.assertEqual(template.render(Context()), VALID_SVG)

    @patch("core.templatetags.svg_icon.FALLBACK_ICON_NAME", "test")
    def test_template_tag_fallback(self):
        """
        This test is for svg_icon.FALLBACK_ICON_NAME and related functionality
        Should return the icon associated with FALLBACK_ICON_NAME when
        an invalid icon name is used.
        """
        template = Template('{% load svg_icon %}{% svg_icon "invalid" %}')
        self.assertEqual(template.render(Context()), VALID_SVG)

    @patch("core.templatetags.svg_icon.FALLBACK_ICON_NAME", "missing")
    def test_missing_fallback_raises_file_not_found_error(self):
        template = Template('{% load svg_icon %}{% svg_icon "invalid" %}')
        with self.assertRaises(FileNotFoundError):
            template.render(Context())

    @patch("core.templatetags.svg_icon.FALLBACK_ICON_NAME", "invalid")
    def test_invalid_fallback_raises_value_error(self):
        template = Template('{% load svg_icon %}{% svg_icon "invalid" %}')
        with self.assertRaises(ValueError):
            template.render(Context())
