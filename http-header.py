"""
        API count exceeded - Increase Quota with Membership
        If you encounter an error (API count exceeded - Increase Quota with Membership)   you need a VPN
        creat by Amir Hossein Tadas & TAHA
"""
import os
import sys
import requests
from colorama import Fore

def __start__():
        try:
                print(Fore.LIGHTRED_EX+" [!] Enter The Domain\n")   
                print(Fore.RED+"\n [!] for exampel : test.com\n") 
                inp = input(Fore.RED+" ┌─["+Fore.LIGHTGREEN_EX+"tahat80"+Fore.BLUE+"/"+Fore.WHITE+"HTTP-Header"+Fore.RED+"""]
 └──╼ """+Fore.WHITE+">> ")
                result = requests.get('https://api.hackertarget.com/httpheaders/?q=' + inp).text
                print(Fore.LIGHTBLUE_EX+result)
                try:
                        input(Fore.RED+" [!] "+Fore.GREEN+"Back To Menu (Press Enter...) ")
                except:
                        print("")
                        sys.exit()  

        
        except:
                print("\nExit :)")



if __name__ == '__main__':
    while True:
        try:
            os.system('cls')
        except:
            os.system('clear')

        __start__()


# If you encounter an error (API count exceeded - Increase Quota with Membership)   you need a VPN
        
        
# creat by Amir Hossein Tadas & TAHA

# instagram = 

#             Taha_t_80



# You can get information such as HTTP Version, Server, Date, Content-Type, Transfer-Encoding, Vary, Expires, X-Frame-Options, Connection, P3P, Keep-Alive, X-DIS-Request-ID, Location, address, Cache-Control, etc.




