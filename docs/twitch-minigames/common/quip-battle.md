---
description: Quip Battle is a common minigame added in version v0.1 Alpha.
---

# Quip Battle

{{ game.info(
  inputs           = "Players: Messages<br>Viewers: Twitch-poll Votes",
  timer            = "1 Minute",
  slots_guaranteed = "3",
  slots_raffle     = "2",
  added            = "v0.1 Alpha",
  
  img_url = "../../../assets/images/minigames/twitch/quip-battle.png"
) }}

**Quip Battle** is a common minigame added in version v0.1 Alpha.

## Gameplay

The participating players are given a random question. They can send messages with their answer, which is displayed next to their marble. A new message overrides previous one. At the same time is a poll started in the twitch chat where the name of each participating player is given as an answer. The viewers of the stream can vote for the player whos answer they find the funniest.

After 60 seconds the game ends and the players are ranked by number of votes they got. The player with the most votes wins. It is possible for several players to get the same rank.

## Prompts

Below is a current list of all available prompts in the game.  

/// details | Click to open/close
    type: info

{% set json = read_json_file("docs/assets/extra_quips.json") %}
{% if json and json.prompts -%}
  <table>
    <thead>
      <tr>
        <th><small>Auto-generated from <a href="https://github.com/chaosleaguewiki/chaosleaguewiki.github.io/blob/main/docs/assets/extra_quips.json" target="_blank" rel="nofollow">extra_quips.json</a></small></th>
      </tr>
    </thead>
    <tbody>
      {% for entry in json.prompts %}
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

{{ game.history(
  versions = {
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
      'Messages starting with <code>!</code> are no longer read by the TTS system'
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
    ]
  }
) }}