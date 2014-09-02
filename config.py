import collections
import jinja2
import webapp2
from authomatic.providers import oauth2, oauth1, gaeopenid

JINJA_ENVIRONMENT = jinja2.Environment(
  loader=jinja2.FileSystemLoader('views'),
  extensions=['jinja2.ext.autoescape'],
  autoescape=True)
JINJA_ENVIRONMENT.globals['OrderedDict'] = collections.OrderedDict

AUTHOMATIC_CONFIG = {

    'tw': { # Your internal provider name

        # Provider class
        'class_': oauth1.Twitter,

        # Twitter is an AuthorizationProvider so we need to set several other properties too:
        'consumer_key': '########################',
        'consumer_secret': '########################',
    },

    'fb': {

        'class_': oauth2.Facebook,

        # Facebook is an AuthorizationProvider too.
        'consumer_key': '########################',
        'consumer_secret': '########################',

        # But it is also an OAuth 2.0 provider and it needs scope.
        'scope': ['user_about_me', 'email', 'publish_stream', 'read_stream'],
    },

    'gae_oi': {

        # OpenID provider based on Google App Engine Users API.
        # Works only on GAE and returns only the id and email of a user.
        # Moreover, the id is not available in the development environment!
        'class_': gaeopenid.GAEOpenID,
    }

}
