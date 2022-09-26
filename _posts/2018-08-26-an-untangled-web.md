---
title: "A Tangled Web, Slightly Untangled"
excerpt_separator: "<!--more-->"
categories:
  - Miscellaneous tricks
tags:
  - web
  - jekyll
  - github
---
I finally updated my website to the 21st century, and decided to go full Computer Scientist on it.
I was looking for something that was full-featured ([markdown](https://daringfireball.net/projects/markdown/), [math](https://www.mathjax.org/)), 
methodical to update ([git](https://git-scm.com/)), and customizable ([layout](https://www.w3schools.com/), [fonts](https://fonts.google.com/)).
<!--more-->

Having rewritten the [RSS 2017](http://rss2017.lids.mit.edu/) website from scratch (later enhanced by the incomparable [Brian Hou](http://brianhou.com/)), I developed a fondness for [Jekyll](https://jekyllrb.com/) as my base engine. Infinitely flexible, Jekyll empowered us to generate the _entire_ [proceedings](http://rss2017.lids.mit.edu/program/detailed/) by piping data from [CMT](https://cmt3.research.microsoft.com/) seamlessly. 

I'm a big fan of [Edward Tufte's](https://www.edwardtufte.com/) work, especially his advice to _[maximize data-ink](https://en.wikipedia.org/wiki/Edward_Tufte)_, so the [Tufte Jekyll theme](https://en.wikipedia.org/wiki/Edward_Tufte) was a natural layout choice.

I hosted the site source code in a private GitHub repo. Now there were several ways to push the _built_ site out to the world. I considered writing a _[git post-receive hook]((https://git-scm.com/book/en/v2/Customizing-Git-Git-Hooks))_ to pipe the site content to the UW CSE web server (works quite well for our [lab website](https://personalrobotics.cs.washington.edu/)), but finally decided on something much simpler: [point](https://help.github.com/articles/adding-a-remote/) my public [GitHub pages](https://pages.github.com/) repository to the built site (remember to add an empty `.nojekyll` file), and let GitHub automatically build and host the site.

Then, I setup a _[301 redirect](https://en.wikipedia.org/wiki/HTTP_301)_ from my UW CSE site to my GitHub pages public site. Now I had a stable and working pipeline. Finally, I decided to [buy a domain](https://goodrobot.ai/) on [NameCheap](https://www.namecheap.com/), and secured it via SSL certificates from [CloudFlare](https://www.cloudflare.com/ssl/). 	