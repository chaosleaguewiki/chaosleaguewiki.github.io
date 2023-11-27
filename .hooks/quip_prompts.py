import jinja2
import posixpath
import json

from mkdocs.structure.files import File, Files
from mkdocs.config.defaults import MkDocsConfig
from mkdocs.structure.pages import Page

def on_page_markdown(markdown: str, page: Page, files: Files, config: MkDocsConfig, **kwargs):
    if page.file.src_uri != 'twitch-minigames/common/quip-battle.md':
        return
    
    path = posixpath.sep.join([config.docs_dir, "assets/extra_quips.json"])
    with open(path, encoding="utf-8") as json_file:
        json_content = json.load(json_file)
    
    return jinja2.Template(markdown).render(json = json_content)