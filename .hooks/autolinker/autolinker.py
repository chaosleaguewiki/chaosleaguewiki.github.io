from markdown.core import Markdown
from markdown.extensions import Extension
from markdown.blockprocessors import BlockProcessor
from markdown.inlinepatterns import InlineProcessor
from markdown.util import AtomicString

import xml.etree.ElementTree as etree

import re

class AutoLinkerExtension(Extension):
    """Auto-link extension for Python-Markdown"""
    
    def extendMarkdown(self, md) -> None:
        md.parser.blockprocessors.register(AutoLinkerPreProcessor(md.parser), 'autolinker', 16)

class AutoLinkerPreProcessor(BlockProcessor):
    """Auto-link Preprocessor - Parse text for autolink references"""
    
    RE = re.compile(r'^[.]\[(?P<text>[^\]]*)\][ ]?:[ ]*\n?[ ]*(?P<link>.*)$', re.MULTILINE)
    
    def run(self, parent: etree.Element, blocks: list[str]) -> bool:
        block = blocks.pop(0)
        m = self.RE.search(block)
        if m:
            text = m.group('text').strip()
            link = m.group('link').strip()
            self.parser.md.inlinePatterns.register(
                AutoLinkerInlineProcessor(self._generate_pattern(text), link), 'autolinker-%s' % text, 2
            )
            if block[m.end():].strip():
                blocks.insert(0, block[m.end():].lstrip('\n'))
            if block[:m.start()].strip():
                blocks.insert(0, block[:m.start()].rstrip('\n'))
            return True
        blocks.insert(0, block)
        return False

class AutoLinkerInlineProcessor(InlineProcessor):
    """AutoLinker inline pattern"""
    
    def __init__(self, pattern: str, link: str) -> None:
        super().__init__(pattern)
        self.link = link
    
    def handleMatch(self, m: re.Match[str], data: str) -> tuple[etree.Element, int, int]:
        a = etree.Element('a')
        a.text = AtomicString(m.group('text'))
        a.set('href', self.link)
        return a, m.start(0), m.end(0)

def makeExtension(**kwargs):
    return AutoLinkerExtension(**kwargs)