{% macro info(title="", rarity="", inputs="", timer="", rounds="", slots_guaranteed="", slots_raffle="", added="", img_url="", img_alt="") -%}
  <div class="admonition wiki inline end">
    <p class="admonition-title">{{ title | d(env.page.title) }}</p>
    <table>
      <tbody>
        <tr>
          <td>Rarity</td>
          <td>{{ rarity | d('Unknown') }}</td>
        </tr>
        <tr>
          <td>Inputs</td>
          <td>{{ inputs | d('None') }}</td>
        </tr>
        <tr>
          <td>Timer</td>
          <td>{{ timer | d('None') }}</td>
        </tr>
        <tr>
          <td>Rounds</td>
          <td>{{ rounds | d('None') }}</td>
        </tr>
        <tr>
          <td>Slots</td>
          <td>Guaranteed: {{ slots_guaranteed | d('N/A') }}</td>
        </tr>
        <tr>
          <td>Raffle: {{ slots_raffle | d('N/A') }}</td>
        </tr>
        <tr>
          <td>Added</td>
          <td>{{ added | d('Unknown') }}</td>
        </tr>
      </tbody>
    </table>
  </div>
{%- endmacro %}