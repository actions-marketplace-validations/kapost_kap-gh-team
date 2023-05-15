# kap-gh-team
GitHub Action to check user team membership - The goal is to check if the user is authorized to run a specific GitHub Action

# Usage
See [example.yml](.github/workflows/example.yml)

Basic Example with the check
```yaml
name: Example workflow

on:
  workflow_dispatch:

jobs:
  check_membership:
    runs-on: ubuntu-latest
    steps:
      - name: Check if actor is a member of team
        id: membership_check
        uses: kapost/kap-gh-team@v1
        with:
          access_token: ${{ secrets.GITHUB_TOKEN }}
          organization: yourorg
          team: yourteam
          user: ${{ github.actor }}
      
      - name: Fail workflow if not a team member
        if: ${{ steps.membership_check.outputs.success == 'false' }}
        run: exit 1
```

Example with additional action

```yaml
name: Example workflow

on:
  workflow_dispatch:        
  check_membership:
    runs-on: ubuntu-latest
    steps:
      - name: Check if actor is a member of team
        id: membership_check
        uses: kapost/kap-gh-team@v1
        with:
          access_token: ${{ secrets.GITHUB_TOKEN }}
          organization: yourorg
          team: yourteam
          user: ${{ github.actor }}
      
      - name: Fail workflow if not a team member
        if: ${{ steps.membership_check.outputs.success == 'false' }}
        run: exit 1
      
      - name: Send Slack message
        if: ${{ steps.membership_check.outputs.success == 'true' }}
        uses: slackapi/send-message-action@v1.2.3
        with:
          token: ${{ secrets.SLACK_BOT_TOKEN }}
          channel: mychannel
          text: "The check succeeded!"

      - uses: actions/checkout@v3
      
      - uses: actions/setup-node@v3
        with:
          node-version: 18
      
      - run: npm ci
      
      - run: npm test
```

# Secrets
Only the GitHub access token is required to run this action. This token needs to have permissions to list GitHub teams and their members. Information on creating a token can be found [here](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token).
