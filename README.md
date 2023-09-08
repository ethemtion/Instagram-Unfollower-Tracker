# Instagram Unfollower Tracker

## Description
Instagram Unfollower Tracker is a Python web scraper application utilizing the Selenium library. It allows users to log into their Instagram profiles, retrieve their followers and following lists, and identify those who do not reciprocate. Additionally, users can unfollow non-reciprocating accounts or follow accounts that the user is not currently following back.

## Usage
- Ensure you have the required dependencies installed (`selenium`, `getpass`).
- Run `instagramBot.py`.
- Follow these steps to interact with your Instagram account:

  1. **Log In**: Enter your Instagram username and password when prompted.
  2. **Main Menu**: Choose an option from the main menu by entering the corresponding number:
      - `1` - Find Followers: Retrieves your followers.
      - `2` - Find Followings: Retrieves accounts you are following.
      - `3` - Users Not Following You Back: Identifies accounts that are not following you back.
      - `4` - Users You're Not Following Back: Identifies accounts that you are not following back.
      - `n` - Exit: To exit the program.

  3. **Following Steps for Option 3 (Users Not Following You Back)**:
      - The program will identify users who are not following you back.
      - You will be presented with a list of these users.
      - Choose the users you want to follow back by entering their numbers (e.g., `1,3,4`) separated by commas.

  4. **Following Steps for Option 4 (Users You're Not Following Back)**:
      - The program will identify users you are not following back.
      - You will be presented with a list of these users.
      - Choose the users you want to start following by entering their numbers (e.g., `1,3,4`) separated by commas.

  5. Follow the on-screen instructions to complete the selected action.
 

## Usage Example
```python
instagram = Instagram()
instagram.login()
instagram.findFollowers()
instagram.findFollowings()

# Use the menu to perform actions on your Instagram account
while True:
    n = instagram.menu()
    match n:
        case "1":
            instagram.findFollowers()
        case "2":
            instagram.findFollowings()
        case "3":
            instagram.userNotFollowingBackMain()
        case "4":
            instagram.notFollowingUserBackMain()
        case "n":
            break
        case _:
            print("Invalid input. Please try again.")
            time.sleep(1.5)
