---
description: A queue system is used in Chaos League to determine who may participate in a tile.
---

# Queue System

A queue system is used in Chaos League to determine who may participate in a [tile](../twitch-tiles/index.md).

## How it works

Each tile has a set of guaranteed and raffle slots. The number of guaranteed and raffle slots depends on the tile itself, but can range from 3 guaranteed and 2 ruffle up to 8 for each.

### Guaranteed Slots

Guaranteed slots are displayed on the side of the tile as a green circle. Players who have spent the most tickets on the tile will be listed on these slots in descending order of tickets spent.  
As the name suggests, players displayed in these slots are guaranteed to participate in the tile.

### Raffle Slots

Raffle slots are shown as green dots over the box with the text "Raffle". Unlike guaranteed slots, raffle slots do not display the players that would currently be selected.  
Every player who spent spawn tickets, but not enough to be in a guaranteed slot, will be added to the raffle. Once the queue timer reaches zero, a set of players equal to the number of raffle slots will be randomly selected, with a bias towards those who have spent more tickets on the tile itself.

If fewer players are in the raffle than the available slots, then all players will be added to the tile.

{{ game.history({
    'v0.1 Alpha': [
        'Gameplay mechanic added'
    ]
}) }}