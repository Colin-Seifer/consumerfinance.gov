# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import v1.models.snippets
import wagtail.wagtailcore.fields
import wagtail.wagtailcore.blocks
import wagtail.wagtailimages.blocks
import v1.util.ref
import v1.atomic_elements.organisms


class Migration(migrations.Migration):

    dependencies = [
        ('v1', '0058_adding_clickable_image_to_50_50'),
    ]

    operations = [
        migrations.AlterField(
            model_name='browsefilterablepage',
            name='content',
            field=wagtail.wagtailcore.fields.StreamField([(b'full_width_text', wagtail.wagtailcore.blocks.StreamBlock([(b'content_with_anchor', wagtail.wagtailcore.blocks.StructBlock([(b'content_block', wagtail.wagtailcore.blocks.RichTextBlock()), (b'anchor_link', wagtail.wagtailcore.blocks.StructBlock([(b'link_id', wagtail.wagtailcore.blocks.CharBlock(help_text=(b'Auto-generated on save, or enter some human-friendly text ', b'to make it easier to read.'), required=False, label=b'ID for this content block'))]))])), (b'content', wagtail.wagtailcore.blocks.RichTextBlock(icon=b'edit')), (b'media', wagtail.wagtailimages.blocks.ImageChooserBlock(icon=b'image')), (b'quote', wagtail.wagtailcore.blocks.StructBlock([(b'body', wagtail.wagtailcore.blocks.TextBlock()), (b'citation', wagtail.wagtailcore.blocks.TextBlock())])), (b'cta', wagtail.wagtailcore.blocks.StructBlock([(b'slug_text', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'paragraph_text', wagtail.wagtailcore.blocks.RichTextBlock(required=False)), (b'button', wagtail.wagtailcore.blocks.StructBlock([(b'text', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'url', wagtail.wagtailcore.blocks.CharBlock(default=b'/', required=False))]))])), (b'related_links', wagtail.wagtailcore.blocks.StructBlock([(b'heading', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'paragraph', wagtail.wagtailcore.blocks.RichTextBlock(required=False)), (b'links', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock([(b'text', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'url', wagtail.wagtailcore.blocks.CharBlock(default=b'/', required=False))])))])), (b'table', wagtail.wagtailcore.blocks.StructBlock([(b'headers', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.CharBlock())), (b'rows', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StreamBlock([(b'hyperlink', wagtail.wagtailcore.blocks.StructBlock([(b'text', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'url', wagtail.wagtailcore.blocks.CharBlock(default=b'/', required=False))])), (b'text', wagtail.wagtailcore.blocks.CharBlock()), (b'text_blob', wagtail.wagtailcore.blocks.TextBlock()), (b'rich_text_blob', wagtail.wagtailcore.blocks.RichTextBlock())])))], editable=False)), (b'table_block', v1.atomic_elements.organisms.AtomicTableBlock(table_options={b'renderer': b'html'})), (b'image_inset', wagtail.wagtailcore.blocks.StructBlock([(b'image', wagtail.wagtailcore.blocks.StructBlock([(b'upload', wagtail.wagtailimages.blocks.ImageChooserBlock(required=False)), (b'alt', wagtail.wagtailcore.blocks.CharBlock(required=False))])), (b'image_position', wagtail.wagtailcore.blocks.ChoiceBlock(default=b'right', choices=[(b'right', b'right'), (b'left', b'left')])), (b'is_image_decorative', wagtail.wagtailcore.blocks.BooleanBlock(required=False, label=b'Image decorative')), (b'image_width', wagtail.wagtailcore.blocks.ChoiceBlock(default=270, help_text=b'Default is 270px.', choices=[(170, b'170px'), (270, b'270px')], label=b'Image Width')), (b'text', wagtail.wagtailcore.blocks.RichTextBlock(required=False)), (b'is_bottom_rule', wagtail.wagtailcore.blocks.BooleanBlock(default=True, required=False, label=b'Bottom Rule'))])), (b'reusable_text', v1.models.snippets.ReusableTextChooserBlock(v1.models.snippets.ReusableText))])), (b'filter_controls', wagtail.wagtailcore.blocks.StructBlock([(b'label', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'is_bordered', wagtail.wagtailcore.blocks.BooleanBlock(required=False)), (b'is_midtone', wagtail.wagtailcore.blocks.BooleanBlock(required=False)), (b'is_expanded', wagtail.wagtailcore.blocks.BooleanBlock(required=False)), (b'form_type', wagtail.wagtailcore.blocks.ChoiceBlock(default=b'filterable-list', choices=[(b'filterable-list', b'Filterable List'), (b'pdf-generator', b'PDF Generator')])), (b'title', wagtail.wagtailcore.blocks.BooleanBlock(default=True, required=False, label=b'Filter Title')), (b'post_date_description', wagtail.wagtailcore.blocks.CharBlock(default=b'Published')), (b'categories', wagtail.wagtailcore.blocks.StructBlock([(b'filter_category', wagtail.wagtailcore.blocks.BooleanBlock(default=True, required=False)), (b'show_preview_categories', wagtail.wagtailcore.blocks.BooleanBlock(default=True, required=False)), (b'page_type', wagtail.wagtailcore.blocks.ChoiceBlock(required=False, choices=v1.util.ref.filterable_list_page_types))])), (b'topics', wagtail.wagtailcore.blocks.BooleanBlock(default=True, required=False, label=b'Filter Topics')), (b'authors', wagtail.wagtailcore.blocks.BooleanBlock(default=True, required=False, label=b'Filter Authors')), (b'date_range', wagtail.wagtailcore.blocks.BooleanBlock(default=True, required=False, label=b'Filter Date Range')), (b'output_5050', wagtail.wagtailcore.blocks.BooleanBlock(default=False, required=False, label=b'Render preview items as 50-50s')), (b'should_link_image', wagtail.wagtailcore.blocks.BooleanBlock(help_text=b'Add links to post preview images in filterable list results', default=False, required=False))])), (b'feedback', wagtail.wagtailcore.blocks.StructBlock([(b'was_it_helpful_text', wagtail.wagtailcore.blocks.CharBlock(help_text=b'Use this field only for feedback forms that use "Was this helpful?" radio buttons.', default=b'Was this page helpful to you?', required=False)), (b'intro_text', wagtail.wagtailcore.blocks.CharBlock(help_text=b'Optional feedback intro', required=False)), (b'question_text', wagtail.wagtailcore.blocks.CharBlock(help_text=b'Optional expansion on intro', required=False)), (b'radio_intro', wagtail.wagtailcore.blocks.CharBlock(help_text=b'Leave blank unless you are building a feedback form with extra radio-button prompts, as in /owning-a-home/help-us-improve/.', required=False)), (b'radio_text', wagtail.wagtailcore.blocks.CharBlock(default=b'This information helps us understand your question better.', required=False)), (b'radio_question_1', wagtail.wagtailcore.blocks.CharBlock(default=b'How soon do you expect to buy a home?', required=False)), (b'radio_question_2', wagtail.wagtailcore.blocks.CharBlock(default=b'Do you currently own a home?', required=False)), (b'button_text', wagtail.wagtailcore.blocks.CharBlock(default=b'Submit')), (b'contact_advisory', wagtail.wagtailcore.blocks.RichTextBlock(help_text=b'Use only for feedback forms that ask for a contact email', required=False))]))]),
        ),
        migrations.AlterField(
            model_name='cfgovpagecategory',
            name='name',
            field=models.CharField(max_length=255, choices=[(b'Administrative adjudication docket', ((b'administrative-adjudication', b'Administrative adjudication'), (b'stipulation-and-constent-order', b'Stipulation and consent order'))), (b'Amicus Brief', ((b'us-supreme-court', b'U.S. Supreme Court'), (b'fed-circuit-court', b'Federal Circuit Court'), (b'fed-district-court', b'Federal District Court'), (b'state-court', b'State Court'))), (b'Blog', ((b'at-the-cfpb', b'At the CFPB'), (b'policy_compliance', b'Policy & Compliance'), (b'data-research-reports', b'Data, research & reports'), (b'info-for-consumers', b'Info for consumers'))), (b'Enforcement Action', ((b'fed-district-case', b'Federal district court case'), (b'administrative-adjudication-2', b'Administrative adjudication'), (b'stipulation-and-consent-order-2', b'Stipulation and consent order'))), (b'Final Rule', ((b'interim-final-rule', b'Interim Final Rule'), (b'final-rule', b'Final Rule'))), (b'FOIA Frequently Requested Record', ((b'report', b'Report'), (b'log', b'Log'), (b'record', b'Record'))), (b'Implementation Resource', ((b'compliance-aid', b'Compliance aid'), (b'official-guidance', b'Official guidance'))), (b'Newsroom', ((b'op-ed', b'Op-Ed'), (b'press-release', b'Press Release'), (b'speech', b'Speech'), (b'testimony', b'Testimony'))), (b'Notice and Opportunity for Comment', ((b'notice-proposed-rule', b'Advanced Notice of Proposed Rulemaking'), (b'proposed-rule', b'Proposed Rule'), (b'interim-final-rule-2', b'Interim Final Rule'), (b'request-comment-info', b'Request for Comment or Information'), (b'proposed-policy', b'Proposed Policy'), (b'intent-preempt-determ', b'Intent to make Preemption Determination'), (b'info-collect-activity', b'Information Collection Activities'), (b'notice-privacy-act', b'Notice related to Privacy Act'))), (b'Research Report', ((b'consumer-complaint', b'Consumer Complaint'), (b'super-highlight', b'Supervisory Highlights'), (b'data-point', b'Data Point'), (b'industry-markets', b'Industry and markets'), (b'consumer-edu-empower', b'Consumer education and empowerment'), (b'to-congress', b'To Congress'))), (b'Rule under development', ((b'notice-proposed-rule-2', b'Advanced Notice of Proposed Rulemaking'), (b'proposed-rule-2', b'Proposed Rule'))), (b'Story', ((b'auto-loans', b'Auto loans'), (b'bank-accts-services', b'Bank accounts and services'), (b'credit-cards', b'Credit cards'), (b'credit-reports-scores', b'Credit reports and scores'), (b'debt-collection', b'Debt collection'), (b'money-transfers', b'Money transfers'), (b'mortgages', b'Mortgages'), (b'payday-loans', b'Payday loans'), (b'prepaid-cards', b'Prepaid cards'), (b'student-loans', b'Student loans')))]),
        ),
        migrations.AlterField(
            model_name='sublandingfilterablepage',
            name='content',
            field=wagtail.wagtailcore.fields.StreamField([(b'text_introduction', wagtail.wagtailcore.blocks.StructBlock([(b'heading', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'intro', wagtail.wagtailcore.blocks.RichTextBlock(required=False)), (b'body', wagtail.wagtailcore.blocks.RichTextBlock(required=False)), (b'links', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock([(b'text', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'url', wagtail.wagtailcore.blocks.CharBlock(default=b'/', required=False))]), required=False)), (b'has_rule', wagtail.wagtailcore.blocks.BooleanBlock(required=False))])), (b'full_width_text', wagtail.wagtailcore.blocks.StreamBlock([(b'content_with_anchor', wagtail.wagtailcore.blocks.StructBlock([(b'content_block', wagtail.wagtailcore.blocks.RichTextBlock()), (b'anchor_link', wagtail.wagtailcore.blocks.StructBlock([(b'link_id', wagtail.wagtailcore.blocks.CharBlock(help_text=(b'Auto-generated on save, or enter some human-friendly text ', b'to make it easier to read.'), required=False, label=b'ID for this content block'))]))])), (b'content', wagtail.wagtailcore.blocks.RichTextBlock(icon=b'edit')), (b'media', wagtail.wagtailimages.blocks.ImageChooserBlock(icon=b'image')), (b'quote', wagtail.wagtailcore.blocks.StructBlock([(b'body', wagtail.wagtailcore.blocks.TextBlock()), (b'citation', wagtail.wagtailcore.blocks.TextBlock())])), (b'cta', wagtail.wagtailcore.blocks.StructBlock([(b'slug_text', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'paragraph_text', wagtail.wagtailcore.blocks.RichTextBlock(required=False)), (b'button', wagtail.wagtailcore.blocks.StructBlock([(b'text', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'url', wagtail.wagtailcore.blocks.CharBlock(default=b'/', required=False))]))])), (b'related_links', wagtail.wagtailcore.blocks.StructBlock([(b'heading', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'paragraph', wagtail.wagtailcore.blocks.RichTextBlock(required=False)), (b'links', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock([(b'text', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'url', wagtail.wagtailcore.blocks.CharBlock(default=b'/', required=False))])))])), (b'table', wagtail.wagtailcore.blocks.StructBlock([(b'headers', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.CharBlock())), (b'rows', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StreamBlock([(b'hyperlink', wagtail.wagtailcore.blocks.StructBlock([(b'text', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'url', wagtail.wagtailcore.blocks.CharBlock(default=b'/', required=False))])), (b'text', wagtail.wagtailcore.blocks.CharBlock()), (b'text_blob', wagtail.wagtailcore.blocks.TextBlock()), (b'rich_text_blob', wagtail.wagtailcore.blocks.RichTextBlock())])))], editable=False)), (b'table_block', v1.atomic_elements.organisms.AtomicTableBlock(table_options={b'renderer': b'html'})), (b'image_inset', wagtail.wagtailcore.blocks.StructBlock([(b'image', wagtail.wagtailcore.blocks.StructBlock([(b'upload', wagtail.wagtailimages.blocks.ImageChooserBlock(required=False)), (b'alt', wagtail.wagtailcore.blocks.CharBlock(required=False))])), (b'image_position', wagtail.wagtailcore.blocks.ChoiceBlock(default=b'right', choices=[(b'right', b'right'), (b'left', b'left')])), (b'is_image_decorative', wagtail.wagtailcore.blocks.BooleanBlock(required=False, label=b'Image decorative')), (b'image_width', wagtail.wagtailcore.blocks.ChoiceBlock(default=270, help_text=b'Default is 270px.', choices=[(170, b'170px'), (270, b'270px')], label=b'Image Width')), (b'text', wagtail.wagtailcore.blocks.RichTextBlock(required=False)), (b'is_bottom_rule', wagtail.wagtailcore.blocks.BooleanBlock(default=True, required=False, label=b'Bottom Rule'))])), (b'reusable_text', v1.models.snippets.ReusableTextChooserBlock(v1.models.snippets.ReusableText))])), (b'filter_controls', wagtail.wagtailcore.blocks.StructBlock([(b'label', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'is_bordered', wagtail.wagtailcore.blocks.BooleanBlock(required=False)), (b'is_midtone', wagtail.wagtailcore.blocks.BooleanBlock(required=False)), (b'is_expanded', wagtail.wagtailcore.blocks.BooleanBlock(required=False)), (b'form_type', wagtail.wagtailcore.blocks.ChoiceBlock(default=b'filterable-list', choices=[(b'filterable-list', b'Filterable List'), (b'pdf-generator', b'PDF Generator')])), (b'title', wagtail.wagtailcore.blocks.BooleanBlock(default=True, required=False, label=b'Filter Title')), (b'post_date_description', wagtail.wagtailcore.blocks.CharBlock(default=b'Published')), (b'categories', wagtail.wagtailcore.blocks.StructBlock([(b'filter_category', wagtail.wagtailcore.blocks.BooleanBlock(default=True, required=False)), (b'show_preview_categories', wagtail.wagtailcore.blocks.BooleanBlock(default=True, required=False)), (b'page_type', wagtail.wagtailcore.blocks.ChoiceBlock(required=False, choices=v1.util.ref.filterable_list_page_types))])), (b'topics', wagtail.wagtailcore.blocks.BooleanBlock(default=True, required=False, label=b'Filter Topics')), (b'authors', wagtail.wagtailcore.blocks.BooleanBlock(default=True, required=False, label=b'Filter Authors')), (b'date_range', wagtail.wagtailcore.blocks.BooleanBlock(default=True, required=False, label=b'Filter Date Range')), (b'output_5050', wagtail.wagtailcore.blocks.BooleanBlock(default=False, required=False, label=b'Render preview items as 50-50s')), (b'should_link_image', wagtail.wagtailcore.blocks.BooleanBlock(help_text=b'Add links to post preview images in filterable list results', default=False, required=False))])), (b'featured_content', wagtail.wagtailcore.blocks.StructBlock([(b'heading', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'body', wagtail.wagtailcore.blocks.RichTextBlock(required=False)), (b'category', wagtail.wagtailcore.blocks.ChoiceBlock(required=False, choices=[(b'featured-event', b'Featured event'), (b'featured-blog', b'Featured blog'), (b'featured-video', b'Featured video'), (b'featured-tool', b'Featured tool'), (b'featured-news', b'Featured news'), (b'featured', b'Featured')])), (b'post', wagtail.wagtailcore.blocks.PageChooserBlock(required=False)), (b'show_post_link', wagtail.wagtailcore.blocks.BooleanBlock(required=False, label=b'Render post link?')), (b'post_link_text', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'image', wagtail.wagtailcore.blocks.StructBlock([(b'upload', wagtail.wagtailimages.blocks.ImageChooserBlock(required=False)), (b'alt', wagtail.wagtailcore.blocks.CharBlock(required=False))])), (b'links', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock([(b'text', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'url', wagtail.wagtailcore.blocks.CharBlock(default=b'/', required=False))]), label=b'Additional Links')), (b'video', wagtail.wagtailcore.blocks.StructBlock([(b'id', wagtail.wagtailcore.blocks.CharBlock(help_text=b'E.g., in "https://www.youtube.com/watch?v=en0Iq8II4fA", the ID is everything after the "?v=".', required=False, label=b'ID')), (b'url', wagtail.wagtailcore.blocks.CharBlock(help_text=b'You must use the embed URL, e.g., https://www.youtube.com/embed/JPTg8ZB3j5c?autoplay=1&enablejsapi=1', required=False, label=b'URL')), (b'height', wagtail.wagtailcore.blocks.CharBlock(default=b'320', required=False)), (b'width', wagtail.wagtailcore.blocks.CharBlock(default=b'568', required=False))]))])), (b'feedback', wagtail.wagtailcore.blocks.StructBlock([(b'was_it_helpful_text', wagtail.wagtailcore.blocks.CharBlock(help_text=b'Use this field only for feedback forms that use "Was this helpful?" radio buttons.', default=b'Was this page helpful to you?', required=False)), (b'intro_text', wagtail.wagtailcore.blocks.CharBlock(help_text=b'Optional feedback intro', required=False)), (b'question_text', wagtail.wagtailcore.blocks.CharBlock(help_text=b'Optional expansion on intro', required=False)), (b'radio_intro', wagtail.wagtailcore.blocks.CharBlock(help_text=b'Leave blank unless you are building a feedback form with extra radio-button prompts, as in /owning-a-home/help-us-improve/.', required=False)), (b'radio_text', wagtail.wagtailcore.blocks.CharBlock(default=b'This information helps us understand your question better.', required=False)), (b'radio_question_1', wagtail.wagtailcore.blocks.CharBlock(default=b'How soon do you expect to buy a home?', required=False)), (b'radio_question_2', wagtail.wagtailcore.blocks.CharBlock(default=b'Do you currently own a home?', required=False)), (b'button_text', wagtail.wagtailcore.blocks.CharBlock(default=b'Submit')), (b'contact_advisory', wagtail.wagtailcore.blocks.RichTextBlock(help_text=b'Use only for feedback forms that ask for a contact email', required=False))]))]),
        ),
    ]
