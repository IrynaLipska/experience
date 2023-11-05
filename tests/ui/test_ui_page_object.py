from modules.ui.page_objects.sign_in_page import SignInPage
from modules.ui.page_objects.check_track import CheckTrack
import pytest


@pytest.mark.ui
def test_check_incorrect_username_page_object():
    sign_in_page = SignInPage()

    # open https://github.com/login 
    sign_in_page.go_to()

    # enter to GitHub
    sign_in_page.try_login("page_object@gmail.com", "wrong password")

    # check page name
    assert sign_in_page.check_title("Sign in to GitHub · GitHub")

    # close browser
    sign_in_page.close()

@pytest.mark.ui
def test_check_incorrect_track_number():

    check_track = CheckTrack()
    check_track.go_to()

    check_track.enter_track_number("1111111111")

    assert check_track.check_title("Трекінг посилки | Nova Global")

    check_track.close()

