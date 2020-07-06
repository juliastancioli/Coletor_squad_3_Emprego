import instaloader, time, datetime, csv
import Hashtag_Modulo
from datetime import date

if __name__ == '__main__':

    # incialização e login---------
    loader = instaloader.Instaloader()
    user_login = str(input("Instagram login: "))
    loader.interactive_login(user_login)
    #---------------------------- 

    Hashtag_Modulo.coleta_hashtag(loader) #função de coleta da tag

