import instaloader, time, datetime, csv
import hashtag
from datetime import date

if __name__ == '__main__':

    # incialização e login---------
    loader = instaloader.Instaloader()
    print('Instagram login:', end=' ')
    user_login = input()
    loader.interactive_login(user_login)
    #---------------------------- 

    hashtag.coleta_hashtag(loader) #função de coleta da tag

