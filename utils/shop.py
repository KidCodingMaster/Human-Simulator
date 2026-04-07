import json
from rich.prompt import Prompt


def import_shop_items():
    with open("shop.json") as f:
        return json.load(f)


def render_shop():
    shop_items = list(import_shop_items().keys())
    
    return Prompt.ask("What do you want to buy? ", choices=shop_items, case_sensitive=False)
