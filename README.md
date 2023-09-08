# Instagram Unfollower Tracker

## Description
Instagram Unfollower Tracker is a Python web scraper application utilizing the Selenium library. It allows users to log into their Instagram profiles, retrieve their followers and following lists, and identify those who do not reciprocate. Additionally, users can unfollow non-reciprocating accounts or follow accounts that the user is not currently following back.

## Benefits of the Project
By using Instagram Unfollower Tracker, you can enjoy the following benefits:

- Quickly and easily list your followers and accounts you are following.
- Identify accounts that do not reciprocate by not following you back or vice versa.
- Based on this information, you can perform follow or unfollow operations.
- Effectively manage your account.

## Requirements
To run this project, you'll need the following dependencies:

- [Selenium](https://pypi.org/project/selenium/): A web testing framework.
- [Getpass](https://docs.python.org/3/library/getpass.html): A library for securely entering passwords.

Make sure to have these dependencies installed before running the project.

## Usage
- Ensure you have the required dependencies installed (`selenium`, `getpass`).
- Run `instagramBot.py`.
- Follow these steps to interact with your Instagram account:

  1. **Log In**: Enter your Instagram username and password when prompted.
  2. **Main Menu**: Choose an option from the main menu by entering the corresponding number:
      - `1` - Find Followers: Retrieves your followers.
      - `2` - Find Followings: Retrieves accounts you are following.
      - `3` - Users You're Not Following Back: Identifies accounts that you are not following back.
      - `4` - Users Not Following You Back: Identifies accounts that are not following you back.
      - `n` - Exit: To exit the program.

  3. **Following Steps for Option 3 (Users You're Not Following Back)**:
      - The program will identify users you are not following back.
      - You will be presented with a list of these users.
      - Choose the users you want to follow back by entering their numbers (e.g., `1,3,4`) separated by commas.

  4. **Following Steps for Option 4 (Users Not Following You Back)**:
      - The program will identify users who are not following you back.
      - You will be presented with a list of these users.
      - Choose the users you want to unfollow by entering their numbers (e.g., `1,3,4`) separated by commas.

  5. Follow the on-screen instructions to complete the selected action.
 

## Usage Scenarios

### Scenario 2: Finding Accounts You're Not Following Back
1. Press `3` on the main menu to find accounts you're not following back.
2. The list of these accounts will be displayed on the screen.
3. Enter the numbers of the accounts you want to follow back, separated by commas (e.g., `1,3,4`).

### Scenario 3: Following or Unfollowing
1. Press `4` on the main menu to find accounts that you're not following back.
2. The list of these accounts will be displayed on the screen.
3. Enter the numbers of the accounts you want to follow or unfollow, separated by commas (e.g., `1,3,4`).

### Scenario 4: Exiting the Program
1. Press `n` on the main menu to close the program.
