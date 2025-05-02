---
permalink: /
title: "About Me"
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

## Welcome!

I'm Sara, a Postdoctoral Researcher in Computer Science at the Gran Sasso Science Institute. 
Alongside my academic work, I’m passionate about **photography**, **traveling**, and **baking**. 

Feel free to explore my website to learn more about my research or contact me at
<i class="fas fa-envelope"></i> [sara.pettinari@gssi.it](mailto:sara.pettinari@gssi.it)!


## 🗞️ News
<div>
  {% assign sorted_news = site.news | sort: 'date' | reverse | slice: 0, 3 %}
  {% for news in sorted_news %}
    {% assign formatted_date = news.date | date: "%Y-%m-%d" %}
    {% include news_entry.html
      date=formatted_date
      event=news.event
      description=news.description
      website=news.website
      linkedin=news.linkedin
    %}
  {% endfor %}
</div>





## 📍 Places

Here’s a map showing some of the places I’ve visited for research around the world.

<iframe src="../assets/maps/visited_places_map.html" width="100%" height="600"></iframe>

