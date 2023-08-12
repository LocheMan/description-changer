import os
import sys
import json
import requests

from time import sleep
from pystyle import Anime, Center, Colors, Colorate, System, Cursor


watermark = '''██████╗ ██████╗ ██████╗ ███╗   ██╗
╚════██╗██╔══██╗╚════██╗████╗  ██║
 █████╔╝██║  ██║ █████╔╝██╔██╗ ██║
 ╚═══██╗██║  ██║ ╚═══██╗██║╚██╗██║
██████╔╝██████╔╝██████╔╝██║ ╚████║
╚═════╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═══╝'''

System.Size(80, 20)

Cursor.HideCursor()
space = ' ' * 73
System.Title(f'\u200b{space}Press ENTER to continue')
Anime.Fade(Center.Center(watermark), Colors.purple_to_blue, Colorate.Vertical, interval=0.100, enter=True)

Cursor.ShowCursor()
System.Title('\u200b Description Changer  /  UrPurchase  /  Par @.3D3N.')
System.Size(160, 40)


class Color:
    @staticmethod
    def compose(color):
        return f'\033[38;2;{color}m'

    red = compose('255;0;0')
    green = compose('0;255;0')
    blue = compose('0;0;255')

    white = compose('255;255;255')
    black = compose('0;0;0')
    gray = compose('150;150;150')

    yellow = compose('255;255;0')
    purple = compose('255;0;255')
    cyan = compose('0;255;255')

    orange = compose('255;150;0')
    pink = compose('255;0;150')
    turquoise = compose('0;150;255')

    light_gray = compose('200;200;200')
    dark_gray = compose('100;100;100')

    light_red = compose('255;100;100')
    light_green = compose('100;255;100')
    light_blue = compose('100;100;255')

    dark_red = compose('100;0;0')
    dark_green = compose('0;100;0')
    dark_blue = compose('0;0;100')


def start(token, descriptions, time, end):
    while True:
        for description in descriptions:
            response = requests.patch(
                "https://discord.com/api/v10/users/@me",
                headers={"Authorization": token, "Content-Type": "application/json"},
                json={"bio": description + end}
            )
            
            print(response.json())
            
            if response.status_code == 200: print(f"{Color.gray}[{Color.light_green}+{Color.gray}] {Color.white}Description changé")
            else: print(f"{Color.gray}[{Color.red}-{Color.gray}] {Color.white}Erreur lors de la requête:", response.json())
                
            sleep(time)
            

os.system('cls')
print(' ')

def help():
    print(f" {Color.turquoise}help      {Color.cyan}Besoin d'aide\n" +
          f" {Color.turquoise}start     {Color.cyan}Lancer le script\n" +
          f" {Color.turquoise}config    {Color.cyan}Configurer le script\n" +
          f" {Color.turquoise}clear     {Color.cyan}Effacer les données à l'écran\n" +
          f" {Color.turquoise}exit      {Color.cyan}Fermer le programme\n")

while True:
    commande = input(f' {Color.green}┌──({Color.light_blue}root@server-cloner{Color.green})-[{Color.white}~{Color.green}]\n' +
                     f' {Color.green}└─$ {Color.white}')
    print(' ')
    if commande.startswith('help'):
        help()
        
    elif commande.startswith('config'):
        os.system(f'notepad "{os.getcwd()}\config.json"')
        print(f' {Color.green}Ok.\n')
        
    elif commande.startswith('start'):
        with open('config.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
        start(data['token'], data['descriptions'], data['time'], data['end'])
    
    elif commande.startswith('clear'):
        os.system('cls')
        print('')
    
    elif commande.startswith('exit'):
        print(f' {Colors.orange}Fermeture du programme...')
        sys.exit()
    
    else:
        print(f' {Color.red}Commande inconnue\n')
