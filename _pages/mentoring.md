---
title: "Mentoring"
permalink: /mentoring/
layout: single
classes: wide
header:
  overlay_image: /assets/images/sidd-teaching.jpg
  overlay_filter: 0.5
---
{% if site.data.mentoring.current.postdocs.size > 0 %}
### Current Postdocs

{% for postdoc in site.data.mentoring.current.postdocs %}
- **{{ postdoc.Name }}**{% if postdoc.Coadvisor %} (co-advised with {{ postdoc.Coadvisor }}){% endif %}
  - Started: {{ postdoc.Start }}
  - Current position: {{ postdoc.NowAt }}
{% endfor %}
{% endif %}

{% if site.data.mentoring.current.phd_students.size > 0 %}
### Current PhD Students

{% for student in site.data.mentoring.current.phd_students %}
- **{{ student.Name }}**{% if student.Coadvisor %} (co-advised with {{ student.Coadvisor }}){% endif %}
  - Thesis: "{{ student.Title }}"
  - Started: {{ student.Start }}
  - Expected completion: {{ student.Finish }}
  - Current position: {{ student.NowAt }}
{% endfor %}
{% endif %}

{% if site.data.mentoring.current.ms_students.size > 0 %}
### Current MS Students

{% for student in site.data.mentoring.current.ms_students %}
- **{{ student.Name }}**{% if student.Coadvisor %} (co-advised with {{ student.Coadvisor }}){% endif %}
  - Thesis: "{{ student.Title }}"
  - Started: {{ student.Start }}
  - Expected completion: {{ student.Finish }}
  - Current position: {{ student.NowAt }}
{% endfor %}
{% endif %}

## Alumni

{% if site.data.mentoring.alumni.postdocs.size > 0 %}
### Alumni Postdocs

{% for postdoc in site.data.mentoring.alumni.postdocs %}
- **{{ postdoc.Name }}**{% if postdoc.Coadvisor %} (co-advised with {{ postdoc.Coadvisor }}){% endif %}
  - Period: {{ postdoc.Start }}-{{ postdoc.Finish }}
  - Current position: {{ postdoc.NowAt }}
{% endfor %}
{% endif %}

{% if site.data.mentoring.alumni.phd_students.size > 0 %}
### Alumni PhD Students

{% for student in site.data.mentoring.alumni.phd_students %}
- **{{ student.Name }}**{% if student.Coadvisor %} (co-advised with {{ student.Coadvisor }}){% endif %}
  - Thesis: "{{ student.Title }}"
  - Period: {{ student.Start }}-{{ student.Finish }}
  - Current position: {{ student.NowAt }}
{% endfor %}
{% endif %}

{% if site.data.mentoring.alumni.ms_students.size > 0 %}
### Alumni MS Students

{% for student in site.data.mentoring.alumni.ms_students %}
- **{{ student.Name }}**{% if student.Coadvisor %} (co-advised with {{ student.Coadvisor }}){% endif %}
  - Thesis: "{{ student.Title }}"
  - Period: {{ student.Start }}-{{ student.Finish }}
  - Current position: {{ student.NowAt }}
{% endfor %}
{% endif %}

## Mentoring Philosophy

I believe in fostering an environment where students can grow both academically and personally. My approach to mentoring focuses on:

- **Independent Research**: Encouraging students to develop their own research directions
- **Collaborative Learning**: Promoting teamwork and knowledge sharing
- **Real-world Impact**: Connecting research to practical applications
- **Career Development**: Supporting students in their professional growth

## Statistics

- **Total Students Mentored**: {{ site.data.mentoring.current.postdocs.size | plus: site.data.mentoring.current.phd_students.size | plus: site.data.mentoring.current.ms_students.size | plus: site.data.mentoring.alumni.postdocs.size | plus: site.data.mentoring.alumni.phd_students.size | plus: site.data.mentoring.alumni.ms_students.size }}
- **Current Students**: {{ site.data.mentoring.current.postdocs.size | plus: site.data.mentoring.current.phd_students.size | plus: site.data.mentoring.current.ms_students.size }}
- **Alumni**: {{ site.data.mentoring.alumni.postdocs.size | plus: site.data.mentoring.alumni.phd_students.size | plus: site.data.mentoring.alumni.ms_students.size }}
- **PhD Students**: {{ site.data.mentoring.current.phd_students.size | plus: site.data.mentoring.alumni.phd_students.size }}
- **MS Students**: {{ site.data.mentoring.current.ms_students.size | plus: site.data.mentoring.alumni.ms_students.size }}
- **Postdocs**: {{ site.data.mentoring.current.postdocs.size | plus: site.data.mentoring.alumni.postdocs.size }}
