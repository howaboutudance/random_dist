import logging
from . import run
logging.basicConfig(level=logging.DEBUG)


logging.info("starting process...")

if __name__ == "__main__":
    run.start()