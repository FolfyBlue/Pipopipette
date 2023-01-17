import os
import sys


def resource_path(relative_path: str) -> str:
    """Used to make resources available through compilation using pyinstaller

    Args:
        relative_path (str): Relative path to the ressource

    Returns:
        str: Absolute path to the ressource to use
    """
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)  # type: ignore
    return os.path.join(os.path.abspath("."), relative_path)
