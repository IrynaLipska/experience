import pytest


@pytest.mark.api
def test_user_exists(github_api):
    user = github_api.get_user('defunkt')
    assert user['login'] == 'defunkt'


@pytest.mark.api
def test_user_not_exists(github_api):
    r = github_api.get_user('butenkosergii')
    assert r['message'] == 'Not Found'


@pytest.mark.api
def test_repo_can_be_found(github_api):
    r = github_api.search_repo("become-qa-auto")
    assert r['total_count'] == 50
    assert 'become-qa-auto' in r['items'][0]['name'] 


@pytest.mark.api
def test_repo_cannot_be_found(github_api):
    r = github_api.search_repo("sergiibutenko_repo_non_exist")
    assert r['total_count'] == 0


@pytest.mark.api
def test_repo_with_single_char_be_found(github_api):
    r = github_api.search_repo("s")
    assert r['total_count'] != 0


@pytest.mark.api
def test_list_commits(github_api):
    owner = "octocat"
    repo = "Spoon-Knife"
    commits = github_api.list_commits(owner, repo)
    assert len(commits) > 0


@pytest.mark.api
def test_commit_comment(github_api):
    owner = "octocat"
    repo = "Hello-World"
    comment_id = "1"
    comment = github_api.test_commit_comment(owner, repo, comment_id)
    assert len(comment) > 0


@pytest.mark.api
def test_check_if_emoji_exists(github_api):
    emoji_name = "ukraine"
    emojis = github_api.test_check_if_emoji_exists()
    assert emoji_name in emojis
