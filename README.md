# Reddit Scraper
A basic script to scrap all the information inside a sub-reddit.

## Modes

### PRAW mode
This mode uses PRAW library and the Reddit API to scrap the las top 1000 post inside a sub, this is a limitation from the API.

### File mode
This mode uses files from reddit data dumps, that can be obtained from sites like [the eye](https://the-eye.eu/). Leave the submissions and comments file inside the root folder, setup the `config.yaml` file and run the script.

## How to run
### .env (Only needed for api mode)
First we need to set the `.env` file.
All the required steps are listed on the [praw quick start page](https://praw.readthedocs.io/en/stable/getting_started/quick_start.html).
An example `.env` file should be like this:

```
REDDIT_CLIENT_ID="client id"
REDDIT_CLIENT_SECRET="client secret"
REDDIT_USER_AGENT="user agent"
```

### Config file

Inside the `config.yaml` there are many things that could be implemented, right now there is only one option that is to edit which user flairs should be acepted for our comments.

### Running from command line
> "API mode example"
`python main.py "api" --subreddit "pics"`

> "File mode example"
`python main.py "file" --path_submissions "pics_submissions" --path_comments "pics_comments"`

## Conc
The script is simple and may need some modifications for specific use cases. I strongly suggest to adapt it to you needs.

