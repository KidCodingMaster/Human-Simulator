from rich.prompt import Prompt
from rich import print
import time
from utils.shop import render_shop, import_shop_items
from utils.jobs import import_jobs
from utils.cli import enter_continue
import os
import random


class Player:
    def __init__(self):
        self.money = 0
        self.experience = []
        self.item = []
        self.job = None

    def work(self):
        jobs = import_jobs()
        
        for i in range(3):
            time.sleep(3.33333333)
            print("Working...")

        final_salary = round(jobs[self.job]["salary"] * random.uniform(1.5, 1.0))
        
        os.system('clear')

        self.money += final_salary
        print("You got " + str(final_salary))

    def buy_shop(self, item):
        os.system("clear")

        if self.money < shop_items_dict[item]:
            print("\nNot enough money to buy")
            enter_continue()
            return

        self.item.append(item)
        print(f"\n[bold cyan]{item} bought!")


def start_shop():
    item_to_buy = render_shop()

    player.shop(item_to_buy)


def start_work():
    os.system("clear")

    if player.job == None:
        print("\nYou have no job... You can go to try job to try out for a job.")
        enter_continue()
        return

    player.work()


def run():
    choices = {"shop": start_shop, "work": start_work}

    while True:
        cmd = Prompt.ask("What do you want to do? ", choices=list(choices.keys()))

        choices[cmd]()


if __name__ == "__main__":
    player = Player()
    shop_items_dict = import_shop_items()
    shop_items = list(import_shop_items().keys())
    run()
