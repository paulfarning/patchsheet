import os
import urllib
import logging
import collections

from google.appengine.api import users
from google.appengine.ext import ndb

from models.models import *

import jinja2
import webapp2

JINJA_ENVIRONMENT = jinja2.Environment(
  loader=jinja2.FileSystemLoader('views'),
  extensions=['jinja2.ext.autoescape'],
  autoescape=True)
JINJA_ENVIRONMENT.globals['OrderedDict'] = collections.OrderedDict


# [START main]
class Main(webapp2.RequestHandler):
  def get(self):
    patches = Patch.query().order(-Patch.created).fetch(10)
    synths = Synth.query().fetch()
    template_values = {
      'patches': patches,
      'synths': synths
    }
    template = JINJA_ENVIRONMENT.get_template('index.html')

    self.response.write(template.render(template_values))
# [END main]


# Init synths
# synth = Synth(id='minibrute')
# synth.author = users.get_current_user()
# synth.make = 'Arturia'
# synth.model = 'MiniBrute'
# key = synth.put()

# synth = Synth(id='juno-60')
# synth.author = users.get_current_user()
# synth.make = 'Roland'
# synth.model = 'Juno 60'
# key = synth.put()
