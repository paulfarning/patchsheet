from controllers.home import Main as MainHome
from controllers.patches import Main as MainPatches
from controllers.patches import Create as CreatePatches
from controllers.patches import View as ViewPatches
from controllers.admin import Main as MainAdmin

import webapp2

app = webapp2.WSGIApplication([
  (r'/', MainHome),
  (r'/synths', MainAdmin),
  (r'/patches', MainPatches),
  (r'/patches/create', CreatePatches),
  (r'/patches/([^\/]*)/create', CreatePatches),
  (r'/patches/([^\/]*)/(\d+)', ViewPatches)
], debug=True)
