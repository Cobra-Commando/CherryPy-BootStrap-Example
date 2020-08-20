# CherryPy-Bootstrap-Example
Proof of concept static HTML5 website via Python that generates a random 8-digit hexadecimal value.

# Requirements
+ Runtime environment used: Ubuntu 20.04 LTS via WSL 2.0
+ Python 3.8 with CherryPy via "pip install cherrypy"
+ Run code via "python hex.py", open localhost:8080

# Why NOT to deploy this on Heroku
- Heroku defaults to gunicorn/django in place of cherrypy
- Sparse documentation on running alternative web servers
- Heroku is optimized for dynamic websites (e.g. Node.js)
