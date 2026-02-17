---
title: "Projects"
permalink: /projects/
layout: single
classes: wide
header:
  overlay_image: /assets/images/tycho-lego.jpeg
---

{% assign projects = site.data.lab.projects %}
{% assign pubs = site.data.lab.publications %}

{% for project in projects %}
<div id="{{ project.id }}" class="project-section" style="margin-top: 2.5em;">

<h2 style="display: inline; margin-right: 0.5em;">{{ project.title }}</h2>
{% if project.status == "active" %}
  {% if project.website and project.website != "" %}
    <a href="{{ project.website }}" target="_blank" class="btn btn--success btn--small">Active</a>
  {% else %}
    <span class="btn btn--success btn--small">Active</span>
  {% endif %}
{% else %}
  <span class="btn btn--secondary btn--small">{{ project.status | capitalize }}</span>
{% endif %}
{% if project.website and project.website != "" %}
<a href="{{ project.website }}" target="_blank" class="btn btn--primary btn--small">Website</a>
{% endif %}
<a href="{{ site.baseurl }}/projects/#{{ project.id }}" class="btn btn--info btn--small">{{ project.id }}</a>

{% if project.description %}
<p style="margin-top: 0.8em;">{{ project.description }}</p>
{% endif %}

{% if project.publication_ids.size > 0 %}
<details style="margin-top: 1em;">
<summary style="cursor: pointer; font-weight: bold; font-size: 1.1em; padding: 0.5em 0;">
  Publications ({{ project.publication_ids.size }})
</summary>

<div style="margin-top: 1em;">
{% for pub_id in project.publication_ids %}
  {% assign pub = pubs | where: "bib_id", pub_id | first %}
  {% if pub %}
<div class="publication-entry" style="margin-bottom: 1.2em; padding-left: 0.5em;">

  <div class="publication-title" style="margin-bottom: 0.2em;">
    {% if pub.pdf_url %}
      <a href="{{ pub.pdf_url }}">{{ pub.title }}</a>
    {% else %}
      {{ pub.title }}
    {% endif %}
  </div>

  <div class="publication-meta" style="font-size: 0.9em; color: #666;">
    {% if pub.authors %}
      {% for author in pub.authors %}{{ author.name }}{% unless forloop.last %}, {% endunless %}{% endfor %}
    {% endif %}
    {% if pub.venue %} — {{ pub.venue | markdownify | remove: "<p>" | remove: "</p>" }}{% endif %}
    {% if pub.note %}
    <br><strong>{{ pub.note | markdownify | remove: "<p>" | remove: "</p>" }}</strong>
    {% endif %}
  </div>

</div>
  {% endif %}
{% endfor %}
</div>
</details>
{% endif %}

</div>
{% endfor %}
