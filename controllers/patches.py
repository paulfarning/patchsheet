import os
import urllib
import logging
import json
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


def synth_key(synth):
  """Constructs a Datastore key for a Synth entity with synth."""
  return ndb.Key('Synth', synth)


# [START main]
class Main(webapp2.RequestHandler):
  def get(self):
    self.redirect('/')
# [END main]


# [START create]
class Create(webapp2.RequestHandler):
  def get(self, synth_id='_select'):
    synths = Synth.query().fetch()
    template_values = {
      'disabled': 'false',
      'synths': synths,
      'synth_id': synth_id
    }
    template = JINJA_ENVIRONMENT.get_template('/synths/%s.html' % synth_id)

    self.response.write(template.render(template_values))

  def post(self):

    synth = self.request.get('patch-synth')
    patch = Patch(parent=synth_key(synth))
    model = globals()[SynthModelMap[synth]]

    if users.get_current_user():
      patch.author = users.get_current_user()

    patch.name = self.request.get('patch-name')

    for param in model.params_int:
      setattr(patch, param, int(self.request.get(param.replace('_', '-'))))

    for param in model.params_bool:
      setattr(patch, param, True if self.request.get(param.replace('_', '-')) else False)

    for param in model.params_string:
      setattr(patch, param, self.request.get(param.replace('_', '-')))

    patch_key = patch.put()
    patch_id = patch_key.id()

    self.redirect('/patches/%s/%s' % (synth, patch_id))
# [END create]


# [START view]
class View(webapp2.RequestHandler):
  def get(self, synth_id, patch_id):
    key_parent = ndb.Key('Synth', synth_id)
    patch = Patch.get_by_id(int(patch_id), key_parent)
    template_values = {
      'disabled': 'true',
      'synth': synth_id,
      'patch': patch,
      'view': True
    }
    template = JINJA_ENVIRONMENT.get_template('/synths/%s.html' % synth_id)

    self.response.write(template.render(template_values))
# [END view]
