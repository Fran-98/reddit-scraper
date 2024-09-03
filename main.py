import praw
import os
import pprint

client_id = os.environ['REDDIT_CLIENT_ID']
client_secret = os.environ['REDDIT_SECRET']
user_agent = os.environ['REDDIT_USER_AGENT']

reddit = praw.Reddit(
    client_id=client_id,
    client_secret=client_secret,
    user_agent=user_agent,
)

url = "https://www.reddit.com/r/DerechoGenial/comments/1f7xevt/me_puedo_negar_a_tener_que_hacerme_responsable_de/"
submission = reddit.submission(url=url)


for top_level_comment in submission.comments:
        print(top_level_comment.author_flair_text)



""" Ejemplo comment
{'_fetched': True,
 '_reddit': <praw.reddit.Reddit object at 0x00000187B231B350>,
 '_replies': <praw.models.comment_forest.CommentForest object at 0x00000187B56A8D10>,
 '_submission': Submission(id='1f7xevt'),
 'all_awardings': [],
 'approved_at_utc': None,
 'approved_by': None,
 'archived': False,
 'associated_award': None,
 'author': Redditor(name='Fresh-Shower-6057'),
 'author_flair_background_color': '#ddbd37',
 'author_flair_css_class': 'untrusted',
 'author_flair_richtext': [],
 'author_flair_template_id': '44f375b2-52ff-11ec-8a2d-72251cf9be77',
 'author_flair_text': 'NSUB - NoSoyUnBoga',
 'author_flair_text_color': 'dark',
 'author_flair_type': 'text',
 'author_fullname': 't2_83wg7xfr',
 'author_is_blocked': False,
 'author_patreon_flair': False,
 'author_premium': False,
 'awarders': [],
 'banned_at_utc': None,
 'banned_by': None,
 'body': 'Lo que le paso a tu suegra va a pasar a tu pareja, podés vivir con '
         'ello o no, pero va a ser un tema...',
 'body_html': '<div class="md"><p>Lo que le paso a tu suegra va a pasar a tu '
              'pareja, podés vivir con ello o no, pero va a ser un '
              'tema...</p>\n'
              '</div>',
 'can_gild': False,
 'can_mod_post': False,
 'collapsed': True,
 'collapsed_because_crowd_control': None,
 'collapsed_reason': 'comment score below threshold',
 'collapsed_reason_code': 'LOW_SCORE',
 'comment_type': None,
 'controversiality': 0,
 'created': 1725366360.0,
 'created_utc': 1725366360.0,
 'depth': 0,
 'distinguished': None,
 'downs': 0,
 'edited': False,
 'gilded': 0,
 'gildings': {},
 'id': 'llan4w5',
 'is_submitter': False,
 'likes': None,
 'link_id': 't3_1f7xevt',
 'locked': False,
 'mod_note': None,
 'mod_reason_by': None,
 'mod_reason_title': None,
 'mod_reports': [],
 'name': 't1_llan4w5',
 'no_follow': True,
 'num_reports': None,
 'parent_id': 't3_1f7xevt',
 'permalink': '/r/DerechoGenial/comments/1f7xevt/me_puedo_negar_a_tener_que_hacerme_responsable_de/llan4w5/',
 'removal_reason': None,
 'report_reasons': None,
 'saved': False,
 'score': -19,
 'score_hidden': False,
 'send_replies': True,
 'stickied': False,
 'subreddit': Subreddit(display_name='DerechoGenial'),
 'subreddit_id': 't5_q0war',
 'subreddit_name_prefixed': 'r/DerechoGenial',
 'subreddit_type': 'public',
 'top_awarded_type': None,
 'total_awards_received': 0,
 'treatment_tags': [],
 'unrepliable_reason': None,
 'ups': -19,
 'user_reports': []}
"""