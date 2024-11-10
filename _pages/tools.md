---
layout: archive
title: "Tools"
permalink: /tools/
author_profile: true
---
<div class="tools-page">
  {% include tool_card.html 
    tool_class="fame" 
    tool_name="FaMe" 
    tool_description="is a BPMN-driven framework for multi-robot system development. It facilitates the definition of robotic missions using BPMN collaborations, while leveraging the ROS2 framework for system execution."
    tool_code_url="https://github.com/SaraPettinari/fame"
    tool_docs_url="https://pros.unicam.it/fame/"
    tool_id="fame" 
  %}
  
  {% include tool_card.html 
    tool_class="tale" 
    tool_name="TALE" 
    tool_description="integrates the tag-based multi-perspective methodology. It helps robotic developers automatically extract multi-perspective event logs from robotic system executions and analyze them through process mining."
    tool_code_url="https://github.com/SaraPettinari/tale"
    tool_docs_url="https://pros.unicam.it/tale/"
    tool_id="tale" 
  %}

  {% include tool_card.html 
    tool_class="soup" 
    tool_name="Soup" 
    tool_description="is a WebApp designed for end users to create Event Knowledge Graphs (EKGs). Starting with an event log in a .csv file, users are guided through the creation of the EKG for object-centric process mining analysis."
    tool_code_url="https://bitbucket.org/proslabteam/soup/src/master/"
    tool_docs_url="https://pros.unicam.it/soup/"
    tool_id="soup" 
  %}
</div>
