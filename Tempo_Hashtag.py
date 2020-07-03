import instaloader, time, datetime, csv
from datetime import date

def ColetaHashtag (loader):
		# Coleta info de uma hashtag
	
		tag = str(input("Digite a palavra que deve ser buscada: ")) #Faz a coleta de qual hashtag deve ser buscada
		a,m,d = input("Digite uma data para ser o inicio da pesquisa(aaaa-mm-dd): ").split("-")
		data_ini = datetime.datetime(int(a),int(m),int(d))
		a,m,d = input("Digite uma data para ser o fim da pesquisa(aaaa-mm-dd): ").split("-")
		data_fin = datetime.datetime(int(a),int(m),int(d))
		hashtag = instaloader.Hashtag.from_name(loader.context, tag)
		tag_id = hashtag.hashtagid
		print('Hashtag: #' + str(hashtag.name) + '  --  ID: ' + str(tag_id))
		print('Posts count: ' + str(hashtag.mediacount))
		print('\n')
		#Faz download dos posts associados com a hashtag
		with open(tag+'.csv', 'w', newline='') as file:
			writer = csv.writer(file)
			writer.writerow(["Likes", "Comentários", ""])
			for post in hashtag.get_posts():
				if (post.date <= data_ini) and (post.date >= data_fin): #Verifica se o post está na margem de tempo desejada
					print(post.date)
					writer.writerow([post.likes, post.comments, post])
				#loader.download_post(post, target="#"+hashtag.name) #Faz o download dos itens do post
			#elif post.date  < data_fin: #Caso não haja mais posts neste mês finaliza
				#print("finalizado" + teste) 