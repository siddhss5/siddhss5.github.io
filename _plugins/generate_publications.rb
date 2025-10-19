# Jekyll plugin to automatically generate publications, projects, and awards data before build
# This ensures all data is always up-to-date when viewing the site locally

Jekyll::Hooks.register :site, :after_init do |site|
  Jekyll.logger.info "Publications:", "Generating publications and projects data..."
  
  # Run the Python script to generate publications.yml and projects.yml
  result = system("uv run python scripts/generate_publications.py > /dev/null 2>&1")
  
  if result
    Jekyll.logger.info "Publications:", "Publications generation complete!"
  else
    Jekyll.logger.warn "Publications:", "Publications generation failed - publications may be out of date"
  end
  
  # Run the Python script to generate awards.yml
  Jekyll.logger.info "Awards:", "Generating awards data..."
  awards_result = system("uv run python scripts/generate_awards.py > /dev/null 2>&1")
  
  if awards_result
    Jekyll.logger.info "Awards:", "Awards generation complete!"
  else
    Jekyll.logger.warn "Awards:", "Awards generation failed - awards may be out of date"
  end
end

