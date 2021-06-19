# import coloredlogs, logging
# from colorlog import ColoredFormatter
# # coloredlogs.install()
# # create logger
# logger = logging.getLogger()
# logger.setLevel(logging.DEBUG)

# # create console handler and set level to debug
# ch = logging.StreamHandler()
# ch.setLevel(logging.DEBUG)

# # create formatter
# # LOGFORMAT = "  %(log_color)s%(levelname)-8s%(reset)s | %(log_color)s%(message)s%(reset)s"
# LOGFORMAT = '%(threadName)s - %(asctime)s - %(name)s - %(levelname)s - %(log_color)s%(message)s'

# formatter = ColoredFormatter(LOGFORMAT)
# # add formatter to ch
# ch.setFormatter(formatter)

# # add ch to logger
# logger.addHandler(ch)

# https://gist.github.com/joshbode/58fac7ababc700f51e2a9ecdebe563ad
import sys
import logging
from typing import Optional, Dict

from colorama import Fore, Back, Style


class ColoredFormatter(logging.Formatter):
    """Colored log formatter."""

    def __init__(self, *args, colors: Optional[Dict[str, str]]=None, **kwargs) -> None:
        """Initialize the formatter with specified format strings."""

        super().__init__(*args, **kwargs)

        self.colors = colors if colors else {}

    def format(self, record) -> str:
        """Format the specified record as text."""

        record.color = self.colors.get(record.levelname, '')
        record.reset = Style.RESET_ALL

        return super().format(record)


formatter = ColoredFormatter(
    '{asctime} |{color} {levelname:8} {reset}| {name} | {message}',
    style='{', datefmt='%Y-%m-%d %H:%M:%S',
    colors={
        'DEBUG': Fore.CYAN,
        'INFO': Fore.GREEN,
        'WARNING': Fore.YELLOW,
        'ERROR': Fore.RED,
        'CRITICAL': Fore.RED + Back.WHITE + Style.BRIGHT,
    }
)


# formatter = ColoredFormatter(
#     '{color}[{levelname:.1s}] {message}{reset}',
#     style='{', datefmt='%Y-%m-%d %H:%M:%S',
#     colors={
#         'DEBUG': Fore.CYAN,
#         'INFO': Fore.GREEN,
#         'WARNING': Fore.YELLOW,
#         'ERROR': Fore.RED,
#         'CRITICAL': Fore.RED + Back.WHITE + Style.BRIGHT,
#     }
# )


handler = logging.StreamHandler(sys.stdout)
handler.setFormatter(formatter)

logger = logging.getLogger()
logger.handlers[:] = []
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)