from imports import *

os.system("")  # Making terminal understand ANSI sequences

x_length, y_height = shutil.get_terminal_size((80, 20))
login_prompts_yes = ["y", "yes", "ye", "ys", "1", "true"]
underline_ansi_start, underline_ansi_end = "\033[4m", "\033[0m"
logged_in = False
mongo = MongoDB("kpkad", "users")
user_info = {}

with open("elements.json") as f:
    contents = f.read()

elements = list(json.loads(contents))
elements_white = copy(elements)
elements_red = []

if __name__ == "__main__":
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

    for i in range(4):
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

        print(f"{underline_ansi_start}Elements that you can choose{underline_ansi_end}".center(x_length))
        print_colored_list(organise_elements(elements_white, 7, False), "white")
        print(f"{underline_ansi_start}Elements that you can't choose{underline_ansi_end}".center(x_length))
        print_colored_list(organise_elements(elements_red, 7, False), "red")

        print(f"This is your {i+1}th try! Good luck. Element is {element_to_guess}\n")
        choice_of_element = input("Choose an element in white: ").lower()

        # Check if wrong or right
        if choice_of_element == element_to_guess.lower():
            points = 30 / (i + 1)
            print("Yes that's correct! You got " + str(points) + " points")
            if logged_in:
                points += user_info["points"]
                mongo.update_one({"_id": user_info["_id"]}, {"points": points})
            break

        if choice_of_element not in elements_white:
            print("Sorry that's not in the selectable elements. Please try again...")
        else:
            print("Sorry that's wrong. Try again :'(")

    if not logged_in:
        print("Since you didn't create an account no points are stored for you...")

