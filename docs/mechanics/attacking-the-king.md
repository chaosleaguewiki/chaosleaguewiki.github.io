---
description: A core mechanic (And the main goal) of Chaos League is to attack the king and capture the throne.
---

# Attacking the King

/// wiki | Attacking the King
    attrs: {class: 'inline end'}

![attack](../assets/images/throne.png)
///

A core mechanic (and the main goal) of Chaos League is to attack the king and capture the throne.

To attack the king, a player has to use the [`!attack` command][attack-command]. This will spawn the Player's marble at the red pipe with the `!attack` text on it.  
The marble will move up towards the current king. During their move, they will encounter a wall of ore blocks. Each block has a base value corresponding to their type; dirt has 2, coal has 4, iron has 8 and diamond has 16.

The obsidian blocks vary in their values, as their base value is increased by 1/20 of the king's own points, while the king loses half of their points on capturing the throne.  
In addition, any player (including the king) can use the [`!defend [amount]` command][defend-command] to spread `[amount]` of their points across the 10 obsidian blocks (the value distributed is divided by 10, so `!defend 100` gives 10 points to each obsidian block).

Each block the player's marble touches will decrease in value while also decreasing the player's score at the same rate. If the player's score reaches 0 before they capture the throne, they will be eliminated.  
Broken blocks remain broken until a player has captured the throne, at which point the wall will be regenerated.

If the throne is captured within 60 seconds of the last capture, the blocks' base values will double from the previous round. Otherwise, they will be halved (unless dirt has 2 points, in which case they remain the same).

{{ game.history({
    'v0.1 Alpha': [
        'Gameplay mechanic added'
    ]
}) }}