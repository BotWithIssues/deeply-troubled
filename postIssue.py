from github import Github
import json


account = Github('c4a614b8f62eba7db6d4d34c4da2b1f77ae5a1ed2253baa68413925d9e2f4f6f178953eee4440e7a')
for repo in account.get_user().get_repos():
    print(repo.name)