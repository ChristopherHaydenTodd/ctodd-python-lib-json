# Christopher H. Todd's Python Library For Interacting With JSON Objects and Files

The ctodd-python-lib-json project is responsible for writing and reading JSON files and objects. will handle encoding Python objects into JSON.

## Table of Contents

- [Dependencies](#dependencies)
- [Libraries](#libraries)
- [Example Scripts](#example-scripts)
- [Notes](#notes)
- [TODO](#todo)

## Dependencies

### Python Packages

- simplejson>=3.16.0

## Libraries

### [json_reading_helpers.py](https://github.com/ChristopherHaydenTodd/ctodd-python-lib-json/blob/master/json_helpers/json_reading_helpers.py)

This library is used to aid in the task of reading .json files

Functions:

```
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
```

### [json_writing_helpers.py](https://github.com/ChristopherHaydenTodd/ctodd-python-lib-json/blob/master/json_helpers/json_writing_helpers.py)

This library is used to aid in the task of reading .json files

Functions:

```
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
```

## Example Scripts

Example executable Python scripts/modules for testing and interacting with the library. These show example use-cases for the libraries and can be used as templates for developing with the libraries or to use as one-off development efforts.

### N/A

## Notes

 - Relies on f-string notation, which is limited to Python3.6.  A refactor to remove these could allow for development with Python3.0.x through 3.5.x

## TODO

 - Unittest framework in place, but lacking tests
