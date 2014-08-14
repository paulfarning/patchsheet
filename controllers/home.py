import os
import urllib
import logging

from google.appengine.api import users
from google.appengine.ext import ndb

from models.models import *

from config import JINJA_ENVIRONMENT


# [START main]
class Main(webapp2.RequestHandler):
  def get(self):
    patches = Patch.query(projection=[Patch.name]).order(-Patch.created).fetch(10)
    synths = Synth.query().fetch()
    template_values = {
      'patches': patches,
      'synths': synths
    }
    template = JINJA_ENVIRONMENT.get_template('index.html')

    self.response.write(template.render(template_values))
# [END main]
