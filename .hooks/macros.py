import posixpath
import json
import markdown

def define_env(env):
    
    @env.macro
    def read_json_file(file_path: str):
        """
        Reads a JSON file from the provided path (Relative to the docs_dir) and gives it as a usable object for jinja2 templating.
        """
        path = posixpath.sep.join([env.project_dir, file_path])
        with open(path, 'r', encoding='utf-8') as file:
            return json.load(file)
    
    @env.macro
    def read_file(file_path: str):
        """
        Reads a file from the provided path (Relative to root of project) and gives it back.
        """
        path = posixpath.sep.join([env.project_dir, file_path])
        with open(path, 'r', encoding='utf-8') as file:
            return file.readlines()
    
    @env.filter
    def markdownify(text: str):
        md = markdown.Markdown(
            extensions=env.conf['markdown_extensions'],
            extension_configs=env.conf['mdx_configs'] or {}
        )
        # markdown adds <p> tags, which we don't need here.
        return md.convert(text).replace('<p>', '').replace('</p>', '')

def on_pre_page_macros(env):
    """
    Injects an import statement at the top to add game-page related macros.
    """
    header = "{% import 'game.md' as game with context %}\n{% import 'image.md' as image with context %}\n{% import 'utils.md' as utils with context %}\n\n" + env.markdown
    env.markdown = header