import time

from ursina import *
from Classes import Card, play_animation, hide_entities, show_entities

window.title = "KPKAD T3"

app = Ursina(fullscreen=True, show_ursina_splash=False)


def update():
    camera.position += (0, held_keys['z'] * time.dt * 30, 0)
    camera.position -= (0, held_keys['x'] * time.dt * 30, 0)


def show_supply():
    scene.clear()
    btn = Button('Gacha Now!', color=color.gold, text_color=color.black, scale=(.4, .2))
    btn.on_click = Func(show_gacha_animation, [btn])


def main_menu():
    scene.clear()
    # Setting card backgrounds
    for card_position in main_menu_card_positions:
        Card(position=card_position)

    # Setting icons
    for name, icon_position in main_menu_card_icon.items():
        Card(position=icon_position, texture=f"assets/{name}", scale=(3, 3, 1))

    # Setting buttons
    for btn_text, metadata in main_menu_buttons.items():
        button = Button(text=btn_text, radius=0, scale=(0.4, 0.1, 0), color=color.black, position=metadata[0])
        try:
            button.on_click = metadata[1]
        except IndexError:
            ...
    
    settings = Button(radius=.5, scale=.1, icon="assets/settings.png", position=(0, -.43), color=color.rgba(0, 0, 0, 0))
    settings.on_click = test


def test():
    print("Test")


def show_gacha_animation(to_hide):
    hide_entities(to_hide)
    box = Entity(model="cube", color=color.white, scale=(5, 5))
    box.shake(2, 10)
    box.fade_out(duration=3)
    print(box.visible)


main_menu_card_positions = [(-7, 0, 1), (0, 0, 1), (7, 0, 1)]
main_menu_card_icon = {"calcium": (-6.8, 0.5, 0), "attack": (0, 0.5, 0), "crate": (6.8, 0.5, 0)}
main_menu_buttons = {
    "Profile": [(-.55, -.25, 0)],
    "Attack": [(0, -.25, 0)],
    "Supply": [(.55, -.25, 0), Func(show_supply)]
}

window.fps_counter.enabled = True
window.exit_button.visible = False
window.cog_button.enabled = False
mouse.visible = False
cursor = Cursor(texture="cursor/normal.png", scale=.03, eternal=True)
camera.position = Vec3(0, 0, -30)

main_menu()
app.run()
