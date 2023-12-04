---
description: Bubble Color Shop is a planned special tile in that it is not a minigame in the usual sense, but a shop players can buy differently colored speech bubbles from using their earned Gold.
---

# Bubble Color Shop

--8<-- "unreleased.md"

{{ game.info(
  rarity = "epic",
  inputs = "[`!buy`][buy-command]",
  timer  = "Unknown",
  slots_guaranteed = "8",
  slots_raffle     = "4",
  added            = "v0.19 Alpha",
  
  img_url = "../../../assets/images/minigames/twitch/speech-bubble-shop.png"
) }}

**Bubble Color Shop** is a planned special tile in that it is not a minigame in the usual sense, but a shop players can buy differently colored speech bubbles from using their earned Gold.

## Gameplay

The tile is split up into three sections, each showing a preview of a speech bubble the player can buy.

The prizes for each speech bubble is different, depending on some yet unknown factor.

Once the game starts can each player use the [`!buy<number>` command][buy-command] where `<number>` is a number between 1 and 3, matching one of the displayed speech bubbles. If the player has enough gold to purchase the speech bubble, will their marble be moved to the trail before moving towards the bottom center of the screen with the new speech bubble applied.

The colors a speech bubble can have are randomly chosen whenever the tile is being selected. Previously purchased speech bubbles can't be re-equipped again.

{{ game.history({
  'v0.19 Alpha': [
    'Minigame added'
  ]
}) }}