# puts "PatchApp"
# require 'sinatra'
# require 'sinatra/base'
# require 'json' # Always handy

# class PatchApp < Sinatra::Base

#   # Fall back to this when needed
#   set :static, true
#   set :public_folder, File.dirname(__FILE__) + '/tmp'

#   # Define a form submit route, in POST
#   post '/subscribe' do

#     # This makes it easy to access heroku environment variables
#     ENV['MY_ENV_VAR']

#     # ... Your server logic goes here

#     # Last arg is sent to the browser
#     params.to_json
#   end
# end
