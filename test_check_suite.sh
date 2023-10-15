curl -Lv --request POST \
--url "https://api.github.com/applications/$GITHUB_CLIENT_ID/token" \
--user "$GITHUB_CLIENT_ID:$GITHUB_APP_CLIENT_SECRET" \
--header "Accept: application/vnd.github+json" \
--header "X-GitHub-Api-Version: 2022-11-28"
