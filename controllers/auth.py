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


providers = {
  'Google': users.create_login_url(federated_identity='https://www.google.com/accounts/o8/id'),
  'Twitter': users.create_login_url(federated_identity='https://twitter.com'),
  'Facebook': users.create_login_url(federated_identity='facebook.com'),
  'Yahoo': users.create_login_url(federated_identity='yahoo.com')
}


# [START main]
class Main(webapp2.RequestHandler):
  def get(self):

    template_values = {
      'providers': providers
    }
    template = JINJA_ENVIRONMENT.get_template('login.html')

    self.response.write(template.render(template_values))
# [END main]
