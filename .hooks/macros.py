import posixpath
import json

def define_env(env):
    
    @env.macro
    def read_json_file(file_path: str):
        """
        Reads a JSON file from the provided path (Relative to the docs_dir) and gives it as a usable object for jinja2 templating.
        """
        path = posixpath.sep.join([env.conf.docs_dir, file_path])
        with open(path, encoding="utf-8") as json_file:
            return json.load(json_file)

def on_pre_page_macros(env):
    """
    Injects an import statement at the top to add game-page related macros.
    """
    footer = "{% import 'game.md' as game with context %}\n\n" + env.markdown
    env.markdown = footer