import sys
import os

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

def get_app_dir():
    if getattr(sys, 'frozen', False):
        # Executable mode
        return os.path.dirname(sys.executable)
    else:
        # Script mode
        return os.path.dirname(os.path.abspath(__file__))
