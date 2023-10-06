# -*- coding: utf-8 -*-
import os
import sys
import logging
import typing as t


_logger: t.Optional[logging.Logger] = None


def _has_level_handler(logger: logging.Logger) -> bool:
    """Check if there is a handler in the logging chain that will handle
    the given logger's effective level.
    """
    level = logger.getEffectiveLevel()
    current = logger

    while current:
        if any(handler.level <= level for handler in current.handlers):
            return True
        if not current.propagate:
            break
        current = current.parent  # type: ignore
    return False


class _ColorStreamHandler(logging.StreamHandler):
    """On Windows, wrap stream with Colorama for ANSI style support."""

    def __init__(self) -> None:
        try:
            import colorama
        except ImportError:
            stream = None
        else:
            stream = colorama.AnsiToWin32(sys.stderr)
        super().__init__(stream)
        

def _log(type: str, message: str, *args: t.Any, **kwargs: t.Any) -> None:
    """Log a message to the 'dipense' logger.

    The logger is created the first time it is needed. If there is no
    level set, it is set to :data:`logging.INFO`. If there is no handler
    for the logger's effective level, a :class:`logging.StreamHandler`
    is added.
    """
    global _logger

    if _logger is None:
        _logger = logging.getLogger("dipense")

        if _logger.level == logging.NOTSET:
            _logger.setLevel(logging.INFO)

        if not _has_level_handler(_logger):
            _logger.addHandler(_ColorStreamHandler())
    getattr(_logger, type)(message.rstrip(), *args, **kwargs)


_log_add_style = True

if os.name == "nt":
    try:
        __import__("colorama")
    except ImportError:
        _log_add_style = False
        

def _ansi_style(value: str, *styles: str) -> str:
    if not _log_add_style:
        return value
    
    codes = {
        "bold": 1,
        "red": 31,
        "green": 32,
        "yellow": 33,
        "magenta": 35,
        "cyan": 36,
    }

    for style in styles:
        value = f"\x1b[{codes[style]}m{value}"
    return f"{value}\x1b[0m"


getout = print

def log_style(msg, *args, log='info', col=None):
    """
    logging style
    
    usage:
        >>> log_style('I am info log', log='info')
        >>> log_style('I am warning log', log='warning')
        >>> log_style('I am error log', log='error')
        >>> log_style('I am critical log', log='critical')

        # this two are thesame (inter-changebly), (use if text need to be bold)
        >>> log_style('I am error log of cyan(color) bold txt', 'cyan', log='error', col='bold')
        >>> log_style('I am error log of cyan(color) bold txt', 'bold', log='error', col='cyan')

        # this just change color to magenta
        >>> log_style('I am error log of magenta(color) bold txt', 'bold', log='error', col='magenta')
    """
    
    if col == None:
        if log == 'info':
            col = 'green'
        elif log == 'warning':
            col = 'yellow'
        elif log == 'error':
            col = 'red'
        elif log == 'critical':
            col = 'cyan'
        else: # if any
            col = 'magenta'
    return _log(log, _ansi_style(msg, col, *args))
