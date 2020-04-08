"""
pextn
"""

from typing import Dict, List

from pextn.consts import DATA

class UnknownExtension(Exception):
    """
    Used when an unknown exception is
    encountered.
    """

def pextn(extension: str) -> List[List[str]]:
    """
    Accepts the extension and returns its
    information list.

    Raises UnknownExtension if the extension
    is not known.
    """
    extension = extension.strip().upper()  # convert as data is upper case
    extension = extension.replace('.', '')
    if extension in DATA:
        return DATA[extension]
    raise UnknownExtension(extension)

