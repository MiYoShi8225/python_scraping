
from selenium import webdriver
import pandas as pd

class Youteb_search:
    def __init__(self, url):
        self.browser = webdriver.Chrome()
        self.url = url
        self.browser.get(url)

        """
        タイトルが出力される
        elem_movie_title = browser.find_element_by_id('video-title')
        #print(elem_movie_title.text)
        """

        """
        タイトルのと更に詳しい情報が出力される
        elem_movie_renderer.text
        #elem_movie_renderer = browser.find_element_by_class_name('style-scope ytd-video-renderer')
        """
        
    def simple_info(self):
        tag_list = ["タイトル", "youtuber", "再生数"]
        title_list = []
        name_list = []
        df = pd.DataFrame()

        elem_movies_title = self.browser.find_elements_by_id('video-title')
        """
        elem_movie_name = self.browser.find_elements_by_class_name(
            "yt-simple-endpoint style-scope yt-formatted-string"
        )
        """
        elem_movie_count = self.browser.find_elements_by_class_name(
            "style-scope ytd-video-meta-block"
        )

        #print(elem_movies_title[0].text)
        for title in elem_movies_title:
            title_list.append(title.text)
            print("\nタイトル\nNo.{}:{}".format(elem_movies_title.index(title), title.text))
        #df["タイトル"] = title_list

        #print(elem_movie_count[0].text.split("\n")[0])
        for name in elem_movie_count:
            name_list.append(name.text.split("\n")[0])
            print("\nyoutuber名\nNo.{}:{}".format(elem_movie_count.index(name), name.text.split("\n")[0]))

        """
        for indexnum,i in enumerate(title_list):
            print(indexnum,title_list[indexnum],name_list[indexnum])
        """
        #df["名前"] = name_list

    def roop_movie_info(self):
        try:
            youtub_info = []
            df = pd.DataFrame()
            tag_list = ["タイトル", "youtuber", "再生数", "投稿時間", "テキスト", "none"]
            
            youtube_info_list = [[],[],[],[],[],[]]

            #elem_movies_title = browser.find_elements_by_id('video-title')
            elem_movie_renderers = self.browser.find_elements_by_class_name('style-scope ytd-video-renderer')

            for indexnum1, info in enumerate(elem_movie_renderers):
                info_box = info.text.split("\n")
                youtub_info.append(info_box)
                        
            for youtube_info_category in youtub_info:
                for index2,category in enumerate(youtube_info_category):
                    if category != "•":
                        youtube_info_list[index2].append(category)

            #print(len(youtube_info_list))
            print(youtube_info_list[0])
            
            """
            for indexnum2, j in enumerate(youtube_info_list):
                df[tag_list[indexnum2]] = j
            df
            """

        except Exception as e:
            self.browser.quit()
            print("\n#####Exception Error\n#####{}".format(e))

    def stop_function(self):
        self.browser.quit()

"""
https://www.youtube.com/feed/trending
"""

rank_page = Youteb_search("https://www.youtube.com/feed/trending")

#rank_page.roop_movie_info()
rank_page.simple_info()

rank_page.stop_function()


