# test.py
# this file means to test following stack of components works or not
# ====> the web client <-> uWSGI <-> Python
# Run command at the same directory :
#     uwsgi --http :8000 --wsgi-file test_uwsgi.py
#
# if that above works good, then test 
# ====>the web client <-> uWSGI <-> Django
# Go to project root, run
#     uwsgi --http :8000 --module project.wsgi
# To check, browse example.com:8000

def application(env, start_response):
    start_response('200 OK', [('Content-Type','text/html')])
    return "Hello World"
