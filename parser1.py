# -*- coding: utf8 -*-
import requests , bs4 
from bs4 import BeautifulSoup




headers = {
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 OPR/68.0.3618.125"
    
}


choise0 = input('Приветствую Вас в программе , созданной для веб-скрапинга , а ели точнее - парсинга сайта с аниме-контентом (YummyAnime.com (Ссылка: https://yummyanime.club)) \nАвтор: tigerk00(https://github.com/tigerk00) \nЖелаю приятного пользования! \n1.Введите "new" , чтобы начать парсинг новинок на сайте \n2.Введите "updates" , чтобы увидеть обновления разных аниме(добавление новых серий , озвучки и т.д.) \n3.Введите "news" , чтобы увидеть новости и посты различных авторов на тему аниме. \n4.Введите "anons" , чтобы увидеть будущие анонсы \n5.Введите "video" , чтобы увидеть информацию о некоторых видео с аниме-тематикой \n6.Введите "top-serials" , чтобы увидеть топ аниме-сериалов. \n7.Введите "top-films" , чтобы увидеть топ полнометражных аниме фильмов \n8.Введите "catalog-anime"  , чтобы иметь возможность увидеть список аниме исходя из выбраного вами жанра \n9.Введите "ongoings" , чтобы увидеть список незавершенных аниме , серии которых еще выходят. \nВаш выбор :  ')


if choise0 == 'new':
    base_url  = 'https://yummyanime.club'
    with requests.Session() as s:
        response = s.get(base_url , headers = headers)
        html = response.text
        soup = BeautifulSoup(html , 'html.parser')
    
    all_new_anime_divs = soup.find_all('div' , {'class': 'preview-block'})    
    for new_anime in all_new_anime_divs:
        name  = new_anime.select_one('a.preview-title').text
        print('[*] ' + name)




elif choise0 == 'updates':
    base_url  = 'https://yummyanime.club/anime-updates'
    with requests.Session() as s:
        response = s.get(base_url, headers = headers)
        html = response.text
        soup = BeautifulSoup(html , 'html.parser')
       
    all_anime_updates = soup.select('ul.update-list > li ')
    for update in all_anime_updates:
        update_date = update.select_one('span.update-date').getText()
        update_title = update.select_one('span.update-title').getText()
        update_info = update.select_one('span.update-info').getText()
        update_link = 'https://yummyanime.club' + update.select_one('a')['href']
        print('------------\n[Дата:] ' + update_date + '\n[Название аниме:]  ' + update_title + '\n[Что нового:]  ' + update_info + '\n[Ссылка:] ' + update_link +  '\n------------')
        


elif choise0 == 'news':
    base_url = "https://yummyanime.club/posts"
    with requests.Session() as s:
        response = s.get(base_url, headers = headers)
        html = response.text
        soup = BeautifulSoup(html , 'html.parser')
        
    all_news = soup.select('div.post-block')
    for news in all_news:
        news_link = 'https://yummyanime.club' + news.select_one('a.post-title')['href']
        news_title = news.select_one('a.post-title').getText()
        news_post_time = news.select_one('div.post-time').getText()
        news_post_text = news.select_one('p').getText().replace('\r\n' , '')
        news_author = news.select_one('p').find_next('p').getText()
        news_number_of_comments = news.select_one('p').find_next('p').find_next('p').getText()
        print('------------\n[Дата:] ' + news_post_time + '\n[Название:] ' + news_title + "\n[Основной текст новости:] "  + news_post_text + "\n[Автор:] " + news_author + "\n[Коментариев:] " + news_number_of_comments + "\n[Ссылка:] " + news_link +  '\n------------' )


elif choise0 == 'anons':
    base_url = "https://yummyanime.club/announcement"
    with requests.Session() as s:
        response = s.get(base_url, headers = headers)
        html = response.text
        soup = BeautifulSoup(html , 'html.parser')
       
    all_anons = soup.select('.preview-block' )
    for one_anons in all_anons:
        anons_title = one_anons.select_one('a.preview-title').getText()
        anons_link = 'https://yummyanime.club' +  one_anons.select_one('a.preview-title')['href']
        anons_info = one_anons.select_one('ul > li').getText().replace('  ' , '').replace('\n' , ' ')
        anons_genre = one_anons.select_one('ul > li').find_next('ul').getText().replace('\n' ,' ')
        try:
            anons_text = one_anons.select_one('div.content-desc > p').getText()
        except:
            anons_text = "Нет описания"
        print("------------\n[Название:] " + anons_title + "\n[Инфо:] " + anons_info + "\n[Жанры:] " + anons_genre + "\n[Описание:] " + anons_text + "\n[Ссылка:] " + anons_link + '\n------------'  )

elif choise0 == 'video':
    base_url = "https://yummyanime.club/channel"
    with requests.Session() as s:
        response = s.get(base_url, headers = headers)
        html = response.text
        soup = BeautifulSoup(html , 'html.parser')
    
    all_videos = soup.select('div.post-block.clearfix')
    for video in all_videos :
        video_title = video.select_one('.post-title').getText()
        video_link = 'https://yummyanime.club' + video.select_one('.post-title')['href']
        video_type = video.select_one('a.badge.disabled').getText()
        video_text = video.select_one('p').getText()
        video_author = video.select_one('p').find_next('p').getText().replace(' ' , '').replace('\n' , ' ')
        video_number_of_comments = video.select_one('p').find_next('p').find_next('p').getText()
        
        print('------------\n[Название:]' + video_title + "\n[Тип:]" + video_type + "\n[Описание:] " + video_text + "\n[Автор:] " + video_author + "\n[Коментариев:] " + video_number_of_comments + "\n[Ссылка:] " + video_link + '\n------------')
        
elif choise0 == 'top-serials':
    base_url = "https://yummyanime.club/top"
    with requests.Session() as s:
        response = s.get(base_url, headers = headers)
        html = response.text
        soup = BeautifulSoup(html , 'html.parser')
    
    top_place = 0
    all_tops = soup.select('div.anime-column')  
    for top in all_tops :
        top_title = top.select_one('.anime-title').getText()
        top_place += 1
        top_views = top.select_one('div.icons-row').find_next('div').getText().replace('  ' , '').replace('\n' , "")
        top_voices = top.select_one('div.icons-row').find_next('div').find_next('div').getText().replace('  ' , '') 
        top_rating = top.select_one('.main-rating').getText()
        top_link = 'https://yummyanime.club' + top.select_one('.anime-title')['href']
        print('------------\n[Место в рейтинге:] ' + "# " + str(top_place) + "\n[Название:] "  + top_title + "\n[Количество просмотров:] " +  top_views + "\n[Количество голосов:] " + top_voices + "\n[Оценка:] " + top_rating + "\n[Ссылка:] " + top_link + '\n------------' )
        
elif choise0 == 'top-films':
    base_url = "https://yummyanime.club/top?sort=films"
    with requests.Session() as s:
        response = s.get(base_url, headers = headers)
        html = response.text
        soup = BeautifulSoup(html , 'html.parser')
    
    top_place = 0
    all_tops = soup.select('div.anime-column')  
    for top in all_tops :
        top_title = top.select_one('.anime-title').getText()
        top_place += 1
        top_views = top.select_one('div.icons-row').find_next('div').getText().replace('  ' , '').replace('\n' , "")
        top_voices = top.select_one('div.icons-row').find_next('div').find_next('div').getText().replace('  ' , '') 
        top_rating = top.select_one('.main-rating').getText()
        top_link = 'https://yummyanime.club' + top.select_one('.anime-title')['href']
        print('------------\n[Место в рейтинге:] ' + "# " + str(top_place) + "\n[Название:] "  + top_title + "\n[Количество просмотров:] " +  top_views + "\n[Количество голосов:] " + top_voices + "\n[Оценка:] " + top_rating + "\n[Ссылка:] " + top_link + '\n------------' )


elif choise0 == 'catalog-anime':
    choise_genre = int(input("Введите число с выбором жанра: \n1.Бисёнэн \n2.Исэкай \n3.Сёдзё \n4.Сёнэн-ай \n5.Гендерная интрига \n6.Махо-сёдзё \n7.Сёдзё-ай \n8.Сэйнэн \n9.Дзёсэй \n10.Меха \n11.Сёнэн \n12.Этти \n13.Вестерн \n14.Комедия \n15.Приключения \n16.Спорт \n17.Фантастика \n18.Эротика \n19.Детектив \n20.Мистика \n21.Психология \n22.Триллер \n23.Фэнтези \n24.Драма \n25.Преступность \n26.Романтика \n27.Ужасы \n28.Экшен \n29.Антивойна \n30.Военная тематика \n31.Гарем(для девочек) \n32.Исторический \n33.Лоликон \n34.Нелинейный сюжет \n35.Полицейские \n36.Прокси бои \n37.Стимпанк \n38.Антиутопия \n39.Война \n40.Игры \n41.Киберпанк \n42.Машины \n43.Повседневность \n44.Полулюди \n45.Русские в аниме \n46.Тайный заговор \n47.Безумие \n48.Гарем \n49.Исскуство \n50.Кулинария \n51.Не японское \n52.Политика \n53.Постапокалипсис \n54.Сверхьестественное \n55.Школьная жизнь \nВаш выбор: "))
    if choise_genre == 1:
        genre = 'category/bisenen'
    elif choise_genre == 2:
        genre = 'category/isekai'
    elif choise_genre == 3:
        genre = 'category/sedze'
    elif choise_genre == 4:
        genre = 'category/senen-aj'
    elif choise_genre == 5:
        genre = 'category/trap'
    elif choise_genre == 6:
        genre = 'category/maho-sedze'
    elif choise_genre == 7:
        genre = 'category/sedze-aj'
    elif choise_genre == 8:
        genre = 'category/sejnen'
    elif choise_genre == 9:
        genre = 'category/dzesej'
    elif choise_genre == 10:
        genre = 'category/meha'
    elif choise_genre == 11:
        genre = 'category/senen'
    elif choise_genre == 12:
        genre = 'category/etti'
    elif choise_genre == 13:
        genre = 'category/vestern'
    elif choise_genre == 14:
        genre = 'category/komediya'
    elif choise_genre == 15:
        genre = 'category/priklyucheniya'
    elif choise_genre == 16:
        genre = 'category/sport'
    elif choise_genre == 17:
        genre = 'category/fantastika'
    elif choise_genre == 18:
        genre = 'category/erotika'
    elif choise_genre == 19:
        genre = 'category/detektiv'
    elif choise_genre == 20:
        genre = 'category/mistika'
    elif choise_genre == 21:
        genre = 'category/psihologiya'
    elif choise_genre == 22:
        genre = 'category/triller'
    elif choise_genre == 23:
        genre = 'category/fentezi'
    elif choise_genre == 24:
        genre = 'category/drama'
    elif choise_genre == 25:
        genre = 'category/prestupnyj-mir'
    elif choise_genre == 26:
        genre = 'category/romantika'
    elif choise_genre == 27:
        genre = 'category/ugasy'
    elif choise_genre == 28:
        genre = 'category/ekshen'
    elif choise_genre == 29:
        genre = 'category/antivojna'
    elif choise_genre == 30:
        genre = 'category/voennaya-tematika' 
    elif choise_genre == 31:
        genre = 'category/garem-dlya-devochek' 
    elif choise_genre == 32:
        genre = 'category/istoricheskij'
    elif choise_genre == 33:
        genre = 'category/lolikon'
    elif choise_genre == 34:
        genre = 'category/nelinejnyj-syuzhet'
    elif choise_genre == 35:
        genre = 'category/policejskie'
    elif choise_genre == 36:
        genre = 'category/proksi-boi'
    elif choise_genre == 37:
        genre = 'category/stimpank'
    elif choise_genre == 38:
        genre = 'category/antiutopiya'
    elif choise_genre == 39:
        genre = 'category/vojna'
    elif choise_genre == 40:
        genre = 'category/igry'
    elif choise_genre == 41:
        genre = 'category/kiberpank'
    elif choise_genre == 42:
        genre = 'category/mashiny'
    elif choise_genre == 43:
        genre = 'category/povsednevnost'
    elif choise_genre == 44:
        genre = 'category/lyudi-zveri'
    elif choise_genre == 45:
        genre = 'category/rossiya-v-anime'
    elif choise_genre == 46:
        genre = 'category/tajnyj-zagovor'
    elif choise_genre == 47:
        genre = 'category/bezumie'
    elif choise_genre == 48:
        genre = 'category/garem'
    elif choise_genre == 49:
        genre = 'category/iskusstvo'
    elif choise_genre == 50:
        genre = 'category/kulinariya'
    elif choise_genre == 51:
        genre = 'category/ne-yaponskoe'
    elif choise_genre == 52:
        genre = 'category/politika'
    elif choise_genre == 53:
        genre = 'category/postapokaliptika'
    elif choise_genre == 54:
        genre = 'category/sverh-estestvennoe'
    elif choise_genre == 55:
        genre = 'category/shkola'
    
    
    base_url = "https://yummyanime.club/catalog/" + genre
    with requests.Session() as s:
        response = s.get(base_url, headers = headers)
        html = response.text
        soup = BeautifulSoup(html , 'html.parser')
    
    all_tops = soup.select('div.anime-column')  
    for top in all_tops :
        top_title = top.select_one('.anime-title').getText()
        top_views = top.select_one('div.icons-row').find_next('div').getText().replace('  ' , '').replace('\n' , "")
        top_voices = top.select_one('div.icons-row').find_next('div').find_next('div').getText().replace('  ' , '') 
        try:
            top_rating = top.select_one('.main-rating').getText()
        except:
            top_rating = '-'
        top_link = 'https://yummyanime.club' + top.select_one('.anime-title')['href']
        print("------------\n[Название:] "  + top_title + "\n[Количество просмотров:] " +  top_views + "\n[Количество голосов:] " + top_voices + "\n[Оценка:] " + top_rating + "\n[Ссылка:] " + top_link + '\n------------' )    

elif choise0 == 'ongoings':
    base_url = "https://yummyanime.club/ongoing"
    with requests.Session() as s:
        response = s.get(base_url, headers = headers)
        html = response.text
        soup = BeautifulSoup(html , 'html.parser')
    
    all_ongs = soup.select('div.preview-block.clearfix')
    for one_ong in all_ongs:
        ong_title = one_ong.select_one('a.preview-title').getText()
        ong_link = 'https://yummyanime.club' +  one_ong.select_one('a.preview-title')['href']
        ong_info = one_ong.select_one('ul > li').getText().replace('  ' , '').replace('\n' , ' ')
        ong_genre = one_ong.select_one('ul > li').find_next('ul').getText().replace('\n' ,' ')
        try:
            ong_text = one_ong.select_one('div.content-desc > p').getText()
        except:
            ong_text = "Нет описания"
        try:
            ong_voice = one_ong.select_one('ul.animeVoices').getText().replace('\n' ,' ')
        except:
           ong_voice = 'Нет информации об озвучке' 
        ong_update_info = one_ong.select_one('div.update-info').getText()
        print("------------\n[Название:] " + ong_title + "\n[Инфо:] " + ong_info + "\n[Жанры:] " + ong_genre + "\n[Описание:] " + ong_text + "\n[Озвучка:] " + ong_voice  + "\n[Что нового:] " + ong_update_info  + "\n[Ссылка:] " + ong_link + '\n------------'  )
        
        
        
        
else :
    print("Неправильно введенные данные!Попробуйте еще раз.")
        
        
    