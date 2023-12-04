{% import 'image.md' as image with context %}

{% macro info(title=page.title, rarity="Common", inputs="None", timer="None", rounds="None", slots_guaranteed="N/A", slots_raffle="N/A", added="Unknown", img_url=None, img_alt=page.title, img_caption="") -%}
  <div class="admonition wiki inline end">
    <p class="admonition-title">{{ title | d(page.title) }}</p>
    <table>
      <tbody>
        <tr>
          <td class="draw_line--down">Rarity</td>
          <td class="draw_line--down">{{ rarity | d('Unknown') | capitalize() }}</td>
        </tr>
        <tr>
          <td class="draw_line--down">Inputs</td>
          <td class="draw_line--down">{{ markdownify(inputs) }}</td>
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
          <td class="{{ 'draw_line--down' if img_url else '' }}">{{ markdownify(added) }}</td>
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
                <td>{{ markdownify(entry) }}</td>
              {% else %}
                <td class="draw_line--down">{{ markdownify(entry) }}</td>
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
    {{ alternative_version(link, type="twitch", alt="youtube") }}
  {%- endif %}
{%- endmacro %}

{% macro twitch_version(link) -%}
  {% if link -%}
    {{ alternative_version(link, type="youtube", alt="twitch") }}
  {%- endif %}
{%- endmacro %}

{% macro alternative_version(link, type, alt) -%}
  <div class="variant_info {{ type }}">
    {{ markdownify("You are viewing the :simple-" ~ type|lower() ~ ": **" ~ type|capitalize() ~ "** version of this Minigame.<br>[Switch to :simple-" ~ alt|lower() ~ ": **" ~ alt|capitalize() ~ "** version.](/" ~ alt|lower() ~ "-minigames/" ~ link ~ ")") }}
  </div>
{%- endmacro %}