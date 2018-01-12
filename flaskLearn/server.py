from gevent import monkey
# Monkey patch to support coroutine
# Must be at the start of the whole app

monkey.patch_all()

import os
import sys
sys.path.insert(0, os.getcwd())
from flaskLearn.app import app
from gevent.wsgi import WSGIServer

http_server = WSGIServer(("", 5000), app)
http_server.serve_forever()
