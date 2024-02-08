---
description: Points multiplier is a mechanic where the points earned in a tile will be multiplied by 2 every certain time interval.
---

# Points Multiplier

**Points multiplier** is a mechanic where the points earned in a tile will be multiplied by 2 every 10 seconds.

## How it works

Tiles can display a circle displaying a x2 on the top-left corner. This circle will have an outline slowly filling up. Whenever the outline makes one full rotation, purple x2 text will fly towards specific components of the tile, multiplying their displayed point values by a factor of 2 each time.

The outline can have 2 specific colors displayed: Yellow and Red.  
Yellow indicates that the points will be multiplied, while red also spawns a [death ball](death-ball.md) on top of multiplying the points.

The time it takes for the outline to make one full resolution is 10 seconds, with the exception of [Combo Breaker], where it takes 4 minutes to complete.

## Trivia

- The point multiplication cannot go past a value of 2,147,483,647 which is the total number a 32-bit integer can reach (which is used here). This has been discovered in the v0.25 Alpha stream, the longest running stream of Chaos League at that time, when a bug caused a player marble to be eliminated in queue, resulting in a softlock and the multiplier constantly multiplying the existing point values.

{{ game.history({
    'v0.22 Alpha': [
        'Game mechanic introduced in [Chaos Plinko]'
    ],
    'v0.24 Alpha': [
        'Multiplier added to additional tiles'
    ]
}) }}