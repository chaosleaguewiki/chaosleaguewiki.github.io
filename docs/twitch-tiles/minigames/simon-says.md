---
description: Simon Says, in the game displayed as Zobm Says, is a minigame tile where the king controls the game and chooses the order in which to eliminate the players.
---

# Simon Says

{{ game.info(
  inputs           = "King: `@mention` user",
  timer            = "60 Seconds",
  slots_guaranteed = "3",
  slots_raffle     = "2",
  added            = "v0.26 Alpha",
  
  img_url = "../../../assets/images/minigames/twitch/common/simon-says.png"
) }}

**Simon Says**, in the game displayed as **Zobm Says**, is a minigame tile where the king controls the game and chooses the order in which to eliminate the players.

## Gameplay

The players are moved into a tile similar in design to [Quip Battle tile].  
A countdown starts during which the current king can eliminate the players by mentioning them in chat.

Every time the king eliminates a player, a sound effect is played and all remaining players receive points.

The game is over when the countdown reaches zero or all but one player got eliminated.  
Players are ranked based on elimination order. Multiple players can win.

{{ game.history({
    'v0.26 Alpha': [
        'Minigame added'
    ]
}) }}