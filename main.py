from rich.prompt import Prompt
import time
from utils.shop import render_shop, import_shop_items

class Player:
    def __init__(self):
        self.money = 0
        self.experience = []

    def work(job):
        time.sleep(3.33333333)
        print('Working...')

def run():
    choices = ['shop']

    while True:
        cmd = Prompt.ask("What do you want to do? ", choices=choices)

run()