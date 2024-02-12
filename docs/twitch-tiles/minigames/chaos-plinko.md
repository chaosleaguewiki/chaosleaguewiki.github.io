---
description: Chaos Plinko is a minigame added in v0.22 Alpha.
---

/// missing | Images missing
This wiki page lacks images of the different [tile rarities](#tile-rarities).
///

# Chaos Plinko

{{ game.info(
  slots_guaranteed = "8",
  slots_raffle     = "6",
  added            = "v0.22 Alpha",
  
  img_url = "../../../assets/images/minigames/twitch/common/chaos-plinko.png"
) }}

**Chaos Plinko** is a minigame added in v0.22 Alpha.

## Gameplay

The tile consists of various obstacles and circles, also referred to as pegs, with point values. The player marbles are dropped into the tile where they earn points by hitting the circles.  
A death bubble is also dropped into the tile. Should a player marble collide with it, they will be eliminated.

For every 10 seconds survived, the pegs double their value. In addition, an additional death bubble will get spawned for every 3rd doubling of points.

The game is over once only a single player remains. Players are listed by their survival time.

## Images

### Tile rarities

/// warning |
This section requires images for rare and legendary rarity of this tile.
///

![common](../../assets/images/minigames/twitch/common/chaos-plinko.png "Common rarity version"){ loading="lazy" style="max-width: 20%;" }
![epic](../../assets/images/minigames/twitch/epic/chaos-plinko.png){ loading="lazy" style="max-width: 20%;" }

<!--
![rare](../../assets/images/minigames/twitch/rare/chaos-plinko.png "Rare rarity verion"){ loading="lazy" style="max-width: 25%;" }
-->
<!--
![legendary](../../assets/images/minigames/twitch/legendary/chaos-plinko.png){ loading="lazy" style="max-width: 25%;" }
-->

{{ game.history({
    'v0.22 Alpha': [
        'Minigame added'
    ],
    'v0.30 Alpha': [
      'Fix bug causing pegs to reset to 5 points.'
    ]
}) }}