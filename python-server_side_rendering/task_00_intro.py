#!/usr/bin/env python3
"""Simple templating program that generates invitation files."""

import logging
import os

logging.basicConfig(level=logging.INFO, format='%(message)s')
logger = logging.getLogger(__name__)

PLACEHOLDERS = ['name', 'event_title', 'event_date', 'event_location']


def generate_invitations(template, attendees):
    """Generate personalized invitation files from a template.

    Args:
        template (str): The invitation template with placeholders.
        attendees (list): A list of dictionaries with attendee data.
    """
    if not isinstance(template, str):
        logger.error("Invalid input: template must be a string.")
        return

    if not isinstance(attendees, list) or not all(
            isinstance(attendee, dict) for attendee in attendees):
        logger.error(
            "Invalid input: attendees must be a list of dictionaries.")
        return

    if not template:
        logger.error("Template is empty, no output files generated.")
        return

    if not attendees:
        logger.error("No data provided, no output files generated.")
        return

    for index, attendee in enumerate(attendees, start=1):
        output = template
        for placeholder in PLACEHOLDERS:
            value = attendee.get(placeholder)
            if value is None:
                value = "N/A"
            output = output.replace("{" + placeholder + "}", str(value))

        filename = "output_{}.txt".format(index)
        with open(filename, 'w', encoding='utf-8') as output_file:
            output_file.write(output)
