---
description: Bubble color Shop is an epic Shop tile, meaning instead of playing a game, you can purchase colored Speech bubbles using Gold you earned as king.
---

# Bubble Color Shop

{{ game.info(
  rarity           = ["epic"],
  inputs           = "[`!buy`][buy-command]",
  timer            = "29 Seconds",
  slots_guaranteed = "8",
  slots_raffle     = "4",
  added            = "v0.19 Alpha",
  
  img_url = "../../../assets/images/minigames/twitch/epic/bubble-color-shop.png"
) }}

**Bubble color Shop** is an epic Shop tile, meaning instead of playing a game, you can purchase colored speech bubbles using [Gold you earned as king](../../mechanics/earning-gold.md).

## Gameplay

The tile is split up into three sections, each showing a preview of a speech bubble the player can buy.

The prizes for each speech bubble is different, depending on some yet unknown factor.

Once the game starts can each player use the [`!buy<number>` command][buy-command] where `<number>` is a number between 1 and 3, matching one of the displayed speech bubbles. If the player has enough gold to purchase the speech bubble, will their marble be moved to the speech bubble before moving towards the bottom center of the screen with the new speech bubble applied. The sound of an old cash register is also played as an audible confirmation of the purchase.

The colors a speech bubble can have are randomly chosen whenever the tile is being selected. Previously purchased speech bubbles can't be re-equipped again.

{{ game.history({
  'v0.19 Alpha': [
    'Minigame added'
  ]
}) }}