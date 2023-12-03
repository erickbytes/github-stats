# github-stats

There are 2 Python scripts in this repo. **repo_traffic.py** uses the [PyGithub](https://pygithub.readthedocs.io/en/latest/index.html) module to return clones, views and referrers of your own Github repos. **stargazers.py** returns the stargazers of any Github repo. This repo holds scripts returning Github data for repo:
- clones
- referrers
- views
- stargazers

<br />

**Install Python Libraries**

```
pip install PyGithub
pip install pandas
pip install tqdm
```
New to Python? Read more about pip installs [on my blog](https://lofipython.com/how-to-python-pip-install-new-libraries).

<br />

**Troubleshooting "Must have push access to repository"**
```
github.GithubException.GithubException: 403
{"message": "Must have push access to repository",
"documentation_url": "https://docs.github.com/rest/metrics/traffic#get-top-referral-sources"}
```
I fixed this error by going to ["Developer Settings"](https://github.com/settings/tokens) > "Fine Grained Token" > Create New Token or Edit and then setting "Repository permissions" > "Content" > "Read and write".

<br />

**curl Github API Example**

This is another way to get repo data from the [Github API](https://docs.github.com/en/rest/metrics/traffic#get-repository-clones):
```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer your_github_token" \
  -H "X-GitHub-Api-Version: 2022-11-28" \
  https://api.github.com/repos/{username}/{repo_name}/traffic/clones
```
