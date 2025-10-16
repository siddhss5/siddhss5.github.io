# Jekyll plugin to automatically generate publications and projects data before build
# This ensures all data is always up-to-date when viewing the site locally

Jekyll::Hooks.register :site, :after_init do |site|
  Jekyll.logger.info "Publications:", "Generating publications and projects data..."
  
  # Run the Python script to generate publications.yml and projects.yml
  result = system("python3 scripts/generate_publications.py > /dev/null 2>&1")
  
  if result
    Jekyll.logger.info "Publications:", "Generation complete!"
  else
    Jekyll.logger.warn "Publications:", "Generation failed - publications may be out of date"
  end
end

