"""A basic Chat Command highlighter"""
import re

from pygments.lexer import RegexLexer, bygroups
from pygments.token import *

__all__ = ("ChatCommandLexer",)

class ChatCommandLexer(RegexLexer):
    """Simple Lexer to highlight chat commands"""
    
    name = "ChatCommand"
    aliases = ["chatcommand","command","cmd"]
    filenames = ["*.chatcommand", "*.command", "*.cmd"]
    
    tokens = {
        'root': [
            (r'[\[\{<@]', Punctuation, 'option'),
            (r'\w', Text)
        ],
        'option': [
            (r'\|', Punctuation),
            (r'[^\[\{<>\}\]@\S]', Name.Tag),
            (r'[\[\{<@]', Punctuation, '#push'),
            (r'[\]\}>\S', Punctuation, '#pop')
        ]
    }