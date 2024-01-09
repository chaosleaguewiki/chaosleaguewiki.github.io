---
description: Trail Shop is an epic Shop tile added in v0.12 Alpha, where players can buy a different color for their trail, using the gold they earned.
---

# Trail Shop

{{ game.info(
  rarity           = ["epic"],
  inputs           = "[`!buy`][buy-command]",
  timer            = "29 seconds",
  slots_guaranteed = "8",
  slots_raffle     = "4",
  added            = "v0.12 Alpha",
  
  img_url = "../../../assets/images/minigames/twitch/epic/trail-shop.png"
) }}

**Trail Shop** is an epic Shop tile added in v0.12 Alpha, where players can buy a different color for their trail, using the [gold they earned](../../mechanics/attacking-the-king.md).

## Gameplay

The tile is split up into three sections, each showing a preview of a trail the player can buy.

From top to bottom, the trails increase in price while also being larger in length and having more colors with the top having only one color and being the shortest and the bottom one having three colors and being the longest trail.

Once the game starts, each player can use the [`!buy<number>` command][buy-command] where `<number>` is a number between 1 and 3, matching one of the displayed trails. If the player has enough gold to purchase the trail, their marble will be moved to the trail before moving towards the bottom center of the screen with the new trail applied. The sound of an old cash register is also played as an audible confirmation of the purchase.

The colors a trail can have are randomly chosen whenever the tile is being selected. Previously purchased trails can't be re-equipped again.

{{ game.history({
  'v0.12 Alpha': [
    'Minigame added'
  ],
  'v0.13 Alpha': [
    'King can complete purchases in shop tiles without leaving the throne'
  ]
}) }}