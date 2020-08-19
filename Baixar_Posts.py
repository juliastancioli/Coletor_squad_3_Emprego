import instaloader, time, datetime, csv
import Hashtag_Modulo, Perfil_Modulo
from datetime import date

if __name__ == '__main__':

    # incialização e login---------
    loader = instaloader.Instaloader()
    user_login = str(input("Instagram login: "))
    loader.interactive_login(user_login)
    #---------------------------- 
    modo = str(input("Qual modo você deseja utilizar (p ou h): "))
    if modo == "h":
        Hashtag_Modulo.coleta_hashtag(loader) #função de coleta da tag
    if modo == "p":
        Perfil_Modulo.coleta_perfil(loader) #função de coleta do perfil

