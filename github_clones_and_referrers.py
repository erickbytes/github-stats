import pandas as pd
import os
from datetime import date
from github import Github, GithubException, Auth


def top_referrers(repo):
    """Returns dictionary of github repo referral traffic.
    https://pygithub.readthedocs.io/en/latest/examples/Repository.html#get-the-top-10-referrers-over-the-last-14-days
    """
    contents = repo.get_top_referrers()
    return contents


def clones_traffic(repo):
    """Returns dictionary of Github repo clones traffic.
    https://pygithub.readthedocs.io/en/latest/examples/Repository.html#get-number-of-clones-and-breakdown-for-the-last-14-days
    """
    contents = repo.get_clones_traffic(per="week")
    return contents


# In an ubuntu shell, set access_token variable: export access_token=your_github_token
access_token = os.getenv("access_token")
auth = Auth.Token(access_token)
# Public Web Github
g = Github(auth=auth)
repos = ["lofipython", "delta_airports", "wayak-website", "finsou.py", "divbull"]
rows = list()
for repo_name in repos:
    try:
        repo = g.get_repo(f"erickbytes/{repo_name}")
    except GithubException:
        print(f"Skipped {repo_name}, repo not found.")
        continue
    referrers = top_referrers(repo)
    clones = clones_traffic(repo)
    row = [repo_name, clones["uniques"], clones["count"], referrers]
    rows.append(row)

names = ["Repo Name", "Unique Clones", "Total Clones", "Referrers"]
traffic = pd.DataFrame(rows, columns=names)
traffic.to_csv(f"Github_Traffic_{date.today()}.csv", index=False)
