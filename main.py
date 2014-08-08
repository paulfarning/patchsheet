from controllers.home import Main as MainHome
from controllers.patches import Main as MainPatches
from controllers.patches import Create as CreatePatches
from controllers.patches import View as ViewPatches

import webapp2

application = webapp2.WSGIApplication([
  (r'/', MainHome),
  (r'/patches', MainPatches),
  (r'/patches/create', CreatePatches),
  (r'/patches/([^\/]*)/create', CreatePatches),
  (r'/patches/([^\/]*)/(\d+)', ViewPatches)
], debug=True)
