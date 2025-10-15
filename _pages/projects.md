---
title: "Projects"
permalink: /projects/
layout: single
classes: wide
header:
  overlay_image: /assets/images/tycho-lego.jpeg
---

{% for project_data in site.data.projects %}
  {% assign project_name = project_data[0] %}
  {% assign project_pubs = project_data[1] %}
  {% assign project_config = site.data.projects-config[project_name] %}

<div id="{{ project_name }}" class="project-section" style="margin-top: 2em;">
<h2 style="display: inline; margin-bottom: 0; border-bottom: none;">{{ project_config.title }}</h2>
  {% if project_config.status %}
    {% if project_config.status == "active" %}
<span class="btn btn--success btn--small" style="margin-left: 0.5em;">{{ project_config.status | capitalize }}</span>
    {% else %}
<span class="btn btn--secondary btn--small" style="margin-left: 0.5em;">{{ project_config.status | capitalize }}</span>
    {% endif %}
  {% endif %}
  {% if project_config.website and project_config.website != "" %}
<a href="{{ project_config.website }}" target="_blank" class="btn btn--primary btn--small" style="margin-left: 0.5em;">Website</a>
  {% endif %}
<span class="btn btn--info btn--small" style="margin-left: 0.5em;">{{ project_name }}</span>

  {% if project_config.description %}
<p>{{ project_config.description }}</p>
  {% endif %}

  {% if project_pubs.publications.size > 0 %}

<details style="margin-top: 1em;">
  <summary style="cursor: pointer; font-weight: bold; font-size: 1.1em; padding: 0.5em 0;">
    Publications ({{ project_pubs.publications.size }})
  </summary>

  <div style="margin-top: 1em;">
    {% for pub in project_pubs.publications %}
    <div class="publication-entry" style="margin-bottom: 1.2em; padding-left: 0.5em;">

      <div class="publication-title" style="margin-bottom: 0.2em;">
        {% if pub.pdf_url %}
      <a href="{{ pub.pdf_url }}">{{ pub.title }}</a>
        {% else %}
      {{ pub.title }}
        {% endif %}
      </div>

      <div class="publication-meta" style="font-size: 0.9em; color: #666;">
        {{ pub.authors }} — {{ pub.venue }}
        {% if pub.note %}
        <br><strong>{{ pub.note }}</strong>
        {% endif %}
      </div>

    </div>
    {% endfor %}
  </div>
</details>

  {% endif %}

</div>

{% endfor %}

