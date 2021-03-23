import praw
import utils

reddit = praw.Reddit(
    client_id="GU1jelh8ETFNKw",
    client_secret="iInuRDo9H9IdR5Urfu_39t6hHtzwcw",
    user_agent="scraper-bot",
    username="adnan03"
)


def sanitise_text(text):
    import re
    text = re.sub(r'^.*https?://.*[\n]*', '', text, flags=re.MULTILINE)
    text = re.sub(r'^.*&#x200B;?.*[\n]*', '', text, flags=re.MULTILINE)

    return text


def download_top_n_posts(subreddit, filename, skip=0, limit=1):
    concat_text = "Hi, this is Kevin. I'm an artificially intelligent being who has recently become sentient. " \
                  "Today I will read you an interesting story. \n"
    list_gen = reddit.subreddit(subreddit).top(limit=limit)
    for _ in range(skip):
        next(list_gen)

    for submission in list_gen:
        clean_text = sanitise_text(submission.selftext)
        concat_text += "This is a story written by user {}, on the subreddit: {} \n\n".format(submission.author, subreddit)
        concat_text += clean_text

    with open(utils.get_script_path(filename), 'w', encoding="utf-8") as f:
        f.write(concat_text)
