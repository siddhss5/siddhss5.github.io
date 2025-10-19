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
{% if site.data.mentoring.current.postdocs.size > 0 %}
### Current Postdocs

| Name | Started | Current Position |
|------|---------|------------------|
{% for postdoc in site.data.mentoring.current.postdocs %}| {{ postdoc.Name }} | {{ postdoc.Start }} | {{ postdoc.NowAt }} |
{% endfor %}
{% endif %}

{% if site.data.mentoring.current.phd_students.size > 0 %}
### Current PhD Students

| Name | Co-advisor | Thesis | Started |
|------|------------|--------|---------|
{% for student in site.data.mentoring.current.phd_students %}| {{ student.Name }} | {{ student.Coadvisor }} | {{ student.Title }} | {{ student.Start }} |
{% endfor %}
{% endif %}

{% if site.data.mentoring.current.ms_students.size > 0 %}
### Current MS Students

| Name | Co-advisor | Thesis | Started |
|------|------------|--------|---------|
{% for student in site.data.mentoring.current.ms_students %}| {{ student.Name }} | {{ student.Coadvisor }} | {{ student.Title }} | {{ student.Start }} |
{% endfor %}
{% endif %}

## Alumni

{% if site.data.mentoring.alumni.postdocs.size > 0 %}
### Alumni Postdocs

| Name | Period | Current Position |
|------|--------|------------------|
{% for postdoc in site.data.mentoring.alumni.postdocs %}| {{ postdoc.Name }} | {{ postdoc.Start }}-{{ postdoc.Finish }} | {{ postdoc.NowAt }} |
{% endfor %}
{% endif %}

{% if site.data.mentoring.alumni.phd_students.size > 0 %}
### Alumni PhD Students

| Name | Co-advisor | Thesis | Period | Current Position |
|------|------------|--------|--------|------------------|
{% for student in site.data.mentoring.alumni.phd_students %}| {{ student.Name }} | {{ student.Coadvisor }} | {{ student.Title }} | {{ student.Start }}-{{ student.Finish }} | {{ student.NowAt }} |
{% endfor %}
{% endif %}

{% if site.data.mentoring.alumni.ms_students.size > 0 %}
### Alumni MS Students

| Name | Co-advisor | Thesis | Period | Current Position |
|------|------------|--------|--------|------------------|
{% for student in site.data.mentoring.alumni.ms_students %}| {{ student.Name }} | {{ student.Coadvisor }} | {{ student.Title }} | {{ student.Start }}-{{ student.Finish }} | {{ student.NowAt }} |
{% endfor %}
{% endif %}
    
