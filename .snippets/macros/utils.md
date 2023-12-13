{% macro table(entries=[]) %}
  {% if entries -%}
    <table>
      <tbody>
        {% set loop_ns = namespace(last_key=false) %}
        {% for key, values in entries.items() %}
          <tr class="no-color">
            {% if loop.last %}
              {% set loop_ns.last_key = true %}
              <td rowspan="{{ values | length() }}" class="draw_line--right no-line--top">{{ key }}</td>
            {% else %}
              <td rowspan="{{ values | length() }}" class="draw_line--right draw_line--down no-line--top">{{ key}}</td>
            {% endif %}
            {% for value in values %}
              {% if not loop.first %}
                </tr>
                <tr class="no-color">
              {% endif %}
              {% if loop.last and loop_ns.last_key %}
                <td class="no-line--top">{{ value | markdownify }}</td>
              {% else %}
                <td class="draw_line--down no-line--top">{{ value | markdownify }}</td>
              {% endif %}
            {% endfor %}
          </tr>
        {% endfor %}
      </tbody>
    </table>
  {%- endif %}
{% endmacro %}