import instaloader, time, datetime, csv, re
from datetime import date

# função que cria a data :)
def criar_data(periodo):
    a,m,d = input("Digite uma data para ser o"+periodo+"da pesquisa(aaaa-mm-dd): ").split("-")
    return datetime.datetime(int(a),int(m),int(d))   



# função que avalia se o coronavirus está relacionado ao post
def post_relacionado(comments, caption):
    corona_list = ['corona', 'coronavirus', 'coronavírus', 'covid', 'covid19', 'coronga', 'vírus', 'doença']

    for comment in comments:
        word_list = re.sub("[^\w]", " ",  comment.text).split()
        #words_list = list_words(comment.text)
        #print(comment.text)
        print(word_list)



#função principal do módulo
def coleta_hashtag (loader):
	# Coleta info de uma hashtag baseado em uma margem de tempo escolhida pelo usuario
	
	tag = str(input("Digite a palavra que deve ser buscada: ")) #Faz a coleta de qual hashtag deve ser buscada
	cont_max = int(input("Quantos posts devem ser buscados (caso 0 será feita a coleta total no periodo de tempo): ")) #Coleta o número máximo de posts que devem ser buscados

    # definição do periodo de tempo:
	data_ini = criar_data(' inicio ')
	data_fin = criar_data(' final ')

    #criação e informações da hashtag:
	hashtag = instaloader.Hashtag.from_name(loader.context, tag)
	tag_id = hashtag.hashtagid
	print('Hashtag: #' + str(hashtag.name) + '  --  ID: ' + str(tag_id))
	print('Posts count: ' + str(hashtag.mediacount))
	print('\n')

	if cont_max == 0:
		cont_max = hashtag.mediacount

	#Faz download dos posts associados com a hashtag
	cont = 0
	filtered_posts = filter(lambda p: data_fin <= p.date <= data_ini, hashtag.get_posts()) #Filtra os posts na margem de tempo
	with open(tag+'.csv', 'w', encoding='utf-8', newline='') as file:
		writer = csv.writer(file)
		writer.writerow(["Usuario", "Data", "Likes", "Comentarios", "Texto", "Hashtags", "Patrocinado", "Usuarios marcados"])
		for post in filtered_posts:
			print(post.date)
			writer.writerow([post.owner_username, post.date, post.likes, post.comments, post.caption, post.caption_hashtags, post.is_sponsored, post.tagged_users]) #Coleta os dados referentes as colunas do arquivo csv
			cont += 1
			comentarios = post.get_comments()
			if post_relacionado(comentarios, post.caption):
				loader.download_post(post, target="#"+hashtag.name) #Faz o download dos itens do post
			if cont == cont_max or post.date < data_fin: #Caso o número necessário de posts seja coletado ou não exista mais posts nessa margem de tempo, finaliza o programa
				print("Finalizado!!")
				break
