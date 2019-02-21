"""
    Purpose:
        JSON Writing Helpers.

        This library is used to aid in the task of reading .json files
"""

# Python Library Imports
import logging
import os
import simplejson as json


###
# Writing Helpers
###


def write_json_into_file(json_object, json_file):
    """
    Purpose:
        Load Dictionary into JSON File
    Args:
        json_object (Dictionary): Dictionary to be stored in .json format
        json_file (String): Filename for JSON file to store (including path)
    Returns:
        N/A
    Examples:
        >>> json_file = 'some/path/to/file.json'
        >>> json_object = {
        >>>     'key': 'value'
        >>> }
        >>> write_json_into_file(json_file, json_object)
    """
    logging.info("Writing JSON File Into Memory: {0}".format(json_file))

    with open(json_file, "w") as file:
        json.dump(
            json_object, file, sort_keys=True, indent=4, separators=(',', ': ')
        )
