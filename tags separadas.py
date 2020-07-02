from datetime import datetime
import instaloader

#função que olha se uma tag determinada tambem está no post
def has_word(hashtags, word):
    for tagg in hashtags:
        if tagg == word:
            return True
    return False

if __name__ == '__main__':


    SINCE = datetime(2020, 1, 1)
    print(SINCE)

    loader = instaloader.Instaloader()
    loader.interactive_login('vinn_correia')

    username = 'vinn_correia'
    
    tag = "demissão"
    hashtag = instaloader.Hashtag.from_name(loader.context, tag)
    tag_id = hashtag.hashtagid
    print('Hashtag: #' + str(hashtag.name) + '  --  ID: ' + str(tag_id))
    print('Posts count: ' + str(hashtag.mediacount))
    print('\n')

    posts = hashtag.get_posts()
    
    #loader.posts_download_loop(posts, target="#"+hashtag.name, fast_update=False, post_filter=callable[posts, ], max_count=30, total_count=None)

    count = 0
    #loop que passa por cada post
    for post in posts:
        #Somente a cima da data estipulada:
        if post.date_local > SINCE:
            #pega uma lista com todas as hashtags presentes no post:
            hashtag_list = post.caption_hashtags
            #olha se tem a tag emprego nas publicações da tag demissão:
            if has_word(hashtag_list, "emprego"):
                loader.download_post(post, target="#"+hashtag.name+"+emprego")
            else:
                loader.download_post(post, target="#"+hashtag.name+"-emprego")
            count -= -1
            if count == 50:
                break
        else:
            break
    
    #eu tava pensando e é melhor a função la de cima, em vez de retornar bool,
    #retornar uma string com o nome da pasta que vai entrar, dessa forma a gente
    #só coloca ali a string no target
    #eu explico mal e não sei se ficou claro KKKKKKK
    #mas qqr coisa amanha eu mostro porces
    #té mais galera

