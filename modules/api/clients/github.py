import requests


class GitHub:
    def get_user(self, username):
        r = requests.get(f'https://api.github.com/users/{username}')
        body = r.json()

        return body
    
    def search_repo(self, name):
        r =  requests.get("https://api.github.com/search/repositories", params={"q": name})
        body = r.json()

        return body
    
    def list_commits(self, owner, repo):
        r = requests.get('https://api.github.com/repos/{owner}/{repo}/commits')
        commits = r.json()
        
        return commits
    
    def test_commit_comment(self, owner, repo, comment_id):
        r = requests.get('https://api.github.com/repos/{owner}/{repo}/comments/{comment_id}')
        comments = r.json()
        
        return comments


    def test_check_if_emoji_exists(self):
        r = requests.get('https://api.github.com/emojis')
        emojis = r.json()

        return emojis