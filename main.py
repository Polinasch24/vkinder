import logging
import sys
from pathlib import Path

from bot import Bot
from config import config
from storage.memory import PersistentStorage

root_logger = logging.getLogger()
root_logger.setLevel(logging.DEBUG)

ch = logging.StreamHandler(sys.stdout)
ch.setLevel(logging.DEBUG)
root_logger.addHandler(ch)

if __name__ == "__main__":
    root_logger.info("Starting bot...")
    storage = PersistentStorage(Path(__file__).parent.resolve() / "data.pickle")
    bot = Bot(config, storage)
    bot.run()