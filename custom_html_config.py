# Custom HTML configuration for professional report
c = get_config()

# HTML Exporter configuration
c.HTMLExporter.template_name = 'lab'
c.HTMLExporter.theme = 'light'
c.HTMLExporter.anchor_link_text = '🔗'
c.HTMLExporter.exclude_input_prompt = True
c.HTMLExporter.exclude_output_prompt = True
c.HTMLExporter.exclude_input = False
c.HTMLExporter.exclude_output = False
c.HTMLExporter.exclude_raw = True
c.HTMLExporter.exclude_unknown = True
