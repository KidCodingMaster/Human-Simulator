from rich.prompt import Prompt
from rich import print
import time
from utils.shop import render_shop, import_shop_items
from utils.cli import enter_continue
import os


class Player:
    def __init__(self):
        self.money = 12345678909876321
        self.experience = []
        self.item = []

    def work(job):
        time.sleep(3.33333333)
        print("Working...")

    def shop(self, item):
        os.system('clear')

        if self.money < shop_items_dict[item]:
            print("\nNot enough money to buy")
            enter_continue()
            return
        
        self.item.append(item)
        print(f'\n[bold cyan]{item} bought!')


def start_shop():
    item_to_buy = render_shop()

    player.shop(item_to_buy)


def run():
    choices = {"shop": start_shop}

    while True:
        cmd = Prompt.ask("What do you want to do? ", choices=list(choices.keys()))

        choices[cmd]()


if __name__ == "__main__":
    player = Player()
    shop_items_dict = import_shop_items()
    shop_items = list(import_shop_items().keys())
    run()
