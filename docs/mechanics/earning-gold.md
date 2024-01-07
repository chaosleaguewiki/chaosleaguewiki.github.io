---
description: Players can earn gold, a virtual currency of the game, while being king.
---

# Earning Gold

{{ image.right(
    url = "../../assets/images/earning-gold.png",
    
    title   = "Earning Gold",
    caption = "Image depicting the current king earning gold"
) }}

Players can earn gold, a virtual currency of the game, while being king.  
This earned gold can then be used on [Shop tiles](../twitch-tiles/index.md#available-shop-tiles) to receive cosmetics in return.

## How to obtain Gold

To earn gold, a player has to [capture the throne](attacking-the-king.md). Once they capture the throne will they receive gold every 5 minutes while being king.

The gold earned is increased every time a new tile is selected, with the tile's rarity determening the number of gold to add to the chest.

Another way to earn gold is by other players using the [`!givegold` command][givegold-command] to give some or all of their gold to another player.

{{ game.history({
    'v0.8 Alpha': [
        'Gameplay mechanic added'
    ],
    'v0.25 Alpha': [
        'Travel indicator for gold changed from a number to individual coins'
    ],
    'v0.28 Alpha': [
        'Gold now increases for every selected tile and value increases based on the tile\'s rarity',
        'King now only earns gold every 5 minutes'
    ]
}) }}
