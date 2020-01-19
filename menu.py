def get_choice(*args):
    while True:
        user_choice = input("Enter something: ").strip()

        if user_choice in args:
            return user_choice

        print(f"Bad choice {user_choice}; try again")
