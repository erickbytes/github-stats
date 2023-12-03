# github-stats

This repo holds scripts returning Github data for repo:
- clones
- referrers
- views
- stargazers

This Python code uses the [PyGithub](https://pygithub.readthedocs.io/en/latest/index.html) module to return data about a Github repo.

**Install Python Libraries**

```
pip install PyGithub
pip install pandas
pip install tqdm
```
New to Python? Read more about pip installs [on my blog](https://lofipython.com/how-to-python-pip-install-new-libraries).


**Troubleshooting "Must have push access to repository"**
```
github.GithubException.GithubException: 403 {"message": "Must have push access to repository", "documentation_url": "https://docs.github.com/rest/metrics/traffic#get-top-referral-sources"}
```
This error can be fixed by going to ["Developer Settings"](https://github.com/settings/tokens) > "Fine Grained Token" > Create New Token or Edit > "Repository permissions" > "Content" > "Read and write".
