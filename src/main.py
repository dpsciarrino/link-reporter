from util.util import get_links_from_yoast, get_content_object

url = 'https://www.example.com/sitemap_index.xml'

# List of links on site
links = get_links_from_yoast(url)

# Get content from links
for link in links:
    get_content_object(link)
