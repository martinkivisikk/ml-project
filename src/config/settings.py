import logging

LOGGING_CONFIG = {
    "level": logging.INFO,
    "format": "%(asctime)s [%(levelname)s] %(name)s.%(funcName)s: %(message)s",
}

def configure_logging():
    root = logging.getLogger()

    if root.handlers:
        root.handlers.clear()

    logging.basicConfig(**LOGGING_CONFIG)