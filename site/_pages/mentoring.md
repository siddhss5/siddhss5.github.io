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

{% assign people = site.data.people %}
{% assign current_postdocs = people | where: "role", "postdoc" | where: "status", "current" %}
{% assign current_phd = people | where: "role", "phd_student" | where: "status", "current" %}
{% assign current_ms = people | where: "role", "ms_student" | where: "status", "current" %}
{% assign alumni_postdocs = people | where: "role", "postdoc" | where: "status", "alumni" | sort: "end_year" | reverse %}
{% assign alumni_phd = people | where: "role", "phd_student" | where: "status", "alumni" | sort: "end_year" | reverse %}
{% assign alumni_ms = people | where: "role", "ms_student" | where: "status", "alumni" | sort: "end_year" | reverse %}

{% if current_postdocs.size > 0 %}
### Current Postdocs

| Name | Started | Current Position |
|------|---------|------------------|
{% for person in current_postdocs %}| {{ person.name }} | {{ person.start_year }} | {{ person.current_position | default: "" }} |
{% endfor %}
{% endif %}

{% if current_phd.size > 0 %}
### Current PhD Students

| Name | Co-advisor | Thesis | Started |
|------|------------|--------|---------|
{% for person in current_phd %}| {{ person.name }} | {{ person.co_advisor | default: "" }} | {{ person.thesis_title | default: "" }} | {{ person.start_year }} |
{% endfor %}
{% endif %}

{% if current_ms.size > 0 %}
### Current MS Students

| Name | Co-advisor | Thesis | Started |
|------|------------|--------|---------|
{% for person in current_ms %}| {{ person.name }} | {{ person.co_advisor | default: "" }} | {{ person.thesis_title | default: "" }} | {{ person.start_year }} |
{% endfor %}
{% endif %}

## Alumni

{% if alumni_postdocs.size > 0 %}
### Alumni Postdocs

| Name | Period | Current Position |
|------|--------|------------------|
{% for person in alumni_postdocs %}| {{ person.name }} | {{ person.start_year }}-{{ person.end_year }} | {{ person.current_position | default: "" }} |
{% endfor %}
{% endif %}

{% if alumni_phd.size > 0 %}
### Alumni PhD Students

| Name | Co-advisor | Thesis | Period | Current Position |
|------|------------|--------|--------|------------------|
{% for person in alumni_phd %}| {{ person.name }} | {{ person.co_advisor | default: "" }} | {{ person.thesis_title | default: "" }} | {{ person.start_year }}-{{ person.end_year }} | {{ person.current_position | default: "" }} |
{% endfor %}
{% endif %}

{% if alumni_ms.size > 0 %}
### Alumni MS Students

| Name | Co-advisor | Thesis | Period | Current Position |
|------|------------|--------|--------|------------------|
{% for person in alumni_ms %}| {{ person.name }} | {{ person.co_advisor | default: "" }} | {{ person.thesis_title | default: "" }} | {{ person.start_year }}-{{ person.end_year }} | {{ person.current_position | default: "" }} |
{% endfor %}
{% endif %}
