import logging


def setup_logger(path: str = "./logs/example.log", location: str = ""):
    logger = logging.getLogger(__name__)
    handler = logging.StreamHandler()
    formatter = logging.Formatter(
        f"{location}: %(levelname)s: -- %(message)s --: %(asctime)s"
    )
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(logging.DEBUG)
    return logger
