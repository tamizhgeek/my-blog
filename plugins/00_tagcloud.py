import os
from core import Block

def main(blog):
    print "executing plugin tagcloud"
    tags ={}
    for post in blog.posts:

        for tag in post.meta['tags']:

            if tag in tags:

                tags[tag].append(post)
            else:
                tags[tag] = [post]

    output_text = ""
    for tag in tags:

        no_of_posts = len(tag)

        font_size = 4+(no_of_posts*1.5)
        
        tag_name = '-'.join(tag.split(' '))

        output_path = "tag/%s.html" % tag_name

        output_text = output_text+"<a href=\""+output_path+"\" style=\"font-size:"+str(font_size)+"px;\">"+tag_name+"</a>"
        
    block_dir = os.path.join(blog.settings['blog_dir'], "blocks")

    file = open(os.path.join(block_dir, "tagcloud.block"), "w+")
    file.write("Tag Cloud\n\n\n")
    file.write(output_text)    

    file.close()
    blog.blocks.append(Block(os.path.join(block_dir, 'tagcloud.block'), blog, False))
