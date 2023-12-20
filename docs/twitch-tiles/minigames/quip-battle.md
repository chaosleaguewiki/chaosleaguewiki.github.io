---
description: Quip Battle is a minigame added in version v0.1 Alpha.
---

# Quip Battle

{{ game.info(
  inputs           = "Players: Messages<br>Viewers: Twitch-poll Votes",
  timer            = "1 minute",
  slots_guaranteed = "3",
  slots_raffle     = "2",
  added            = "v0.1 Alpha",
  
  img_url = "../../../assets/images/minigames/twitch/common/quip-battle.png"
) }}

**Quip Battle** is a minigame added in version v0.1 Alpha.

## Gameplay

The participating players are given a random question. They can send messages with their answer, which is displayed next to their marble. A new message overrides the previous one. At the same time, a poll is started in the twitch chat where the name of each participating player is given as an answer. The viewers of the stream can vote for the player whose answer they find the funniest.

After 60 seconds, the game ends and the players are ranked by the number of votes they got. The player with the most votes wins. It is possible for several players to get the same rank.

## Prompts

Below is a current list of all available prompts in the game.  

/// details | Click to open/close
    type: info

{% set json = read_json_file("docs/assets/quip_battle_prompts.json") %}
{% if json -%}
  <table>
    <thead>
      <tr>
        <th><small>Auto-generated from <a href="https://github.com/chaosleaguewiki/chaosleaguewiki.github.io/blob/main/docs/assets/quip_battle_prompts.json" target="_blank" rel="nofollow">quip_battle_prompts.json</a></small></th>
      </tr>
    </thead>
    <tbody>
      {% for entry in json %}
        <tr>
          <td>{{ entry }}</td>
        </tr>
      {% endfor %}
    </tbody>
  </table>
{%- else -%}
  No prompts available to display.
{%- endif %}
///

{{ game.history({
  'v0.1 Alpha': [
    'Minigame added'
  ],
  'v0.10 Alpha': [
    'Error handling and Timeout got added to not get stuck if reading the poll from API fails'
  ],
  'v0.11 Alpha': [
    'New battle prompts added',
    'Fixed TTS voice not being high-pitched'
  ],
  'v0.12 Alpha': [
    'Messages starting with `!` are no longer read by the TTS system'
  ],
  'v0.13 Alpha': [
    'Each vote is now worth 1/10th of the total win prize of the tile'
  ],
  'v0.14 Alpha': [
    'Prompts doubled, thanks to contributions by Maildropfolder'
  ],
  'v0.15 Alpha': [
    'Fixed typos in prompts'
  ],
  'v0.16 Alpha': [
    'Further typo corrections in prompts'
  ],
  'v0.20 Alpha': [
    'Minimum points earned from a vote is now 1 instead of 0'
  ],
  'v0.22 Alpha': [
    'Minigame can now appear in any rarity',
    'Vote values now scale with rarity and rebellion multiplier'
  ],
  'v0.26 Alpha': [
    'Emotes are no longer spoken by the TTS'
  ],
  'v0.27 Alpha': [
    'Added 29 new Prompts, courtesy of MailDropFolder.'
  ]
}) }}