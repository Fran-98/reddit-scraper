import os
import yaml
import praw
import argparse
from dotenv import load_dotenv
from from_api import scrap_sub_api
from from_file import scrap_sub_file

load_dotenv()  # take environment variables from .env.

with open('config.yaml', 'r') as file:
    config = yaml.safe_load(file)

client_id = os.environ['REDDIT_CLIENT_ID']
client_secret = os.environ['REDDIT_CLIENT_SECRET']
user_agent = os.environ['REDDIT_USER_AGENT']

reddit = praw.Reddit(
    client_id=client_id,
    client_secret=client_secret,
    user_agent=user_agent,
)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Scrap Sub-Reddit Script By Fran98')

    parser.add_argument('mode', type=str,
                        help='Mode to run "file" or "api".')

    parser.add_argument('--subreddit', type=str,
                        help='Name of the subreddit to scrap. Needed for "api" mode.')
    
    parser.add_argument('--path_submissions', type=str,
                        help='Path to submission file for "file" mode.')
    
    parser.add_argument('--path_comments', type=str,
                        help='Path to comments file for "file" mode.')
    
    args = parser.parse_args()

    if args.mode == 'file':
        scrap_sub_file(reddit, config, args.path_submissions, args.path_comments)
    elif args.mode == 'api':
        scrap_sub_api(reddit, args.subreddit, config)