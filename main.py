from utils.shop import render_shop, import_shop_items

class Player:
    def __init__(self):
        self.money = 0
        self.experience = []

import_shop_items()
print(render_shop())
