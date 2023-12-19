---
description: Points multiplier is a mechanic where the points earned in a tile will be multiplied by 2 every 10 seconds.
---

# Points Multiplier

**Points multiplier** is a mechanic where the points earned in a tile will be multiplied by 2 every 10 seconds.

## How it works

Certain tiles will display a circle with a x2 text displayed on it. Once the game starts, an outline will slowly increase around the circle. Once it has completed a full revolution, purple x2 texts will fly towards components in a tile that can give or take points.  
Depending on the tile played, either all or only a selection of components will have their values doubled.

The outline will appear in two colors: Yellow and red.  
Yellow indicates a simple multiplication of point values, while red indicates that alongside the multiplication, a [death ball](death-ball.md) will be spawned right underneath it.  
Depending on the tile, this can happen every 3rd multiplication or even every multiplication after an initial 3 iterations.

## Trivia

- The point multiplication cannot go past a value of 2,147,483,647 which is the total number a 32-bit integer can reach (which is used here). This has been discovered in the v0.25 Alpha stream, the longest so far for Chaos League, where the [Chaos Plinko] tile got stuck in active game state, causing the multiplier to increase the points constantly.

{{ game.history({
    'v0.22 Alpha': [
        'Game mechanic introduced in [Chaos Plinko]'
    ],
    'v0.24 Alpha': [
        'Multiplier added to additional tiles'
    ]
}) }}