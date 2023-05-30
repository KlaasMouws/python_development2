from github import Github
access_token = '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'
g = Github(access_token)
user = g.get_user()
repo = user.get_repo("pythonInstructions")
contents = repo.get_contents("test1")
print(contents)