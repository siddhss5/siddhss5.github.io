---
title: "CV"
permalink: /cv/
layout: single
classes: wide
header:
  overlay_image: /assets/images/HERB-pose.jpg
---
Here is my [CV](/assets/SiddharthaSrinivasaCV.pdf).


## Short Bio for Seminars
Siddhartha Srinivasa is a Professor at The Paul G. Allen School of Computer Science & Engineering at the University of Washington, and an IEEE Fellow. He is a full-stack roboticist, with the goal of enabling robots to perform complex manipulation tasks under uncertainty and clutter, with and around people. To this end, he founded the Personal Robotics Lab in 2005. He is a PI on the Quality of Life Technologies NSF ERC, RCTA, DARPA ARM-S, DARPA Robotics Challenge, and DARPA RACER, and has built several robots (HERB, ADA, CHIMP, MuSHR), and has written software frameworks (OpenRAVE, DART) and best-paper award winning algorithms (CBiRRT, CHOMP, BIT*, Legibility, LazySP) used extensively by roboticists around the world. Sidd received a B.Tech in Mechanical Engineering from the Indian Institute of Technology Madras in 1999, and a PhD in 2005 from the Robotics Institute at Carnegie Mellon University. He played badminton and tennis for IIT Madras, captained the CMU squash team, ran long-distance competitively, and lately plays tennis.

## Awards

| Year(s)   |Award           | Paper  |
|----------:|:---------------|:-------|
{% for award in site.data.awards %}|{{ award.year }}|{{ award.award }}|{% if award.pub_title %}[{{ award.pub_title }}]({{ award.pub_link }}){% endif %}|
{% endfor %}

