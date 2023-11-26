---
description: Quip Battle is a common minigame added in version v0.1 Alpha.
history:
  'v0.1 Alpha':
    - Minigame added
  'v0.10 Alpha':
    - Error handling and Timeout got added to not get stuck if reading the poll from API fails
  'v0.11 Alpha':
    - New battle prompts added
    - Fixed TTS voice not being high-pitched
  'v0.12 Alpha':
    - Messages starting with <code>!</code> are no longer read by the TTS system
  'v0.13 Alpha':
    - Each vote is now worth 1/10th of the total win prize of the tile
---

# Quip Battle

/// wiki | Quip Battle
    attrs: {class: 'inline end'}

|         |                    |
|---------|--------------------|
| Rarity: | Common             |
| Input:  | Messages           |
|         | Twitch-poll voting |
| Timer:  | 1 Minute           |
| Rounds: | None               |
| Slots:  | Guaranteed: 3      |
|         | Raffle: 2          |
| Added:  | v0.1 Alpha         |

![quip-battle](../../assets/images/minigames/twitch/quip-battle.png)
///

**Quip Battle** is a common minigame added in version v0.1 Alpha.

## Gameplay

The participating players are given a random question. They can send messages with their answer, which is displayed next to their marble. A new message overrides previous one. At the same time is a poll started in the twitch chat where the name of each participating player is given as an answer. The viewers of the stream can vote for the player whos answer they find the funniest.

After 60 seconds the game ends and the players are ranked by number of votes they got. The player with the most votes wins. It is possible for several players to get the same rank.
