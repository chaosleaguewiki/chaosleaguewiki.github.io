---
description: Text Color Shop is an epic Shop tile added in v0.19 Alpha, where players can buy a different color for their message text, using the gold they earned.
---

# Text Color Shop

{{ game.info(
  rarity           = ["epic"],
  inputs           = "[`!buy`][buy-command]",
  timer            = "29 seconds",
  slots_guaranteed = "8",
  slots_raffle     = "4",
  added            = "v0.19 Alpha",
  
  img_url = "../../../assets/images/minigames/twitch/epic/text-color-shop.png"
) }}

**Text Color Shop** is an epic Shop tile added in v0.19 Alpha, where players can buy a different color for their message text, using the [gold they earned](../../mechanics/attacking-the-king.md).

## Gameplay

The tile is split up into three sections, each showing a preview of a speech bubble with a colored text the player can buy.

The prices for each text color are different, depending on some yet unknown factor.

Once the game starts, each player can use the [`!buy<number>` command][buy-command] where `<number>` is a number between 1 and 3, matching one of the displayed text colors. If the player has enough gold to purchase the text color, their marble will be moved to the text color before moving towards the bottom center of the screen with the new text color applied. The sound of an old cash register is also played as an audible confirmation of the purchase.

The colors a text color can have are randomly chosen whenever the tile is being selected. Previously purchased text colors can't be re-equipped again.

{{ game.history({
  'v0.19 Alpha': [
    'Minigame added'
  ]
}) }}