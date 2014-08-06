class PatchWriter < Middleman::Extension
  def initialize(app, options_hash={}, &block)
    super

    puts "Patch Writer writing"

  end
end

::Middleman::Extensions.register(:patch_writer, PatchWriter)
