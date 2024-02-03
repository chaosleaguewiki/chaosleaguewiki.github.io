---
description: Gold Tile is a game mechanic where a minigame or shop tile can spawn with a golden border, affecting the points you can earn or the gold you spent respectively.
---

# Gold Tile

{{ image.right(
    url = "../../assets/images/gold-tile.png",
    
    title = "Gold Tile"
) }}

**Gold Tile** is a game mechanic where a minigame or shop tile can spawn with a golden border, affecting the points you can earn or the gold you spent respectively.  
It has a 1% chance of appearing on any tile.

Gold Tiles are indicated by a yellow border with particles moving clockwise on it. Every ticket a player spents on this tile will be multiplied by a factor of 10, meaning a player spending 10 tickets will get 100 tickets spent.  
Additionally will any components in a tile that give or take points also increase by the same factor. This includes gaps/buckets, points earned by surviving a round of [Danger Zone] or [Zobm Says] or losing a round in those tiles.  
An exception to this rule are [Shop Tiles](../twitch-tiles/index.md#available-shop-tiles) where instead of increasing prices, a 25% discount is applied to all shop prices instead.

In case a [Rebellion Multiplier](rebellion.md) is active will its effect and the Gold Tile effect get added together, meaning a x5 rebellion in a gold tile will increase points earned by a factor of 15. This has no effect on Shop Tiles.

{{ game.history({
    'v0.13 Alpha': [
        'Game mechanic added'
    ]
}) }}
