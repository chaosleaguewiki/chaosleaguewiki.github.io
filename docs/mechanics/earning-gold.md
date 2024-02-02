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

Gold can be earned through 3 ways: Being the King, breaking gold ore blocks or receiving gold through the [`!givegold`][givegold-command] command.

### Being the King

At the right-hand side of the king is a circle displaying a open treasure chest. The circle is filling up over the span of 5 minutes. Once the timer reaches zero will all accumulated gold be given to the current king.  
The chest fills up with gold for each tile that has been selected, with the starting win prize of the tile being used as the gold to add.

### Breaking Gold ore blocks

Gold ore blocks are randomly spread across the defense wall of the King. When a gold ore block is broken will its point value be given as gold to whoever broke the block itself.  
Gold ore blocks can have a maximum value of 256 points, meaning you can at most earn 256 gold from one block.

### `!givegold` command

Players can use the [`!givegold`][givegold-command] command to give some of their Gold to other players.

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
    ],
    'v0.30 Alpha': [
        'Gold ore blocks added to the wall, which when broken will give the player who broke it gold'
    ],
    'v0.31 Alpha': [
        'Gold ore blocks now can\'t go beyond 256 in value'
    ]
}) }}
