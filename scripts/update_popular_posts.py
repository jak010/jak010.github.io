import os
import re
from google.analytics.data_v1beta import BetaAnalyticsDataClient
from google.analytics.data_v1beta.types import (
    DateRange,
    Dimension,
    Metric,
    RunReportRequest,
)

PROPERTY_ID = os.environ.get("GA4_PROPERTY_ID", "407462765")
MARKDOWN_FILE = 'index.md'
START_MARKER = '<!-- POPULAR-POSTS:START -->'
END_MARKER = '<!-- POPULAR-POSTS:END -->'
MAX_POSTS = 3

def fetch_popular_posts():
    try:
        client = BetaAnalyticsDataClient()
        request = RunReportRequest(
            property=f"properties/{PROPERTY_ID}",
            dimensions=[Dimension(name="pagePath"), Dimension(name="pageTitle")],
            metrics=[Metric(name="screenPageViews")],
            date_ranges=[DateRange(start_date="30daysAgo", end_date="today")],
            limit=20
        )
        
        response = client.run_report(request)
        
        medals = ["🥇", "🥈", "🥉"]
        posts = []
        count = 0
        
        for row in response.rows:
            path = row.dimension_values[0].value
            title = row.dimension_values[1].value
            views = row.metric_values[0].value
            
            # 필터링 로직 (메인 페이지, 카테고리, 태그, 관리자 페이지 등 제외)
            if path == '/' or 'category' in path or path.startswith('/guestbook') or path.startswith('/tag') or path.startswith('/manage'):
                continue
                
            title = title.split(' - ')[0].strip()
            medal = medals[count] if count < len(medals) else "🔹"
            url = f"https://jakpentest.tistory.com{path}"
            
            posts.append(f"- {medal} [{title}]({url}) (최근 30일 조회수: {views}회)")
            
            count += 1
            if count >= MAX_POSTS:
                break
                
        return '\n'.join(posts)
    except Exception as e:
        print(f"Error fetching GA4 data: {e}")
        return ""

def update_readme():
    post_list = fetch_popular_posts()
    if not post_list:
        print("No popular posts found or error occurred.")
        return

    md_path = os.path.join(os.path.dirname(__file__), "..", MARKDOWN_FILE)
    
    with open(md_path, 'r', encoding='utf-8') as f:
        content = f.read()

    replacement = f"{START_MARKER}\n{post_list}\n{END_MARKER}"
    pattern = re.compile(rf"{START_MARKER}.*?{END_MARKER}", re.DOTALL)
    
    if pattern.search(content):
        updated_content = pattern.sub(replacement, content)
        with open(md_path, 'w', encoding='utf-8') as f:
            f.write(updated_content)
        print("Successfully updated index.md with popular blog posts.")
    else:
        print(f"Could not find markers {START_MARKER} and {END_MARKER} in {MARKDOWN_FILE}")

if __name__ == "__main__":
    update_readme()
