import webbrowser

webbrowser.open('https://www.instagram.com/accounts/login/', new=2, autoraise=True)


def get_login():
    user_name = input("Please provide your Instagram account name: ")
    password = input("Please provide your Instagram password: ")
