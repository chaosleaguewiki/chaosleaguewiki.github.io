---
description: Predictions are a game mechanic using Twitch's prediction system.
---

# Predictions

**Predictions** are a game mechanic using Twitch's prediction system.

## How it works

The game will create a Prediction using Twitch's Prediction system.  
Every viewer can participate on the prediction by spending at least 10 channel points on either `Yes` or `No` on whether the given prediction will happen or not.

Each prediction has a timeframe in which it has to happen, or else `No` will be the result of it. Should the event happen within the given timeframe will `Yes` be the result.

Once a prediction is either happening or not will the total amount of channel points spent by the losers of the prediction be distributed equally towards the winners of the prediction.

## List of Predictions

Below is a list of all Predictions currently available. Each has an equal chance to be selected.

/// details | Click to open/close
    type: info

{% set json = read_json_file("docs/assets/predictions.json") %}
{% if json -%}
  <table>
    <thead>
      <tr>
        <th colspan="2"><small>Auto-generated from <a href="https://github.com/chaosleaguewiki/chaosleaguewiki.github.io/blob/main/docs/assets/predictions.json" target="_blank" rel="nofollow">predictions.json</a></small></th>
      </tr>
      <tr>
        <th>Prediction:</th>
        <th>Yes when:</th>
      </tr>
    </thead>
    <tbody>
      {% for prompt, yes_cause in json.items() %}
        <tr>
          <td>{{ prompt }}</td>
          <td>{{ yes_cause }}
        </tr>
      {% endfor %}
    </tbody>
  </table>
{%- else -%}
  No prompts available to display.
{%- endif %}
///