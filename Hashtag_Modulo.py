import instaloader, time, datetime, csv, re

def kmp(t, p):
	"""return all matching positions of p in t"""
	next = [0]
	j = 0
	for i in range(1, len(p)):
		while j > 0 and p[j] != p[i]:
			j = next[j - 1]
		if p[j] == p[i]:
			j += 1
		next.append(j)
	# the search part and build part is almost identical.
	ans = []
	j = 0
	for i in range(len(t)):
		while j > 0 and t[i] != p[j]:
			j = next[j - 1]
		if t[i] == p[j]:
			j += 1
		if j == len(p):
			ans.append(i - (j - 1))
			j = next[j - 1]
	return ans



# função que cria a data :)
def criar_data(periodo):
	a,m,d = input("Digite uma data para ser o"+periodo+"da pesquisa(aaaa-mm-dd): ").split("-")
	return datetime.datetime(int(a),int(m),int(d))   



# função que avalia se o coronavirus está relacionado ao post
def comentario_relacionado(comments):
	corona_list = ["coron", "covid", "quarentena", "homeoffice", "pandemia"]
	for comment in comments:
		for x in corona_list:
			string = comment.text.replace(" ", "")
			if kmp(string,x) != []:
				return True
	return False

def texto_relacionado(caption):
	corona_list = ["covid", "corona", "doença", "quarentena", "coronga", "virus", "pandemia"]
	for x in corona_list:
		string = caption.replace(" ", "")
		if kmp(string,x) != []:
			return True
	return False


#função principal do módulo
def coleta_hashtag(loader):
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

	#filtra os emojis
	emoji_pattern = re.compile("["
		u"\U0001F600-\U0001F64F"  # emoticons
		u"\U0001F300-\U0001F5FF"  # symbols & pictographs
		u"\U0001F680-\U0001F6FF"  # transport & map symbols
		u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
		u"\U00002702-\U000027B0"
		u"\U00002702-\U000027B0"
		u"\U000024C2-\U0001F251"
		u"\U0001f926-\U0001f937"
		u"\U00010000-\U0010ffff"
		u"\u2640-\u2642" 
		u"\u2600-\u2B55"
		u"\u200d"
		u"\u23cf"
		u"\u23e9"
		u"\u231a"
		u"\ufe0f"  # dingbats
		u"\u3030"
							"]+", flags=re.UNICODE)

	#Cria os arquivos csv
	cont = 0
	filtered_posts = filter(lambda p: data_fin <= p.date <= data_ini, hashtag.get_posts()) #Filtra os posts na margem de tempo
	with open(tag+'.csv', 'w', encoding='utf-8', newline='') as file:
		writer = csv.writer(file)
		writer.writerow(["Usuario", "Data", "Likes", "Comentarios", "Texto", "Hashtags", "Patrocinado", "Usuarios marcados", "Comentário Rel.", "Texto Rel."])
		for post in filtered_posts:
			if post.is_video == False and post.caption != None:
				print(post.date)
				cont += 1
				comentarios = post.get_comments()
				writer.writerow([post.owner_username, post.date, post.likes, post.comments,emoji_pattern.sub(r'', post.caption), post.caption_hashtags, post.is_sponsored, post.tagged_users, comentario_relacionado(comentarios), texto_relacionado(post.caption)]) #Coleta os dados referentes as colunas do arquivo csv
				if post.owner_profile.is_business_account: 
					with open("business_names"+'_'+tag+'.csv', 'a', encoding='utf-8', newline='') as arq:
						bus = csv.writer(arq)
						bus.writerow([post.owner_username,post.owner_profile.business_category_name])
			if cont == cont_max or post.date < data_fin: #Caso o número necessário de posts seja coletado ou não exista mais posts nessa margem de tempo, finaliza o programa
				print("Finalizado!!")
				break
