---
description: Trail Shop is an epic Shop tile, meaning instead of playing a game, you can purchase colored Trails using Gold you earned as king.
---

# Trail Shop

{{ game.info(
  rarity           = ["epic"],
  inputs           = "[`!buy`][buy-command]",
  timer            = "29 Seconds",
  slots_guaranteed = "8",
  slots_raffle     = "4",
  added            = "v0.12 Alpha",
  
  img_url = "../../../assets/images/minigames/twitch/trail-shop.png"
) }}

**Trail Shop** is an epic Shop tile, meaning instead of playing a game, you can purchase colored Trails using [Gold you earned as king](../../mechanics/earning-gold.md).

## Gameplay

The tile is split up into three sections, each showing a preview of a trail the player can buy.

From top to bottom do the trails increase in prize while also being larger in length and having more colors with the top having only one color and being the shortest and the bottom one having three colors and being the longest trail.

Once the game starts can each player use the [`!buy<number>` command][buy-command] where `<number>` is a number between 1 and 3, matching one of the displayed trails. If the player has enough gold to purchase the trail, will their marble be moved to the trail before moving towards the bottom center of the screen with the new trail applied. The sound of an old cash register is also played as an audible confirmation of the purchase.

The colors a trail can have are randomly chosen whenever the tile is being selected. Previously purchased trails can't be re-equipped again.

{{ game.history({
  'v0.12 Alpha': [
    'Minigame added'
  ],
  'v0.13 Alpha': [
    'King can complete purchases in shop tiles without leaving the throne'
  ]
}) }}