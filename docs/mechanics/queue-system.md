---
description: A queue system is used in Chaos League to determine who may participate in a minigame.
---

# Queue System

A queue system is used in Chaos League to determine who may participate in a [minigame](../twitch-minigames/index.md).

## How it works

Each tile has a set of guaranteed and raffle slots. The number of guaranteed and raffle slots depends on the game itself, but can range from 3 guaranteed and 2 ruffle up to 8 for each.

### Guaranteed Slots

Guaranteed slots are displayed on the side of the tile as a green circle. The `n` players who have spent the most amount of spawn tickets will be added to these slots.  
As the name suggests are players shown in these slots guaranteed to participate in the game, unless someone else bids more tickets, in which case the players will be moved down according to the new player's position in the queue.

### Raffle Slots

Raffle slots are shown as green dots over the box with the text "Raffle". Unlike guaranteed slots do raffle slots not display the players that would currently be selected.  
Every player who spents spawn tickets, but not enough to be in a guaranteed slot, will be added to the raffle. Once the queue timer reaches zero will `n` players be randomly selected from the raffle pool, with a bias towards players who have spent more spawn tickets on the tile.

{{ game.history({
    'v0.1 Alpha': [
        'Gameplay mechanic added'
    ]
}) }}