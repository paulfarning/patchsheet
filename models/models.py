import os
import logging

from google.appengine.api import users
from google.appengine.ext import ndb

import webapp2


SynthModelMap = {
  'juno-60': 'Juno60',
  'minibrute': 'MiniBrute'
}


# TODO: use abbreviated names in datastore https://developers.google.com/appengine/docs/python/ndb/properties#options

# [START synth]
class Synth(ndb.Model):
  """Models an individual synth."""
  author = ndb.UserProperty()
  created = ndb.DateTimeProperty(auto_now_add=True)
  edited = ndb.DateProperty(auto_now=True)
  make = ndb.StringProperty(indexed=False)
  model = ndb.StringProperty(indexed=False)
# [END synth]

# [START patch]
class Patch(ndb.Expando):
  """Models an individual synth patch."""
  author = ndb.UserProperty()
  created = ndb.DateTimeProperty(auto_now_add=True)
  edited = ndb.DateProperty(auto_now=True)
  name = ndb.StringProperty(indexed=False)
  parameters = ndb.JsonProperty()
# [END patch]

# [START juno60]
class Juno60:
  """Models an individual Juno 60 patch."""
  params_int = [
    'lfo_rate',
    'lfo_delay_time',
    'dco_lfo',
    'dco_pwm',
    'dco_sub_osc',
    'dco_noise',
    'hpf_freq',
    'vcf_freq',
    'vcf_res',
    'vcf_env',
    'vcf_lfo',
    'vcf_kybd',
    'vca_level',
    'env_a',
    'env_d',
    'env_s',
    'env_r'
  ]
  params_bool = [
    'dco_square',
    'dco_saw',
    'dco_sub',
    'chorus_i',
    'chorus_ii'
  ]
  params_string = [
    'lfo_trig_mode',
    'dco_pwm_mode',
    'vcf_polarity',
    'vca_control_signal'
  ]
# [END juno60]

# [START minibrute]
class MiniBrute(ndb.Model):
  """Models an individual MiniBrute patch."""
  params_int = [
    'brute_factor'
  ]
  params_bool = [
  ]
  params_string = [
  ]
# [END minibrute]
