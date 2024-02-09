---
description: Recruiting is a game mechanic where a player can invite other players to the stream using a dedicated URL, which in return will make them earn gold from the invited players.
---

# Recruiting

**Recruiting** is a game mechanic where a player can invite other players to the stream using a dedicated URL, which in return will make them earn gold from the invited players.

## How to recruit

To recruit a player, one has to execute the [`!recruit`][recruit-command] command, which will give them a link to share with others.  
Any player who uses that link will be send to an authorization screen. There they can authorize the application using their currently logged in Twitch account. As a result will they be considered recruited by the game, which also gets announced by the game in the stream itself.

The recruiting player will earn 25% of any gold the recruited player earns in stream, excluding gold earned by [`!givegold`][givegold-command]. The recruited player will not lose any of their earned gold in the process.

## Requirements

In order for a player to be recruited, they need to not be active in the stream for a certain time. Additionally, they can only join one player.  
If they try joining another player while already being recruited or being considered active by the game, the recruiting will fail.

{{ game.history({
    'v0.1 Alpha': [
        'Gameplay mechanic added'
    ],
    'v0.34 Alpha': [
        'Recruited players now give 25% of any gold they earned. This does not include gold earned from a player using the [`!givegold`][givegold-command] command.'
    ]
}) }}