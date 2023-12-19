---
description: Zobm Says is a minigame tile where the king controls the game and chooses the order in which to eliminate the players.
---

# Zobm Says

{{ game.info(
  inputs           = "King: `@mention` user",
  timer            = "60 Seconds",
  slots_guaranteed = "3",
  slots_raffle     = "2",
  added            = "v0.26 Alpha",
  
  img_url = "../../../assets/images/minigames/twitch/common/zobm-says.png"
) }}

**Zobm Says** is a minigame tile where the king controls the game and chooses the order in which to eliminate the players.

## Gameplay

The players are moved into a tile similar in design to [Quip Battle].  
A countdown starts during which the current king can eliminate the players by mentioning them in chat.

Every time the king eliminates a player, a sound effect is played and all remaining players receive points. In addition is the reward for surviving a round doubled.

The game is over when the countdown reaches zero or all but one player got eliminated.  
Players are ranked based on elimination order, with first eliminated being lowest. Multiple players can win.

## Trivia

- The name is a reference to the stream participant Mr_Zobm, who is known for gifting hundreds of twitch subscriptions and spending a lot of bits, most of them for spawning lava.

{{ game.history({
    'v0.26 Alpha': [
        'Minigame added'
    ]
}) }}