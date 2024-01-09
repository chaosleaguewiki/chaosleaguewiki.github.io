---
description: Crown Shop is an epic Shop tile added in v0.29 Alpha, where players can buy a different crown for their marble when being king, using the gold they earned.

status: new
---

# Crown Shop

{{ game.info(
  rarity           = ["epic"],
  inputs           = "[`!buy`][buy-command]",
  timer            = "29 seconds",
  slots_guaranteed = "8",
  slots_raffle     = "4",
  added            = "v0.29 Alpha"
) }}

**Bubble Color Shop** is an epic Shop tile added in v0.29 Alpha, where players can buy a different crown for their marble when being king, using the [gold they earned](../../mechanics/attacking-the-king.md).

## Gameplay

The tile is split up into three sections, each showing a preview of a crown the player can buy.

Each crown is a different tier, with the first one only having a different color, the second one having a different color and different trim color and the third one having a different color, different trim color and gems.  
The prices for each crown becomes more expensive the more complex it is.

Once the game starts, each player can use the [`!buy<number>` command][buy-command] where `<number>` is a number between 1 and 3, matching one of the displayed crowns. If the player has enough gold to purchase the crown, their marble will be moved to the crown before moving towards the bottom center of the screen with the new crown applied. The sound of an old cash register is also played as an audible confirmation of the purchase.

The colors a crown, its trims and gems can have are randomly chosen whenever the tile is being selected. Previously purchased crowns can't be re-equipped again.

{{ game.history({
  'v0.29 Alpha': [
    'Minigame added'
  ]
}) }}