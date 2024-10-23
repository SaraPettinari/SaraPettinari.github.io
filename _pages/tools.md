---
layout: archive
title: "Tools"
permalink: /tools/
author_profile: true
---

{% include base_path %}

---

## FaMe

**FaMe** is a BPMN-driven framework for multi-robot system development. It facilitates the definition of robotic missions using BPMN collaborations, while leveraging the ROS2 framework for system execution.

<p align="center">
  <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/code.svg" width="20" height="20"> <a href="https://github.com/SaraPettinari/fame">Code</a>
  &nbsp;|&nbsp;
  <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/circle-info.svg" width="20" height="20"> <a href="https://pros.unicam.it/fame/">Documentation</a>
</p>

### Related Publications

{% for pub in site.publications %}
  {% if pub.tool == "fame" %}
    - **{{ pub.title }}**  
      _{{ pub.venue }}, {{ pub.date | date: "%Y" }}_  
      [View Paper]({{ pub.paperurl }})
  {% endif %}
{% endfor %}



---

## TALE

**TALE** is a tool that integrates the tag-based multi-perspective methodology. It helps robotic developers automatically extract multi-perspective event logs from robotic system executions and analyze them through process mining. The analysis can be visualized from both behavioral and spatial perspectives.

<p align="center">
  <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/code.svg" width="20" height="20"> <a href="https://github.com/SaraPettinari/tale">Code</a>
  &nbsp;|&nbsp;
  <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/circle-info.svg" width="20" height="20"> <a href="https://pros.unicam.it/tale/">Documentation</a>
</p>

### Related Publications

<p>
{% for pub in site.publications %}
  {% if pub.tool == "tale" %}
    - **{{ pub.title }}**  
      _{{ pub.venue }}, {{ pub.date | date: "%Y" }}_  
      [View Paper]({{ pub.paperurl }})
  {% endif %}
{% endfor %}
</p>


---

## Soup

**Soup** is a WebApp designed for end users to create Event Knowledge Graphs (EKGs). Starting with an event log in a .csv file, users are guided through the creation of the EKG, which can be used for object-centric process mining analysis.

<p align="center">
  <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/code.svg" width="20" height="20"> <a href="https://bitbucket.org/proslabteam/soup/src/master/">Code</a>
  &nbsp;|&nbsp;
  <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/circle-info.svg" width="20" height="20"> <a href="https://pros.unicam.it/soup/">Documentation</a>
</p>

### Related Publications

{% for pub in site.publications %}
  {% if pub.tool == "soup" %}
    - **{{ pub.title }}**  
      _{{ pub.venue }}, {{ pub.date | date: "%Y" }}_  
      [View Paper]({{ pub.paperurl }})
  {% endif %}
{% endfor %}
