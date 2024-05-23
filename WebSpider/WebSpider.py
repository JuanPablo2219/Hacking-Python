# David Pozo
#Juan Pablo Malla
# Kevin Sibri


import requests
import re
import argparse

#
def get_html(url: str):
    try:
        response = requests.get(url)
        if response.status_code >= 300:
            print(f"this page can't be fetched: {url}")
            return ""
        html = str(response.content)
        return html
    except:
        return ''

def get_links(html: str):
    links = re.findall(r'https:\/\/\w+.\w+.\w+[\/\w+]+|http:\/\/\w+.\w+.\w+[\/\w+]+[\.?\w+]+', html)
    return links

def get_links_recursive(links, tries):
    for link in links:
        html = get_html(link)
        if tries == 0:
            return
        
        new_links = get_links(html)
        
        with open(args.outfile, "a") as out_file:
            str_links = "\n".join(new_links) + "\n"
            out_file.write(str_links)
        get_links_recursive(new_links, tries - 1)


parser = argparse.ArgumentParser(description="crawler")
parser.add_argument("link_seed", type=str)
parser.add_argument("tries", type=int)
parser.add_argument("--outfile", type=str, default="links.txt")

args = parser.parse_args()

with open(args.link_seed, "r") as file:
    links = file.readlines()
    get_links_recursive(links, tries=args.tries)
