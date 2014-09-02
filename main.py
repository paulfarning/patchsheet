import sys
sys.path.insert(0, 'libs')

from controllers.home import Main as MainHome
from controllers.patches import Main as MainPatches
from controllers.patches import Create as CreatePatches
from controllers.patches import View as ViewPatches
from controllers.admin import Main as MainAdmin

from authomatic import Authomatic
from authomatic.adapters import Webapp2Adapter

from config import AUTHOMATIC_CONFIG

import webapp2

authomatic = Authomatic(config=AUTHOMATIC_CONFIG, secret='yumyumrandomstring')

class Login(webapp2.RequestHandler):
  def get(self, provider_name):
    result = authomatic.login(Webapp2Adapter(self), provider_name)
    if result:
      self.response.write('<a href="..">Home</a>')

      if result.error:
        self.response.write(u'<h2>Damn that error: {}</h2>'.format(result.error.message))
      elif result.user:
        if not (result.user.name and result.user.id):
          result.user.update()

        self.response.write(u'<h1>Hi {}</h1>'.format(result.user.name))
        self.response.write(u'<h2>Your id is: {}</h2>'.format(result.user.id))
        self.response.write(u'<h2>Your email is: {}</h2>'.format(result.user.email))

        if result.user.credentials:
          if result.provider.name == 'fb':
            self.response.write('Your are logged in with Facebook.<br />')

          if result.provider.name == 'tw':
              self.response.write('Your are logged in with Twitter.<br />')


app = webapp2.WSGIApplication([
  (r'/', MainHome),
  (r'/login/([^\/]*)', Login),
  (r'/synths', MainAdmin),
  (r'/patches', MainPatches),
  (r'/patches/create', CreatePatches),
  (r'/patches/([^\/]*)/create', CreatePatches),
  (r'/patches/([^\/]*)/(\d+)', ViewPatches)
], debug=True)
