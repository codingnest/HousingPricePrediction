import logging
import os

from housing_model.config import config
from housing_model.config import logging_config

# Configure logger for use in package
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger.addHandler(logging_config.get_console_handler())
logger.propagate = False
#print(os.path.join(config.PACKAGE_ROOT, 'VERSION'))
with open(os.path.join(config.PACKAGE_ROOT, 'VERSION')) as version_file:
    __version__ = version_file.read().strip()