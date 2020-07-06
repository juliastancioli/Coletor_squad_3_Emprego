import instaloader, time, datetime, csv
import hashtag_modulo
from datetime import date

if __name__ == '__main__':

    # incialização e login---------
    loader = instaloader.Instaloader()
    user_login = str(input("Instagram login: "))
    loader.interactive_login(user_login)
    #---------------------------- 

    hashtag_modulo.coleta_hashtag(loader) #função de coleta da tag

