# hIPPYlib / web

This repo contains the [MkDocs](http://mkdocs.org) source files of the hIPPYlib website.

## Prerequisites

* Install [MkDocs](http://mkdocs.org)
    sudo pip install mkdocs

* Install [bootstrap](http://getbootstrap.com/) and [bootswatch](https://bootswatch.com/) themes
    sudo pip install mkdocs-bootstrap
    sudo pip install mkdocs-bootswatch
    
* Install [MathJax](https://www.mathjax.org/) support using [python-markdown-math](https://github.com/mitya57/python-markdown-math)
    sudo pip install python-markdown-math


## To make changes to the website

* Clone this repository
    git clone https://github.com/hippylib/hippylib.github.io.git
* Edit or add some `.md` files in the src folder (you may also need to update the `mkdocs.yml` config); 
* Preview locally
    mkdocs serve
* Publish on GitHub
    mkdocs gh-deploy