"""Tharun++"""
from . import ast, lexer, parser, runner, utils

__all__ = ["parser", "ast", "lexer", "runner", "utils"]

__version__ = "0.3.1"
__version_str__ = (
    f"Tharun++ v{__version__}."
    + "\nTharun++ is a programming language based on the famous comedy dialogues of Tamil cinema industry."
    + "\nCreated by Tharun Kumar(TharunkumarTQK@medium)."
)

rpp = runner.RppRunner()
