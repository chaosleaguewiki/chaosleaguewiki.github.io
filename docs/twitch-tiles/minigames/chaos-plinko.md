---
description: Chaos Plinko is a minigame added in v0.22 Alpha.
---

# Chaos Plinko

{{ game.info(
  rarity           = ["common", "rare", "epic", "legendary"],
  slots_guaranteed = "8",
  slots_raffle     = "6",
  added            = "v0.22 Alpha"
) }}

**Chaos Plinko** is a minigame added in v0.22 Alpha.

## Gameplay

The tile consists of various obstacles and circles, also referred to as pegs, with point values. The player marbles are droped into the tile where they earn points by hitting the circles.  
A death bubble is also dropped into the tile. Should a player marble collide with it, they will be eliminated.

For every 10 seconds survived, the pegs double their value. In addition will an additional death bubble get spawned for every 3rd doubling of points.

The game is over once only a single player remains. Players are listed by their survival time.

{{ game.history({
    'v0.22 Alpha': [
        'Minigame added'
    ]
}) }}