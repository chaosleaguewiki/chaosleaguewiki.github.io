---
description: Explanation of the Water and Lava Bucket feature.
---

# Water and Lava Bucket

A mechanic in the game is the Water and Lava Bucket. They can be activated either by using bits to fill up a progress bar, or by buying the respective item using tickets.

## How to fill the buckets

In order to fill the buckets, one has to use the `!lava [bits]` or `!water [bits]` chat command for filling the progress bar of the lava or water bucket respectively. `[bits]` needs to replaced by the amount of bits you want to spend, using the `cheer<bits>` format.  
As an example, `!lava cheer100` will fill the progress bar for the lava bucket by 100 bits.

The Lava bucket needs 750 bits while the Water Bucket only requires 500 bits to be filled.  
Once either is filled, they will be activated in the attack tile.

Players can also purchase a Lava or Water bucket directly through tickets, which fills it up completely and activates them.

Activating the lava bucket causes lava to be spread across the attack tile. Every Player Marble hitting the lava will be eliminated and lose half their points. The lava will disappear slowly over time, or can be removed directly using the Water bucket.  
Activating said water bucket will spread water across the attack tile, removing any lava it touches, while being destroyed itself.

## Trivia

- Water drops can't hurt a player's marble, but they can slow it down.
- Lava and Water Buckets have existed in a previous iteration of Chaos league.
- It was possible for lava to eliminate players who exited the raffle queue, causing a hard lock for the game/shop tile starting.

{{ game.history({
    'v0.9 Alpha': [
        'Gameplay mechanic added'
    ],
    'v0.10 Alpha': [
        'Option to buy a Bucket through tickets added',
        'SFW added for filling Lava or Water progress bar',
        'Announcement added for releasing Lava or Water Bucket',
        'Price for Lava Bucket changed from 1000 Bits to 750 Bits'
    ],
    'v0.25 Alpha': [
        'Player marbles now sink into water to aid in attacking'
    ],
    'v0.26 Alpha': [
        'Fixed bug causing lava to kill players exiting raffle slot'
    ]
}) }}