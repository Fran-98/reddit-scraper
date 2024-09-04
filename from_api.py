import praw
from datetime import datetime
import json

def scrap_comments(submission, config: dict):
        comments = []
        for top_level_comment in submission.comments:
                if top_level_comment.author_flair_text in config['allowed_flairs']:
                        comment = {
                        'user': top_level_comment.author.name,
                        'flair': top_level_comment.author_flair_text,
                        'comment_id': top_level_comment.id,
                        'text': top_level_comment.body
                        }
                        comments.append(comment)

        data = {
               'title': submission.title,
               'id': submission.id,
               'created': submission.created_utc,
               'url': submission.url,
               'text': submission.selftext,
               'comments': comments
        }
        return data

def scrap_sub_api(reddit: praw.Reddit, subreddit_name: str, config: dict):
       
        subreddit = reddit.subreddit(subreddit_name)

        posts = subreddit.top(time_filter = "all", limit = None)

        data = []
        i = 0
        for post in posts:
                submission = reddit.submission(post)
                scraped = scrap_comments(submission, config)
                i += 1
                print(i)
                print(scraped['title'], datetime.fromtimestamp(scraped['created']))
                data.append(scraped)


        with open(f"{subreddit_name}.jsonl", 'w') as f:
                for item in data:
                        f.write(json.dumps(item) + "\n")