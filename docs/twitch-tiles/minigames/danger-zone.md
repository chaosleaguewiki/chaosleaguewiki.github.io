---
description: Danger Zone is a minigame added in version v0.1 Alpha.
---

# Danger Zone

{{ game.info(
  inputs           = "`@mention` user",
  timer            = "20 seconds",
  rounds           = "3",
  slots_guaranteed = "8",
  slots_raffle     = "4",
  added            = "v0.1 Alpha",
  
  img_url = "../../../assets/images/minigames/twitch/common/danger-zone.png"
) }}

**Danger Zone** is a minigame added in version v0.1 Alpha.

## Gameplay

The tile consists of 6 chambers.

At the beginning of each round, the participating players' marbles are distributed evenly between the chambers. For 20 seconds, the players gain the ability to pull other players' marbles to their marble by `@mention` them. It is possible for a marble to be pulled by several other marbles at once.

When the timer is up, the pulls are executed for 4 seconds. Marbles in the green chamber are safe and Marbles in the red chamber are eliminated. In the remaining chambers, a needle is spinned. If it points at the red area, the marbles are eliminated, otherwise they are safe.  
Every marble that survives a round will earn points and the reward gets doubled for the next round.

When there are no marbles or one marble left, or after 3 rounds, the game ends and the players are ranked by their elimination order. The longest surviving player wins. It is possible for several players to get the same rank.

{{ game.history({
  'v0.1 Alpha': [
    'Minigame added'
  ],
  'v0.13 Alpha': [
    'Additional points are rewarded for players surviving a round'
  ],
  'v0.14 Alpha': [
    'Round number resets now after it rolls up again'
  ],
  'v0.17 Alpha': [
    'Surviving a round now equals 1 instead of 0'
  ],
  'v0.20 Alpha': [
    '[`!pull`][pull-command] command removed. You can now just mention a user to pull them',
    'Fixed arrow going off-screen'
  ],
  'v0.22 Alpha': [
    'Minigame can now appear in any rarity',
    'Round survival bonus now scales with rarity and rebellion bonus',
    'Round survival bonuses double with each round'
  ]
}) }}
