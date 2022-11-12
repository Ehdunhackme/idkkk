from immutables import *

os.system("")  # Making terminal understand ANSI sequences


def addPoints():
    points = 30 / (_iter + 1)
    cprint("Yes that's correct! You got " + str(points) + " points", "green")
    if logged_in:
        points += user_info["points"]
        mongo.update_one({"_id": user_info["_id"]}, {"points": points})


def move_elements():
    global num_of_elements, elements_white, elements_red
    num_of_elements = num_of_elements // 2
    # move 26-num_of_elements to red list
    # This must be len(elements) because white will eventually be lower than red, resulting in negative number
    number_supposed_in_red = len(elements) - num_of_elements
    number_to_move = number_supposed_in_red - len(elements_red)
    moveToRed = random.sample(elements_white, k=number_to_move)
    if moveToRed:
        for a in range(len(moveToRed)):
            elements_white, elements_red = moveElements(elements_white, elements_red, moveToRed[a])
            # This implementation is used due to being unable to reference variables in python

        if element_to_guess in elements_red:
            move_again = random.choice(elements_white)
            # Deletes from red and appends to white (element to be guessed)
            elements_red, elements_white = moveElements(elements_red, elements_white, element_to_guess)
            # Deletes from white and appends to red (element chosen to be swapped)
            elements_white, elements_red = moveElements(elements_white, elements_red, move_again)

    # Hotfix for bug #3
    elements_white.insert(randint(0, len(elements_white)), elements_white.pop())


if __name__ == "__main__":
    global elements_white, elements_red, logged_in
    login = input("Do you wish to login: ").lower()

    if login in login_prompts_yes:
        result, user_info = UserAuth().run("kpkad", "users")
        if result:
            logged_in = True
            print("Login success")
            time.sleep(1)
            print("\n"*y_height)

    num_of_elements = len(elements) * 2
    element_to_guess = random.choice(elements)
    _iter = 0
    _end = False
    retry = False

    while not _end and _iter < 4:
        try:
            print("\n\n")
            if not retry:
                move_elements()

            cprint(f"{underline_ansi_start}\nElements that you can choose{underline_ansi_end}", "blue")
            print_colored_list(organise_elements(elements_white, 7, False), "green")
            cprint(f"{underline_ansi_start}\nElements that you can't choose{underline_ansi_end}", "blue")
            print_colored_list(organise_elements(elements_red, 7, False), "red")

            print(f"\nThis is your {_iter + 1}th try! Good luck. Element is {element_to_guess}\n")
            choice_of_element = input("Choose an element in green: ").lower()
            _iter += 1
            retry = False

            if choice_of_element == element_to_guess.lower():  # Check if wrong or right
                addPoints()
                _end = True
                break

            if choice_of_element.capitalize() not in elements_white:
                print("Sorry that's not in the selectable elements. Please try again...")
                _iter -= 1
                retry = True
            else:
                print_end_none("Sorry that's wrong. Try again :'(")
        except Exception as e:
            print_end_none("Error detected - ")
            print(e)

    if not logged_in and _end:
        print("Since you didn't create an account no points are stored for you...")
    if not _end:
        print(f"Game ended. The answer was {element_to_guess}")

    print("\n")
