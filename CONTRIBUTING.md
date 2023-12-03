# Contributing

We are always happy for contributions towards this wiki, no matter how big or small they are.  
This file was made to explain the basics of contributing and what we expect from you to do, to have your changes approved and merged into this repository.

## Terminology

The following words and sentences will be used throughout this document.

| Term             | Description                                                                                             |
|------------------|---------------------------------------------------------------------------------------------------------|
| Git              | Open source, distributed version control system. See [git-scm.com][git] for more info.                  |
| Fork             | A copy of this repository you made on GitHub.                                                           |
| Local repository | Your forked cloned to your PC using the `git clone` command.                                            |
| Branch           | Git term used to describe a separate "version" of the repository.                                       |
| Commit           | Git term describing the addition of one or multiple changes to a repo's version history                 |
| Pull request     | Method used on GitHub to integrate changes made from a separate branch (and from a fork) into the repo. |
| Pip              | Command included in Python to install and manage python libraries.                                      |

[git]: https://git-scm.com

## Requirements and Prerequisits

Before you start contributing should you make sure to have covered the following points first.

- You have a decent understanding of Git and GitHub including but not limited to...
  - ...knowing how to fork this repo and keep it updated.
  - ...knowing how to clone your fork to a local repository on your PC.
  - ...know how to make new branches, commit changes to it and push these changes to your fork on GitHub
  - ...know how to create Pull requests
- You have basic understanding of how to use Python and MkDocs.
  - MkDocs is the site generator we use for the wiki and it relies on Python 3.10 or newer
  - Knowledge of using the `pip` command including installing dependencies from a file is recommended.

We do not have the resources nor the time to explain to you the basics of Git and GitHub, aswell as how to install Python. Countless tutorials exist explaining these things to you better than we could, so don't hesitate looking for them.

In order for you to properly contribute is it recommended to have a fork of this repository on GitHub and have it copied to your PC for modifications. In addition should you make sure of the following:

- You installed all necessary dependencies for this project.
  The easiest way would be to run `pip install -r requirements.txt` on your local repository.
- `mkdocs serve` can be used, namely the port it uses (8000) for the live-preview.

## Adding pages

This section explains what you need to look out for if you add new pages to the wiki.

### For any kind of page

No matter the page, you need to make sure to include it in the `nav` list of the `mkdocs.yml` file. Otherwise will MkDocs not recognize the file as being part of the site's navigation and exclude it from it. The page itself will still be accessible, but it won't be shown in any navigation.

### Minigame page

#### Macros

If your page covers a new minigame should you include specific Macros ([What is a Macro?][macro]).

The first required macro is the [`game.info(...)`][game.inf] macro. It is used to display common minigame info on the Page itself.  
The position is important: It has to be the first thing after the h1 header of the page.

> [!NOTE]
> The `game.info` macro only covers the current (Gen 3) games and isn't suited for game pages of previous versions. Instead, you have to manually create the necessary content.

The second macro should be the [`game.history(...)`][game.history] macro. It displays all the changes made to this game, including its addition.  
The position should be at the very bottom of the page.

Finally, should the game have a version from YouTube (Given that it is a twitch version game) should you add the [`game.yt_version(Path)`][game.yt_version] macro at the very top of the page (Above the h1 header but below any YAML frontmatter).

Here is an example of a possible minigame page:  
```markdown
---
description: Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam
---

{{ game.yt_version("common/lorem-ipsum/") }}

# Lorem Ipsum

{{ game.info() }}

Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam

{{ game.history({
    'v0.1': [
        'Minigame added'
    ]
}) }}
```

[macro]: https://chaosleaguewiki.github.io/meta/#macros
[game.info]: https://chaosleaguewiki.github.io/meta/macros/game/#game.info
[game.history]: https://chaosleaguewiki.github.io/meta/macros/game/#game.history
[game.yt_version]: https://chaosleaguewiki.github.io/meta/macros/game/#game.yt_version

### Changelog page

The [CL3 Changelog page][changelog] is, for the most part, automatically generated. It pulls content from other files to display.  
As such should any new changelog be added as a separate file in the `changelog/cl3/` folder. This page itself uses the [`utils.table(...)`][utils.table] macro to generate the Table used for the changelog.

A `.template.md` file exists that allows you to just copy it and modify it for the new changelog. What is important here is to set a proper `weight` YAML frontmatter. It is used to sort the pages in proper order.  
Should the changelog be a new version not yet added to the wiki can you just check the weight of the previous changelog entry and add one to it for yours, meaning if previous changelog has weight 16, should yours be weight 17.

[changelog]: https://chaosleaguewiki.github.io/changelog
[utils.table]: https://chaosleaguewiki.github.io/meta/macros/utils/#utils.table
