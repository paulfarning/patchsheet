require 'lib/patch_writer'


set :relative_links, true
set :css_dir, 'css'
set :js_dir, 'js'
set :images_dir, 'img'
set :haml, :attr_wrapper => '"'

activate :autoprefixer
activate :directory_indexes
activate :image_optimizer

activate :i18n, :mount_at_root => :en, :templates_dir => "./"

activate :patch_writer




# Build-specific configuration
configure :build do
  # For example, change the Compass output style for deployment
  # activate :minify_css

  # Minify Javascript on build
  # activate :minify_javascript

  # Enable cache buster
  # activate :asset_hash

  # Use relative URLs
  # activate :relative_assets

  # Or use a different image path
  # set :http_prefix, "/Content/images/"
end
