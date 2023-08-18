import random


def a():
    list_of_alpha = "abcdefghijklmopqrstuvwxyzABCDEFGHIJKLMOPQRSTUVWXYZ"
    list = [i for i in range(8,11)]

    arr = [ random.choice(list_of_alpha) for _ in range(0,random.choice(list))]
    strin = ""
    sr = strin.join(arr)


    invite = f'https://discord.com/invite/{sr}'

    return invite
