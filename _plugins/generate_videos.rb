# frozen_string_literal: true

# Jekyll plugin to automatically generate videos data from YouTube API
# This plugin runs the Python script to fetch videos and generate _data/videos.yml

module Jekyll
  module GenerateVideos
    class Generator < Jekyll::Generator
      safe true
      priority :high

      def generate(site)
        Jekyll.logger.info "Videos:", "Generating videos data..."
        
        # Run the Python script to generate videos data
        result = system("python3 scripts/generate_videos.py > /dev/null 2>&1")
        
        if result
          Jekyll.logger.info "Videos:", "Generation complete!"
          
          # Reload the data files to pick up the new videos.yml
          site.data['videos'] = YAML.load_file(File.join(site.source, '_data', 'videos.yml')) if File.exist?(File.join(site.source, '_data', 'videos.yml'))
        else
          Jekyll.logger.warn "Videos:", "Generation failed - videos may be out of date"
        end
      end
    end
  end
end

# Register the generator
Jekyll::Hooks.register :site, :after_init do |site|
  Jekyll.logger.info "Videos:", "Initializing videos data generation..."
end
