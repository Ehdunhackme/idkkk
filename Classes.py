import time
import pymongo
from hashlib import md5
from termcolor import cprint
from ursina import Entity, color, Vec3, Animation


class Card(Entity):
    def __init__(self, **kwargs):
        super().__init__(model="quad")

        self.color = color.gray
        self.scale = Vec3(6.5, 9, 1)

        for attr, value in kwargs.items():
            setattr(self, attr, value)


class MongoDB:
    HOST = "mongodb://localhost:27017/"
    DB = None
    COLLECTION = None
    client = None

    def __init__(self, database, collection, host = ""):
        if host != "":
            self.HOST = host

        self.client = pymongo.MongoClient(self.HOST)
        self.DB = self.client[database]
        self.COLLECTION = self.DB[collection]

    def insert_db(self, data: dict):
        return self.COLLECTION.insert_one(data)

    def find_one(self, data: dict):
        return self.COLLECTION.find_one(data)

    def update_one(self, _filter: dict, updatedValues: dict):
        return self.COLLECTION.update_one(_filter, {'$set': updatedValues})


class UserAuth:
    def run(self, database, collection):
        while True:
            # print("\n"*100)
            username = input("Your username: ")
            password = input("Your password: ")  # TODO: Change to pwinput
            hashed_password = md5(password.encode()).hexdigest()
            result = MongoDB(database, collection).find_one({"username": username})

            try:
                if result["password"] == hashed_password:
                    return True, result
                else:
                    print("Password is wrong")  # TODO: Add number of tries
            except TypeError:
                print("Username is wrong")


def loadingText(text: str = "Loading", followingChar: str = ".", iterations: int = 10, sleep: float = 0.3):
    for i in range(iterations):
        print(text + followingChar*i, end="\r")
        time.sleep(sleep)


def moveElements(originalList: list, updatedList: list, objectToMove):
    if objectToMove not in originalList:
        var_name = get_var_name(originalList, locals())
        raise ValueError(
            f"Object '{objectToMove}' to be moved is not in original list '{originalList}' called '{var_name}'")

    originalList.remove(objectToMove)
    updatedList.append(objectToMove)

    return originalList, updatedList


def get_var_name(obj, namespace):
    return [name for name in namespace if namespace[name] is obj]


def organise_elements(elements: list, objPerLine: int, printMessages: bool = True):
    a = 0  # Element index
    returns = []

    while a < len(elements):
        returned_string = ""
        for i in range(objPerLine):
            try:
                returned_string += (str(elements[a]) + " ")
                a += 1
            except IndexError:
                pass

        if printMessages:
            print(returned_string)

        returns.append(returned_string)

    return returns


def print_colored_list(items: list, color: str, attrs: list = []):
    for i in items:
        cprint(i, color=color, attrs=attrs)


def play_animation(name, fps, loop, autoplay, scale, position, to_disable):
    hide_entities(to_disable)
    animation = Animation(name, fps=fps, loop=loop, autoplay=autoplay, scale=scale, position=position)
    animation.sequence.auto_destroy = True


def hide_entities(entities: list):
    for i in entities:
        i.enabled = False


def show_entities(entities: list):
    for i in entities:
        i.enabled = True
