---
title: "Mentoring"
permalink: /mentoring/
layout: single
classes: wide
header:
  overlay_image: /assets/images/sidd-teaching.jpg
  overlay_filter: 0.5
---

![PRL Team 2024](/assets/images/PRL-2024.jpg)

{% comment %}One row per role each person held, earlier roles included (scripts/sync_config.py writes it). Alumni are every status but current. Each cell escapes "|", which would otherwise end the cell.{% endcomment %}
{% assign people = site.data.mentoring %}
{% assign current_postdocs = people | where: "role", "postdoc" | where: "status", "current" %}
{% assign current_phd = people | where: "role", "phd_student" | where: "status", "current" %}
{% assign current_ms = people | where: "role", "ms_student" | where: "status", "current" %}
{% assign alumni_postdocs = people | where: "role", "postdoc" | where_exp: "p", "p.status != 'current'" | sort: "end_year" | reverse %}
{% assign alumni_phd = people | where: "role", "phd_student" | where_exp: "p", "p.status != 'current'" | sort: "end_year" | reverse %}
{% assign alumni_ms = people | where: "role", "ms_student" | where_exp: "p", "p.status != 'current'" | sort: "end_year" | reverse %}

{% if current_postdocs.size > 0 %}
### Current Postdocs

| Name | Started | Current Position |
|------|---------|------------------|
{% for person in current_postdocs %}| {{ person.name | replace: "|", "\|" }} | {{ person.start_year | replace: "|", "\|" }} | {{ person.current_position | replace: "|", "\|" }} |
{% endfor %}
{% endif %}

{% if current_phd.size > 0 %}
### Current PhD Students

| Name | Co-advisor | Thesis | Started |
|------|------------|--------|---------|
{% for person in current_phd %}| {{ person.name | replace: "|", "\|" }} | {{ person.co_advisor | replace: "|", "\|" }} | {{ person.thesis_title | replace: "|", "\|" }} | {{ person.start_year | replace: "|", "\|" }} |
{% endfor %}
{% endif %}

{% if current_ms.size > 0 %}
### Current MS Students

| Name | Co-advisor | Thesis | Started |
|------|------------|--------|---------|
{% for person in current_ms %}| {{ person.name | replace: "|", "\|" }} | {{ person.co_advisor | replace: "|", "\|" }} | {{ person.thesis_title | replace: "|", "\|" }} | {{ person.start_year | replace: "|", "\|" }} |
{% endfor %}
{% endif %}

## Alumni

{% if alumni_postdocs.size > 0 %}
### Alumni Postdocs

| Name | Period | Current Position |
|------|--------|------------------|
{% for person in alumni_postdocs %}| {{ person.name | replace: "|", "\|" }} | {{ person.start_year | replace: "|", "\|" }}-{{ person.end_year | replace: "|", "\|" }} | {{ person.current_position | replace: "|", "\|" }} |
{% endfor %}
{% endif %}

{% if alumni_phd.size > 0 %}
### Alumni PhD Students

| Name | Co-advisor | Thesis | Period | Current Position |
|------|------------|--------|--------|------------------|
{% for person in alumni_phd %}| {{ person.name | replace: "|", "\|" }} | {{ person.co_advisor | replace: "|", "\|" }} | {{ person.thesis_title | replace: "|", "\|" }} | {{ person.start_year | replace: "|", "\|" }}-{{ person.end_year | replace: "|", "\|" }} | {{ person.current_position | replace: "|", "\|" }} |
{% endfor %}
{% endif %}

{% if alumni_ms.size > 0 %}
### Alumni MS Students

| Name | Co-advisor | Thesis | Period | Current Position |
|------|------------|--------|--------|------------------|
{% for person in alumni_ms %}| {{ person.name | replace: "|", "\|" }} | {{ person.co_advisor | replace: "|", "\|" }} | {{ person.thesis_title | replace: "|", "\|" }} | {{ person.start_year | replace: "|", "\|" }}-{{ person.end_year | replace: "|", "\|" }} | {{ person.current_position | replace: "|", "\|" }} |
{% endfor %}
{% endif %}
