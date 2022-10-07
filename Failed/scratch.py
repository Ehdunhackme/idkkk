# from ursina import *
#
# app = Ursina()
# class MainMenu(Entity):
#     def __init__(self, **kwargs):
#         super().__init__(parent=camera.ui, ignore_paused=True)

#         self.main_menu = Entity(parent=self, enabled=True)
#         self.secondary_menu = Entity(parent=self, enabled=False)

#         self.background = Sprite('shore', color=color.black, z=1)

#         Text("Hello world", parent=self.main_menu, origin=(0, 0))

#         def switch(first, second):
#             first.enable()
#             second.disable()

#     def input(self, key):
#         if key == "escape" and self.main_menu.enabled:
#             application.quit()
#         elif self.secondary_menu.enabled and key == "escape":
#             self.main_menu.enable()
#             self.secondary_menu.disable()


# main_menu = MainMenu()

# button = Button(text="Hello", color=color.gold, radius=0.5, scale=.3)
# button.position = (.1, .1, .1)

# mongo = MongoDB("kpkad", "users")
# hashed_password = md5("a".encode()).hexdigest()
# _id = ObjectId('6315e75de998628cbbd234d0')
# # mongo.insert_db({"username": "lyx", "password": hashed_password, "points": 0, "characters": []})
# result = mongo.update_one({"_id": _id}, {"points": 30})
# pprint.pprint(result)

# with open("elements.json") as f:
#     contents = f.read()
#
# elements = list(json.loads(contents))
#
# organised_elements = organise_elements(elements, 7, False)
# print_colored_list(organised_elements, "red")

# from ursina import *
#
# # create a window
# app = Ursina()
#
# player = Entity(model='quad', color=color.orange, scale_y=1)
#
# # create a function called 'update'.
# # this will automatically get called by the engine every frame.
#
#
# def update():
#     player.x += held_keys['d'] * time.dt * 2
#     player.x -= held_keys['a'] * time.dt * 2
#
#     player.y += held_keys['w'] * time.dt * 2
#     player.y -= held_keys['s'] * time.dt * 2
#
# # this part will make the player move left or right based on our input.
# # to check which keys are held down, we can check the held_keys dictionary.
# # 0 means not pressed and 1 means pressed.
# # time.dt is simply the time since the last frame. by multiplying with this, the
# # player will move at the same speed regardless of how fast the game runs.
#
#
# def input(key):
#     if key == 'space':
#         player.y += 1
#         invoke(setattr, player, 'y', player.y-1, delay=.25)
#
#
# # start running the game
# app.run()

# player.rotation_x += held_keys['r'] * time.dt * 100
# player.rotation_y += held_keys['q'] * time.dt * 100
# player.rotation_y -= held_keys['e'] * time.dt * 100
# camera.position += (0, 0, held_keys['z'] * time.dt * 30)
# camera.position -= (0, 0, held_keys['x'] * time.dt * 30)

# Text.size = 0.05
# Text.default_resolution = 1080 * Text.size
# info = Text(text="A powerful waterfall roaring on the mountains")
# info.x = -0.5
# info.y = 0.4
# info.background = True
# info.visible = False        # Do not show this text
#
#
# def update():
#     if held_keys['a']:
#         ...
#
#
# app.run()

