"""
FilePathing.py

This file is responsible for handling the file directories to organize
the system and avoid mismatched file pathing.
"""

import sys
import os

# This function joins the relative path based on where the system is located on
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

# This function provides the directory where the app is located on
def get_app_dir():
    if getattr(sys, 'frozen', False):
        # Executable mode
        return os.path.dirname(sys.executable)
    else:
        # Script mode
        return os.path.dirname(os.path.abspath(__file__))
