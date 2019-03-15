import praw
import webbrowser
import secretStuff

#need this to call reddit API
reddit = praw.Reddit(client_id =secretStuff.client_id,
                     client_secret = secretStuff.client_secret,
                     user_agent = 'DogMounter')


#list of 'cute' subreddits
subreddits = ['aww', 'wholesomememes', 'eyebleach']


for name in subreddits:
    #gets subreddit object
    subreddit = reddit.subreddit(name)

    #gets top 4 hotposts from each subreddit
    hotposts = subreddit.hot(limit=4)

    print(name)

    for post in hotposts:
        if not post.stickied:
            #opens the post in url
            webbrowser.open(post.url)


"""
#prints title for top 5 hot posts in gaming subreddit that are not stickied
subreddit = reddit.subreddit('aww')

hot_python = subreddit.hot(limit=2)
counter = 0

for submission in hot_python:
    #prints submission's attributes
    #print(dir(submission))


    if not submission.stickied:
        print(submission.url)
        if counter == 0:
            print(counter)
            webbrowser.open_new(submission.url)
        else:
            webbrowser.open(submission.url)
        counter += 1
"""