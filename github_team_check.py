import sys
from github import Github

access_token = sys.argv[1]
gh_org = sys.argv[2]
gh_team = sys.argv[3]
gh_user = sys.argv[4]

g = Github(access_token)
org = g.get_organization(f"{gh_org}")
team = org.get_team_by_slug(f"{gh_team}")

is_member = False
for member in team.get_members():
    if member.login == gh_user:
        is_member = True
        break

if is_member:
    sys.exit(0)
else:
    print(f"{gh_user} is not authorized to use this action")
    sys.exit(1)
