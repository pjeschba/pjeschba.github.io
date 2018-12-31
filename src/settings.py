import os


# General
def parent_dir(path):
    '''Return the parent of a directory.'''
    return os.path.abspath(os.path.join(path, os.pardir))


DEBUG = True
TEMPLATES_AUTO_RELOAD = True
APP_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = parent_dir(APP_DIR)


# Flask freeze config
FREEZER_DESTINATION = PROJECT_ROOT
FREEZER_BASE_URL = "https://patrickeschbach.com"
FREEZER_REMOVE_EXTRA_FILES = False  # Needed since we build in proj_root

# Flatpages config
FLATPAGES_ROOT = os.path.join(APP_DIR, 'pages')
FLATPAGES_EXTENSION = '.md'
