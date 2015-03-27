# -*- coding: utf-8 -*-
__author__ = 'seany'


import sqlite3


def store_in_database(movie_list, database_name):
    conn = sqlite3.connect(database_name)
    cur = conn.cursor()
    for i in movie_list.dict.keys():
        # print "The type is:", i.decode("utf-8")
        cmd_1 = "CREATE TABLE " + i + \
                " (movie_name varchar(20) not null, score varchar(5), num_of_rating varchar(6) not null)"
        print cmd_1
        cur.execute(cmd_1)
        for j in movie_list.dict[i]:
            cmd_2 = "INSERT INTO " + i + \
                    " values('" + j.name_ch + "', " + str(j.score) + ", " + str(j.num_of_rating) + ")"
            print cmd_2
            cur.execute(cmd_2)
    conn.commit()
    conn.close()