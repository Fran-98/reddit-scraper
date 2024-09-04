import json
from datetime import datetime
from tqdm import tqdm

def parse_submissions(path: str):
        posts = []
        with open(path, encoding='utf-8', mode='r') as file:
                for line in file.readlines():
                        post = json.loads(line)
                        posts.append(post)
        return posts

def parse_comments(path: str):
        comments = {}
        with open(path, encoding='utf-8', mode='r') as file:
                for line in file.readlines():
                        comment = json.loads(line)
                        parent_id = comment['link_id'].split('_')[-1]
                        if parent_id in comments.keys():
                                comments[parent_id].append(comment)
                        else:
                                comments[parent_id] = [comment]
        return comments

def scrap_comments(submission, all_comments:dict , config: dict):
                comments = []
                if submission['id'] in all_comments.keys():
                        for post_comment in all_comments[submission['id']]:
                                if post_comment['author_flair_text'] in config['allowed_flairs']:
                                        comment = {
                                        'user': post_comment['author'],
                                        'flair': post_comment['author_flair_text'],
                                        'comment_id': post_comment['id'],
                                        'text': post_comment['body']
                                        }
                                        comments.append(comment)

                        data = {
                                'title': submission['title'],
                                'id': submission['id'],
                                'created': submission['created_utc'],
                                'url': submission['url'],
                                'text': submission['selftext'],
                                'comments': comments
                        }
                        return data
                else:
                        return None

def scrap_sub_file(config: dict, path_submissions: str, path_comments: str):
        # We need to parse the data files
        posts = parse_submissions(path_submissions)
        comments = parse_comments(path_comments)
        subreddit_name = posts[1]['subreddit']

        data = []

        for post in tqdm(posts, position=0):
                #submission = reddit.submission(post)
                scraped = scrap_comments(post, comments, config)
                if scraped is not None:
                        tqdm.write(f"{scraped['title']} - {datetime.fromtimestamp(scraped['created'])}")
                        data.append(scraped)
                else:
                        tqdm.write('Detected not matching pair')


        with open(f"{subreddit_name}.jsonl", 'w') as f:
                for item in data:
                        f.write(json.dumps(item) + "\n")
