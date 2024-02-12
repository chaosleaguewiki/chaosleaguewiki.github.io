---
description: Forked Frenzy is a minigame added in v0.16 Alpha.
---

/// missing | Images missing
This wiki page lacks images of the different [tile rarities](#tile-rarities).
///

# Forked Frenzy

{{ game.info(
  slots_guaranteed = "8",
  slots_raffle     = "3",
  added            = "v0.16 Alpha",
  
  img_url = "../../../assets/images/minigames/twitch/common/forked-frenzy.png"
) }}

**Forked Frenzy** is a minigame added in v0.16 Alpha.

## Gameplay

The tile is split up into multiple sets of forking pipes, 1 at the top, 2 in the middle and 2 at the bottom. The player marbles are dropped into the first pipe at the top where they will be split up equally towards the left and right.

Players ending up on the left side will enter another forking pipe where they will be split up again. If they exit the pipe to the left, they will end up in a closed gap, transferring 5 points to the king while also being eliminated. Exiting the pipe on the right side will result in them passing through a gap giving them points while also falling into the next forking pipe.  
The right side is the same, but mirrored, meaning players on the right get eliminated while players on the left move on.

The final set of pipes drops the player's marble through a gap, giving them points no matter what side they exit from. Once the marble reaches the bottom, they will reappear at the top, repeating the circle.

## Images

### Tile rarities

/// warning |
This section requires images for rare, epic and legendary rarity of this tile.
///

![common](../../assets/images/minigames/twitch/common/forked-frenzy.png "Common rarity version"){ loading="lazy" style="max-width: 20%;" }
<!-- No images yet.
![rare](../../assets/images/minigames/twitch/rare/forked-frenzy.png "Rare rarity verion"){ loading="lazy" style="max-width: 20%;" }
![epic](../../assets/images/minigames/twitch/epic/forked-frenzy.png "Epic rarity version"){ loading="lazy" style="max-width: 20%;" }
![legendary](../../assets/images/minigames/twitch/legendary/forked-frenzy.png "Legendary rarity version"){ loading="lazy" style="max-width: 20%;" }
-->

{{ game.history({
  'v0.16 Alpha': [
    'Minigame added'
  ],
  'v0.22 Alpha': [
    'Minigame can now appear in any rarity'
  ],
  'v0.26 Alpha': [
    'Game now waits for all players to be eliminated before switching to podium'
  ]
}) }}