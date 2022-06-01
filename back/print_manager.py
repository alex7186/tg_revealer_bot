import sys
import logging


class Logger:
    def __init__(self, SCRIPT_PATH):
        logging.basicConfig(
            filename=f"{SCRIPT_PATH}/misc/logfile.txt",
            filemode="a",
            format="%(asctime)s %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
            level=logging.INFO,
        )

    def mprint(self, message):

        logging.info(message)

        try:
            print(message)
            sys.stdout.flush()

        except Exception as e:
            pass
