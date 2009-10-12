def main(blog):
    for link in blog.settings['nav_links']:
        for link_name,link_url in link.iteritems():
            blog.nav_link_names.append(link_name)
            blog.nav_link_urls.append(link_url)
            

   
