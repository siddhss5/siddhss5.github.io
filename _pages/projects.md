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
  {% assign project = project_data[1] %}

<div id="{{ project_name }}" class="project-section" style="margin-top: 2em;">
<h2 style="display: inline; margin-bottom: 0; border-bottom: none;">{{ project.title }}</h2>
  {% if project.status %}
    {% if project.status == "active" %}
<span class="btn btn--success btn--small" style="margin-left: 0.5em;">{{ project.status | capitalize }}</span>
    {% else %}
<span class="btn btn--secondary btn--small" style="margin-left: 0.5em;">{{ project.status | capitalize }}</span>
    {% endif %}
  {% endif %}
  {% if project.website and project.website != "" %}
<a href="{{ project.website }}" target="_blank" class="btn btn--primary btn--small" style="margin-left: 0.5em;">Website</a>
  {% endif %}
<span class="btn btn--info btn--small" style="margin-left: 0.5em;">{{ project_name }}</span>

  {% if project.description %}
<p>{{ project.description }}</p>
  {% endif %}

  {% if project.publications.size > 0 %}

<details style="margin-top: 1em;">
  <summary style="cursor: pointer; font-weight: bold; font-size: 1.1em; padding: 0.5em 0;">
    Publications ({{ project.publications.size }})
  </summary>
  
  <div style="margin-top: 1em;">
    {% for pub in project.publications %}
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

