
from django import template
from django.template.defaultfilters import stringfilter
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter
@stringfilter
def priority_btn(priority, btn_size="xs"):
    '''given a ticket priority and button size, return a colour-coded
    bootstrap button with an appropriate label.
    '''

    btn_map = {
        '1': ['danger', 'Critical'],
        '2': ['warning', 'High'],
        '3': ['success', 'Normal'],
        '4': ['info', 'Low'],
        '5': ['default', 'Very Low'],
    }

    btn_attr = btn_map.get(priority)
    btn = '<button type="button" class="btn btn-{0} btn-{1}">{2}</button>'
    btn = btn.format(btn_attr[0], btn_size, btn_attr[1])

    return mark_safe(btn)


@register.filter
@stringfilter
def status_btn(status, btn_size='xs'):
    '''given a ticket status and button size, return a colour-coded
    bootstrap button with an appropriate label.
    '''

    btn_map = {
        'new': ['success', 'New'],
        'accepted': ['info', 'Accepted'],
        'assigned': ['primary', 'Assigned'],
        'reopened': ['warning', 'Reopened'],
        'closed': ['default', 'Closed'],
        'duplicate': ['default', 'Closed - Duplicate'],
        'split': ['default', 'Closed - Split'],
    }

    btn_attr = btn_map.get(status.lower(), ['default', status])

    if btn_size == 'lg' and status in ('closed', 'duplicate', 'split'):
        btn_attr[0] = 'danger'

    btn = '<button type="button" class="btn btn-{0} btn-{1}">{2}</button>'
    btn = btn.format(btn_attr[0],  btn_size, btn_attr[1])

    return mark_safe(btn)


@register.filter
@stringfilter
def ticket_type_btn(ticket_type, btn_size="xs"):
    '''given a ticket type and button size, return a colour-coded
    bootstrap button with an appropriate label.
    '''

    btn_map = {
        'bug': ['danger', 'Bug Report'],
        'feature': ['default', 'Feature Request'],
    }

    btn_attr = btn_map.get(ticket_type.lower())
    btn = '<button type="button" class="btn btn-{0} btn-{1}">{2}</button>'
    btn = btn.format(btn_attr[0],  btn_size, btn_attr[1])

    return mark_safe(btn)


@register.filter
@stringfilter
def classify(ticket_attribute):
    '''Given a ticket attribute, return a string representation that could
    be used to to assign a class in an html template.

    '''

    classString = ticket_attribute.replace(' ', '-').replace('_', '-').lower()

    return mark_safe(classString)


@register.filter
@stringfilter
def space(string):
    '''A simple little template filter to replace underscores with spaces
    '''
    return mark_safe(string.replace('_', ' '))




@register.filter
@stringfilter
def format_action(string):
    '''A simple little template filter to return a title case, presence
    tense version of a ticket action

    '''

    action_map = {
        'reopened': 'Re-Open',
        'closed': 'Close',
        'new': 'New',
        'accept': 'Accept',
        'comment': 'Comment on ',
        'assigned': 'Assign',
        're-assign': 'Accept And Assign',
        'duplicate': 'Duplicate',
        'split': 'Split',
    }

    return mark_safe(action_map.get(string, string))
