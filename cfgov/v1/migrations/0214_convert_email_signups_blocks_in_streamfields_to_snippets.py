# Generated by Django 3.2.13 on 2022-05-26 18:31

from functools import partial

from django.db import migrations

from v1.util.migrations import (
    convert_emailsignup_block_to_snippet,
    migrate_page_types_and_fields,
)


def forwards(apps, schema_editor):
    page_types_and_fields = [
        ('v1', 'BlogPage', 'content', ['full_width_text', 'email_signup']),
        ('v1', 'BrowseFilterablePage', 'content', ['full_width_text', 'email_signup']),
        ('v1', 'BrowsePage', 'content', ['full_width_text', 'email_signup']),
        ('v1', 'EnforcementActionPage', 'content', ['full_width_text', 'email_signup']),
        ('v1', 'LearnPage', 'content', ['full_width_text', 'email_signup']),
        ('v1', 'DocumentDetailPage', 'content', ['full_width_text', 'email_signup']),
        ('v1', 'StoryPage', 'content', ['full_width_text', 'email_signup']),
        ('v1', 'SublandingFilterablePage', 'content', ['full_width_text', 'email_signup']),
        ('v1', 'SublandingPage', 'content', ['full_width_text', 'email_signup']),
    ]
    migrate_page_types_and_fields(
        apps,
        page_types_and_fields,
        partial(convert_emailsignup_block_to_snippet, apps)
    )


class Migration(migrations.Migration):

    dependencies = [
        ('v1', '0213_convert_email_signups_blocks_in_pages_to_snippets'),
    ]

    operations = [
        migrations.RunPython(forwards),
    ]

