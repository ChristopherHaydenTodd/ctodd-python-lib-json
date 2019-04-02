"""
    Purpose:
        JSON Reading Helpers.

        This library is used to aid in the task of reading .json files
"""

# Python Library Imports
import logging
import os
import simplejson as json


###
# Reading Helpers
###


def read_json_file_into_memory(json_file):
    """
    Purpose:
        Read properly formatted JSON file into memory.
    Args:
        json_file (String): Filename for JSON file to load (including path)
    Returns:
        json_object (Dictonary): Dictonary representation JSON Object
    Examples:
        >>> json_file = 'some/path/to/file.json'
        >>> json_object = read_json_file_into_memory(json_file)
        >>> print(json_object)
        >>> {
        >>>     'key': 'value'
        >>> }
    """
    logging.info(f"Reading JSON File Into Memory: {json_file}")

    try:
        with open(json_file, "r") as json_file_obj:
            return json.load(json_file_obj)
    except Exception as err:
        logging.exception(f"Cannot Read json into memory ({json_file}): {err}")
        raise err


def convert_bytes_array_to_json(bytes_array, encoding="utf-8"):
    """
    Purpose:
        Read Bytes-Array (of a JSON Object) To a JSON Object
    Args:
        bytes_array (Bytes Array): Bytes-Array of a JSON Object
    Returns:
        json_object (Dictonary): Dictonary representation JSON Object
    """

    str_representation = bytes_array.decode(encoding)
    str_representation = str_representation.replace("'", '"')
    json_object = json.loads(str_representation)

    return json_object

