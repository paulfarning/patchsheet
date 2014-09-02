import os
import logging

from google.appengine.api import users
from google.appengine.ext import ndb

import webapp2


SynthModelMap = {
  'juno-60': 'Juno60',
  'sh-101': 'SH101',
  'minibrute': 'MiniBrute'
}


# TODO: use abbreviated names in datastore https://developers.google.com/appengine/docs/python/ndb/properties#options

# [START synth]
class Synth(ndb.Model):
  """Models an individual synth."""
  author = ndb.StringProperty()
  created = ndb.DateTimeProperty(auto_now_add=True)
  edited = ndb.DateProperty(auto_now=True)
  make = ndb.StringProperty()
  model = ndb.StringProperty()
# [END synth]

# [START patch]
class Patch(ndb.Expando):
  """Models an individual synth patch."""
  author = ndb.StringProperty()
  created = ndb.DateTimeProperty(auto_now_add=True)
  edited = ndb.DateProperty(auto_now=True)
  name = ndb.StringProperty()
  owner = ndb.StringProperty()
# [END patch]

# [START juno60]
class Juno60:
  """Models an individual Juno 60 patch."""
  params_num = [
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

# [START sh101]
class SH101:
  """Models an individual SH-101 patch."""
  params_num = [
    'mod_rate',
    'vco_mod',
    'vco_pulse_width',
    'source_pulse',
    'source_saw',
    'source_sub',
    'source_noise',
    'vcf_freq',
    'vcf_res',
    'vcf_env',
    'vcf_mod',
    'vcf_kybd',
    'env_a',
    'env_d',
    'env_s',
    'env_r'
  ]
  params_bool = [
  ]
  params_string = [
    'mod_form',
    'vco_range',
    'vco_pwn_mode',
    'source_sub_oct',
    'env_gatetrig'
  ]
# [END sh101]

# [START minibrute]
class MiniBrute(ndb.Model):
  """Models an individual MiniBrute patch."""
  params_num = [
    'osc_ultrasaw_amount',
    'osc_ultrasaw_rate',
    'osc_ultrasaw_amount',
    'osc_ultrasaw_rate',
    'osc_pulse_width',
    'osc_pulse_amt',
    'osc_metalizer',
    'osc_metalizer_amt',
    'mix_sub_osc',
    'mix_saw',
    'mix_square',
    'mix_triangle',
    'mix_noise',
    'mix_audio',
    'filter_cutoff',
    'filter_resonance',
    'filter_amt',
    'filter_kbd',
    'filter_env_a',
    'filter_env_d',
    'filter_env_s',
    'filter_env_r',
    'amp_env_a',
    'amp_env_d',
    'amp_env_s',
    'amp_env_r',
    'controls_bend',
    'controls_glide',
    'vibrato_rate',
    'lfo_pwm',
    'lfo_pitch',
    'lfo_filter',
    'lfo_amp',
    'lfo_rate',
    'brute_factor'
  ]
  params_bool = [
  ]
  params_string = [
    'osc_wave',
    'osc_octave',
    'filter_mode',
    'filter_speed',
    'controls_mod',
    'controls_aftertouch',
    'vibrato_shape',
    'lfo_wave'
  ]
# [END minibrute]
