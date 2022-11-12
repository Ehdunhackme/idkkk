from imports import *

x_length, y_height = shutil.get_terminal_size((80, 20))
underline_ansi_start, underline_ansi_end = "\033[4m", "\033[0m"
login_prompts_yes = ["y", "yes", "ye", "ys", "1", "true", "es", "s"]
mongo = MongoDB("kpkad", "users")
logged_in = False
user_info = {}

with open("elements.json") as f:
    contents = f.read()

elements = list(json.loads(contents))
elements_white = copy(elements)
elements_red = []