{% import 'image.md' as image with context %}

{% macro info(title=page.title, rarity=["common", "rare", "epic", "legendary"], inputs="None", timer="None", rounds="None", slots_guaranteed="N/A", slots_raffle="N/A", added="Unknown", img_url=None, img_alt=page.title, img_caption="") -%}
  <div class="admonition wiki inline end">
    <p class="admonition-title">{{ title | d(page.title) }}</p>
    <table>
      <tbody>
        <tr>
          <td class="draw_line--down">Rarity</td>
          <td class="draw_line--down">
            {% for r in rarity %}
              {{ chance(r|lower()) or (r|capitalize()) }}
              {% if loop.revindex > 1 %}<br>{% endif %}
            {% else %}
              Unknown
            {% endfor %}
          </td>
        </tr>
        <tr>
          <td class="draw_line--down">Inputs</td>
          <td class="draw_line--down">{{ inputs | markdownify }}</td>
        </tr>
        <tr>
          <td class="draw_line--down">Timer</td>
          <td class="draw_line--down">{{ timer }}</td>
        </tr>
        <tr>
          <td class="draw_line--down">Rounds</td>
          <td class="draw_line--down">{{ rounds }}</td>
        </tr>
        <tr>
          <td class="draw_line--down" rowspan="2">Slots</td>
          <td>Guaranteed: {{ slots_guaranteed }}</td>
        </tr>
        <tr>
          <td class="draw_line--down">Raffle: {{ slots_raffle }}</td>
        </tr>
        <tr>
          <td class="{{ 'draw_line--down' if img_url else '' }}">Added</td>
          <td class="{{ 'draw_line--down' if img_url else '' }}">{{ added | markdownify }}</td>
        </tr>
      </tbody>
    </table>
    {% if img_url %}
      <p>
        {{ image.img(url=img_url, alt=img_alt, caption=img_caption) }}
      </p>
    {% endif %}
  </div>
{%- endmacro %}

{% macro history(versions=[]) -%}
  {% if versions -%}
  <hr>
  
  <div class="admonition wiki history">
    <p class="admonition-title">History</p>
    <table>
      <tbody>
        {% set loop_ns = namespace(last_key=false) %}
        {% for version, entries in versions.items() %}
          <tr>
            {% if loop.last %}
              {% set loop_ns.last_key = true %}
              <td rowspan="{{ entries | length() }}" class="game_version draw_line--right">{{ version }}</td>
            {% else %}
              <td rowspan="{{ entries | length() }}" class="game_version draw_line--down draw_line--right">{{ version }}</td>
            {% endif %}
            {% for entry in entries %}
              {% if not loop.first %}
                </tr>
                <tr>
              {% endif %}
              {% if loop.last and loop_ns.last_key %}
                <td>{{ entry | markdownify }}</td>
              {% else %}
                <td class="draw_line--down">{{ entry | markdownify }}</td>
              {% endif %}
            {% endfor %}
          </tr>
        {% endfor %}
      </tbody>
    </table>
  </div>
  {%- endif %}
{%- endmacro %}

{% macro yt_version(link) -%}
  {% if link -%}
    <div class="variant_info twitch">
      {{ "You are viewing the :simple-twitch: **Twitch** version of this Minigame." | markdownify }}<br>
      {{ ("[Switch to :simple-youtube: **YouTube** version.](/youtube-minigames/" ~ link ~ ")") | markdownify }}
    </div>
  {%- else -%}
    <div class="admonition failure">
      <p class="admonition-title">ERROR: Invalid argument 'link'</p>
      <p>The provided argument <code>link</code> was either empty or not set!</p>
    </div>
  {%- endif %}
{%- endmacro %}

{% macro twitch_version(link) -%}
  {% if link -%}
    <div class="variant_info youtube">
      {{ "You are viewing the :simple-youtube: **YouTuve** version of this Minigame" | markdownify }}<br>
      {{ ("[Switch to :simple-twitch: **Twitch** version.](/twitch-tiles/" ~ link ~ ")") | markdownify }}
    </div>
  {%- else -%}
    <div class="admonition failure">
      <p class="admonition-title">ERROR: Invalid argument 'link'</p>
      <p>The provided argument <code>link</code> was either empty or not set!</p>
    </div>
  {%- endif %}
{%- endmacro %}

{% macro chance(key) %}{{ {
  "common": "<abbr title='69% chance'>Common</abbr>",
  "rare": "<abbr title='25% chance'>Rare</abbr>",
  "epic": "<abbr title='5% chance'>Epic</abbr>",
  "legendary": "<abbr title='1% chance'>Legendary</abbr>"
}[key] }}{% endmacro %}