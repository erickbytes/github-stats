import pandas as pd
from github import Github
import os


def stars(repo, g):
    """Retrieve github repo star count.
    Accepts: str, repo "username/repo name",ex: "getpelican/pelican"
    Returns: int, github repo stargazers number"""
    repo = g.get_repo(repo)
    return repo.stargazers_count


# static site repos: http://lofipython.com/a-brief-summary-of-promising-python-static-site-generators/
urls = [
    "https://github.com/getpelican/pelican",
    "https://github.com/lektor/lektor",
    "https://github.com/eudicots/Cactus",
    "https://github.com/getnikola/nikola",
    "https://github.com/sunainapai/makesite",
    "https://github.com/hyde/hyde",
    "https://github.com/Anomareh/mynt",
    "https://github.com/staticjinja/staticjinja",
]
repos = [url.replace("https://github.com/", "") for url in urls]
# In an ubuntu shell, set access_token variable: export access_token=your_github_token
access_token = os.getenv("access_token")
g = Github(access_token)
counts = [(repo, stars(repo, g)) for repo in repos]
stars_df = pd.DataFrame(counts, columns=["repo", "stars"])
stars_df.to_csv("Stars.csv", index=False)
