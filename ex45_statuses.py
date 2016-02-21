from sys import exit


def death(scene_name):
    quips = {
         "Gate": "你的行动太过鲁莽了！",
         "AdytumDoor1": "想法太天真！",
         "AdytumDoor2": "愚蠢的人才会重复使用同一战术！",
         "Adytum": "好好练一练魔鬼的步法吧0.0..."
     }
    print(quips[scene_name])
    exit(-1)


def finished():
    print("Congratulation! You are the hero. You save the world!")
    exit(0)
