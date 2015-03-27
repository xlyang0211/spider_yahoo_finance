# -*- coding: utf-8 -*-

__author__ = 'seany'

import get_info
import companies
import store_in_database


def main(database_name, score):
    movies_list = companies.Movies()
    movie_types = [
        "爱情",   "喜剧",   "动画",   "青春",
        "科幻",   "剧情",   "动作",   "经典"
        "剧情",   "动作",   "经典",   "青春",
        "悬疑",   "犯罪",   "惊悚",   "文艺",
        "励志",   "搞笑",   "恐怖",   "纪录片",
        "战争",   "短片",   "黑色幽默",
        "传记",   "情色",   "感人",   "动画短片",
        "暴力",   "音乐",   "童年",   "家庭",
        "黑帮",   "同志",   "女性",   "浪漫",
        "史诗",   "童话",   "烂片",   "cult"
    ]

    for i in movie_types:
        # print i
        get_info.get_info(movies_list, i, score)
    movies_list.sort()
    store_in_database.store_in_database(movies_list, database_name)
    # for key in movies_list.dict:
    #     for movie in movies_list.dict[key]:
    #         print key
    #         print movie


if __name__ == "__main__":
    database_name = raw_input("Input the database name you want to store the movies:")
    score = raw_input("Input the minimum score of the movie you want to search:")
    main(database_name, score)