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
    patches = Patch.query().order(-Patch.created).fetch(10)
    synths = Synth.query().fetch()

    if len(synths) == 0:
      synth = Synth(id='minibrute')
      synth.author = users.get_current_user().user_id()
      synth.make = 'Arturia'
      synth.model = 'MiniBrute'
      key = synth.put()

      synth = Synth(id='juno-60')
      synth.author = users.get_current_user().user_id()
      synth.make = 'Roland'
      synth.model = 'Juno 6/60'
      key = synth.put()

    template_values = {
      'patches': patches,
      'synths': synths
    }
    template = JINJA_ENVIRONMENT.get_template('admin.html')

    self.response.write(template.render(template_values))
# [END main]
