# Testing Framework for GitHub API, UI, and SQL Database

This testing framework aims to perform checks on various parts of GitHub API, web interface, and the database.

## Usage

### Preparing

Before using the framework, ensure that you have the necessary dependencies and environment set up to run the tests.

### Test Framework for GitHub API, UI, and SQL Database

This testing framework is designed to execute various checks and tests across different layers of the technological stack:

#### HTTP Request Tests
- `test_first_request`: Executes a request to `http://api.github.com/zen` and prints the received response.
- `test_second_request`: Sends a request to `https://api.github.com/users/defunkt`, verifies the existence of the user, and checks the response headers.
- `test_second_request`: Sends a request to `https://api.github.com/users/sergii_butenko` and checks if it returns a status 404.

#### API Tests
- `test_user_exists`: Verifies the existence of the user "defunkt".
- `test_user_not_exists`: Checks the absence of the user "butenkosergii".
- `test_repo_can_be_found`: Ensures the presence of a repository with the name "become-qa-auto".
- `test_repo_cannot_be_found`: Checks the absence of a repository with the name "sergiibutenko_repo_non_exist".
- `test_repo_with_single_char_be_found`: Checks if repositories are found when searching by a single character.
- `test_list_commits`: Verifies the existence of commits in the "Spoon-Knife" repository.
- `test_commit_comment`: Checks for comments on a commit in the "Hello-World" repository.
- `test_check_if_emoji_exists`: Ensures the existence of a specific emoji, in this case, "ukraine".

#### Change and Validation Tests
- `test_remove_name`: Tests the capability to remove a user's name.
- `test_name`: Validates the correctness of the user's set name.
- `test_second_name`: Checks the accuracy of the user's set surname.

#### Database Tests
- `test_database_connection`: Verifies the connection to the database.
- `test_check_all_users`: Retrieves a list of all users.
- `test_check_user_sergii`: Validates Sergii's user information from the database.
- `test_product_qnt_update`: Tests the update of product quantities in the database.
- `test_product_insert`: Checks the insertion of a new product into the database.
- `test_product_delete`: Ensures the deletion of a product from the database.
- `test_detailed_orders`: Verifies the details of a specific order in the database.
- `test_check_user_by_id`: Checks user information by ID.
- `test_user_insert`: Validates the insertion of a new user into the database.
- `test_user_info`: Checks information for a user who hasn't filled in all fields.

#### UI Tests
- `test_check_incorrect_username_page_object`: Tests inputting incorrect data for GitHub website authorization.
- `test_check_incorrect_track_number`: Verifies entering an incorrect tracking number on the Nova Global website and checks the page title.


## Important
Before running the tests, ensure you have the necessary permissions, correctly configured environment variables, and accurate data to execute the tests.

Exercise caution and make sure you are performing tests on a testing environment or with proper information to resolve issues and prevent data loss.
