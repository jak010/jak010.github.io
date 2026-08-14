import urllib.request
import xml.etree.ElementTree as ET
import re
from email.utils import parsedate_to_datetime

RSS_URL = 'https://jakpentest.tistory.com/rss'
MARKDOWN_FILE = 'index.md'
START_MARKER = '<!-- BLOG-POST-LIST:START -->'
END_MARKER = '<!-- BLOG-POST-LIST:END -->'
MAX_POSTS = 3

def fetch_recent_posts():
    req = urllib.request.Request(RSS_URL, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        with urllib.request.urlopen(req) as response:
            xml_data = response.read()
        
        root = ET.fromstring(xml_data)
        posts = []
        for item in root.findall('./channel/item')[:MAX_POSTS]:
            title = item.find('title').text
            link = item.find('link').text
            date_text = item.find('pubDate').text
            
            try:
                dt = parsedate_to_datetime(date_text)
                formatted_date = dt.strftime('%Y.%m.%d')
                posts.append(f'- [{title}]({link}) ({formatted_date})')
            except Exception:
                posts.append(f'- [{title}]({link})')
            
        return '\n'.join(posts)
    except Exception as e:
        print(f"Error fetching posts: {e}")
        return ""

def update_readme():
    post_list = fetch_recent_posts()
    if not post_list:
        print("No posts found or error occurred.")
        return

    with open(MARKDOWN_FILE, 'r', encoding='utf-8') as f:
        content = f.read()

    # Create replacement text
    replacement = f"{START_MARKER}\n{post_list}\n{END_MARKER}"

    # Use regex to replace everything between markers
    pattern = re.compile(rf"{START_MARKER}.*?{END_MARKER}", re.DOTALL)
    
    if pattern.search(content):
        updated_content = pattern.sub(replacement, content)
        with open(MARKDOWN_FILE, 'w', encoding='utf-8') as f:
            f.write(updated_content)
        print("Successfully updated index.md with recent blog posts.")
    else:
        print(f"Could not find markers {START_MARKER} and {END_MARKER} in index.md")

if __name__ == "__main__":
    update_readme()
