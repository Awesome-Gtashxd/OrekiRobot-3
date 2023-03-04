import sys

from OrekiRobot import LOGGER

except Exception as e:
    LOGGER.exception(f"Movies Failed to upload here")
    sys.exit()

LOGGER.info("Movies Connection successful, session started.")
