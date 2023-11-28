def on_pre_page_macros(env):
    footer = "\n\n{% import 'game.md' as game %}"
    env.markdown += footer