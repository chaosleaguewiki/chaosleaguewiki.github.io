---
description: Royal Execution is a a rare minigame added in version v0.8 Alpha.
---

# Royal Execution

{{ game.info(
  rarity           = ["rare"],
  inputs           = "King&#58; [`!left`][left-command], [`!right`][right-command]",
  timer            = "30 Seconds",
  rounds           = "1-3",
  slots_guaranteed = "6",
  slots_raffle     = "2",
  added            = "v0.8 Alpha",
  
  img_url = "../../../assets/images/minigames/twitch/royal-execution.png"
) }}

**Royal Execution** is a a rare minigame added in version v0.8 Alpha.

## Gameplay

The tile consists of 2 chambers separated vertically and a segregator below the entrance, splitting the participating players' marbles evenly between the two chambers.

Above one of the chambers there is a spiked platform. For 20 seconds, the king gains the ability to move the platform between the chambers using the [`!left`][left-command] and [`!right`][right-command] commands. When the timer is up, the platform is dropped, the marbles underneath transfer 4 points to the king's balance and are eliminated from the game.

When there's one marble left, the game ends and the players are ranked by their elimination order. The longest surviving player wins. It is possible for several players to get the same rank, however, only one person can win.

## Trivia

- It is actually possible to die to the spikes when exiting the forking pipe, if your marble happens to have the right velocity.

{{ game.history({
  'v0.8 Alpha': [
    'Minigame added'
  ],
  'v0.9 Alpha': [
    'Timer increased to 30 seconds'
  ],
  'v0.14 Alpha': [
    'Fixed Bug causing commands from king to not be registered'
  ]
}) }}