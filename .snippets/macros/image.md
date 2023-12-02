{% macro right(url, title="", alt="image", caption="") %}
  {% if caption -%}
    <div class="admonition wiki inline end">
      {% if title -%}<p class="admonition-title">{{ title }}</p>{%- endif %}
      <p>
        <figure>
          <img alt="{{ alt }}" src="{{ url }}" loading="lazy">
          <figcaption>{{ caption | e }}</figcaption>
        </figure>
      </p>
    </div>
  {%- else -%}
    <div class="admonition wiki inline end">
      {% if title %}<p class="admonition-title">{{ title }}</p>{% endif %}
      <p>
        <img alt="{{ alt }}" src="{{ url }}" loading="lazy">
      </p>
    </div>
  {%- endif %}
{% endmacro %}

{% macro left(url, title="", alt="image", caption="") %}
  {% if caption -%}
    <div class="admonition wiki inline">
      {% if title -%}<p class="admonition-title">{{ title }}</p>{%- endif %}
      <p>
        <figure>
          <img alt="{{ alt }}" src="{{ url }}" loading="lazy">
          <figcaption>{{ caption | e }}</figcaption>
        </figure>
      </p>
    </div>
  {%- else -%}
    <div class="admonition wiki inline">
      {% if title %}<p class="admonition-title">{{ title }}</p>{% endif %}
      <p>
        <img alt="{{ alt }}" src="{{ url }}" loading="lazy">
      </p>
    </div>
  {%- endif %}
{% endmacro %}

{% macro img(url, alt="image", caption="") %}
  {% if caption -%}
    <figure>
      <img alt="{{ alt }}" src="{{ url }}" loading="lazy">
      <figcaption>{{ caption | e }}</figcaption>
    </figure>
  {%- else -%}
    <img alt="{{ alt }}" src="{{ url }}" loading="lazy">
  {%- endif %}
{% endmacro %}