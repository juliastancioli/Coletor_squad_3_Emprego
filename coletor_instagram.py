#>>> pip install instaloader
import instaloader, time, datetime
import MargemDeTempoHashtag
from datetime import date

if __name__ == '__main__':

	# >> Para ver os atributos de cada classe e ter mais informacoes: https://instaloader.github.io/as-module.html
	loader = instaloader.Instaloader()

	# O interactive_login recebe username como parâmetro, necessário para alguns processos e para a coleta de perfis privados.
	# A senha deve ser preenchida no terminal.

	loader.interactive_login('--usuario--')

	# Coleta de info de um perfil
	'''
	username = "--usuario--"
	profile = instaloader.Profile.from_username(loader.context, username)
	user_id = profile.userid
	full_name = profile.full_name
	print('Name: ' + str(full_name) + '  --  ID: ' + str(user_id))
	print('Private? ' + str(profile.is_private))
	print('\n')
	'''

	#Download da imagem de perfil do usuário
	'''
	loader.download_profilepic(profile)
	'''

	#Coleta highlights de um perfil
	# >> É necessário estar logado no Instagram
	'''
	for highlight in loader.get_highlights(profile):
		for item in highlight.get_items():
			loader.download_storyitem(item, '{}/{}'.format(highlight.owner_username, highlight.title))
	'''

	# Coleta posts de um perfil
	# >> É necessário seguir o perfil privado para coletar essas informações
	'''
	posts = profile.get_posts()

	# Com um post voce pode coletar os comments e com um comment, os replies dele
	
	counter = 1
	for post in posts:
	
		print('Post ' + str(counter))
		loader.download_post(post, username)
		print(post.caption)
		print(post.owner_profile)
		print('Data de postagem: ' + str(post.date_local))
		print('tagged users: '+str(post.tagged_users))
		
		comments = post.get_comments()

		for comment in comments:
			print(comment.text)
			replies = comment.answers

			for reply in replies:
				pass

		print('\n')
		counter += 1
    '''

	# Coleta da rede do perfil
	# >> É necessário estar logado no Instagram
	'''
	loader.login("usuario","password")
	followers = profile.get_followers()
	followees = seed_user_profile.get_followees()

	for follower in followers:
		pass
	'''

	# Coleta de stories de um perfil
	# >> É necessário estar logado no Instagram
	'''
	loader.download_stories(userids=[profile.userid], filename_target='{}'.format(profile.username), fast_update=True)
	'''

	# Coleta info de uma hashtag
	MargemDeTempoHashtag.ColetaHashtag(loader)
