import praw
def parse(subreddit):
    subreddit = str(subreddit)
    f = open(subreddit,'w')
    r = praw.Reddit('CommentParser by u/captainpantsman')
    subreddit = r.get_subreddit(subreddit)
    for submission in subreddit.get_hot(limit=25):
        comments = praw.helpers.flatten_tree(submission.comments)
        for things in comments:
            f.write(str(things))
    f.close()
