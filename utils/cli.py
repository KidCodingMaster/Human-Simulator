from rich.prompt import Prompt
import os

def enter_continue():
    Prompt.ask('Press [bold cyan]Enter[/] to progress')
    os.system('clear')