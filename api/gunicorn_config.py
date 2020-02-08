from os import environ

# import multiprocessing

PORT = int(environ.get("PORT", 8080))
DEBUG_MODE = int(environ.get("DEBUG_MODE", 1))

# Gunicorn config
bind = ":" + str(PORT)


"""
It turns out that multiprocessing cannot tell how many 
CPUs are inside Docker containers 
nor on Heroku Dynos (which are shared instances I think)

Gunicorn acknowledges this...
https://github.com/benoitc/gunicorn/issues/2028

Python.org says yup that is a bug...
https://bugs.python.org/issue36054


Heroku suggests 2-3 workers...
https://devcenter.heroku.com/articles/optimizing-dyno-usage#python

https://devcenter.heroku.com/articles/python-gunicorn#adding-gunicorn-to-your-application


Funnily enough, the code deployed on heroku runs just fine 
and the "R14 memory quota exceeded" error 
really just behaves like a warning.
I am unsure of possible security/memory leak bugs.

Anyway. Let's go with the Heroku recommendation.
"""
# workers = multiprocessing.cpu_count() * 2 + 1

workers = 3
