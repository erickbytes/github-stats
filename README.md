# github-stats

This repo holds scripts returning Github data for repo:
- clones
- referrers
- views
- stargazers

This Python code uses the [PyGithub](https://pygithub.readthedocs.io/en/latest/index.html) module to return data about a Github repo.

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
github.GithubException.GithubException: 403 {"message": "Must have push access to repository", "documentation_url": "https://docs.github.com/rest/metrics/traffic#get-top-referral-sources"}
```
I fixed this error by going to ["Developer Settings"](https://github.com/settings/tokens) > "Fine Grained Token" > Create New Token or Edit and then setting "Repository permissions" > "Content" > "Read and write".

<br />

**curl Github API Example**
This is another way to get the data from the Github API:
```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer your_github_token" \
  -H "X-GitHub-Api-Version: 2022-11-28" \
  https://api.github.com/repos/{username}/{repo_name}/traffic/clones
```
