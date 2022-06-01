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

    def mprint(self, message, print_std=True):

        logging.info(message)

        if print_std:
            try:
                print(message)
                sys.stdout.flush()

            except Exception as e:
                pass
