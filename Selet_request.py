import sqlalchemy

engine = sqlalchemy.create_engine('postgresql://postgres:123456789@localhost:5432/postgres')

connection = engine.connect()

# connection.execute("""INSERT INTO artist(artist, nickname)
#                 VALUES('wolf', 'wolfman'),('Слон', 'Хобот'),('Енот', 'Полоскун'),('Жираф','Пятно'),
#                 ('Попугай','Перо'),('Медведь','Саня'),('Еж','Поравоз'),
#                 ('Собака','Псинчи');
# """)

# connection.execute("""INSERT INTO genres(genre)
#                 VALUES('Инди-Рок'),('Рок'),('Попса'),('Шансон'),('Классика');
# """)

# connection.execute("""INSERT INTO alboms(alboms, year)
#                 VALUES('Вою на луну',2018),('Хочу домой', 2021),('Длинная шея',2021),('Медвежий угол', 2020),
#                 ('Постой Паровоз', 2000),('Летели не туда', 2021),('Мойте руки', 2020),('Лучше всех живу',2022);
# """)
#
# connection.execute("""INSERT INTO tracks(alboms_id, tracks, duration)
#                 VALUES(1,'Вою на луну', 3.5),(1, 'Летит кирпич', 1),(1, 'Уворот',4),(1, 'Приехали менты', 4),
#                 (4,'Медвежий угол', 5),(4, 'Цыганский цирк', 4),(4, 'Зубастый рот', 7),(5, 'Мойте руки дети', 5),
#                 (5,'В Питере мыть', 3.5),(5, 'Нева Краса', 4),(6, 'Летели не туда',4),(6, 'Очнулись в Сургуте', 4),
#                 (6,'Постучались с низу', 5),(8, 'Лучший день', 4),(8, 'Конец света', 7),(8, 'Последний час', 5);
# """)

# connection.execute("""INSERT INTO Сollection(namecollection, year_)
#                 VALUES('Блатняк', 2022),
#                 ('Крокс', 2021),
#                 ('Звуки природы', 2022),
#                 ('Конь не беда', 2021),
#                 ('Путешествие', 2021),
#                 ('Конец света', 2020),
#                 ('Желание', 2022),
#                 ('Запара', 2022);
# """)
#
# connection.execute("""INSERT INTO artist_tracks_genres(artist_id, tracks_id, genres_id)
#                 VALUES(1, 1, 1),(3, 2, 3),(5, 3, 3),(7, 4, 4),(8, 5, 5),(6, 6, 2),
#                 (4, 7, 2),(7, 8, 4),(8, 9, 5),(8, 10, 5),(6, 11, 2),(6, 12, 1),(6, 13, 4),(7, 14, 5),
#                 (7, 15, 3);
# """)

# connection.execute("""INSERT INTO tracol(collection_id, tracks_ids)
#                 VALUES(24, 1),(25, 2),(26, 3),(27, 4),(28, 5),(29, 6),
#                 (30, 7),(31, 8),(31, 9),(30, 10),(29, 11),(28, 12),(27, 13),(26, 14),
#                 (25, 15);
# """)


# test1 = connection.execute(""" DELETE  FROM Сollection;
# """)
#
# test2 = connection.execute(""" SELECT * FROM Сollection;
# """).fetchall()
# print(test2)

test1 = connection.execute(""" SELECT alboms, year FROM alboms
WHERE year = 2018
""").fetchall()

test2 = connection.execute(""" SELECT tracks, duration FROM tracks
WHERE duration = (SELECT MAX(duration) FROM tracks)
""").fetchall()

test3 = connection.execute(""" SELECT tracks FROM tracks
WHERE duration  >= 3.5
""").fetchall()

test4 = connection.execute(""" SELECT namecollection, year_ FROM Сollection
WHERE year_  BETWEEN 2018 and 2020;
""").fetchall()

test5 = connection.execute(""" SELECT artist FROM artist
WHERE array_length(regexp_split_to_array(artist, '\s+'), 1) <= 1;
""").fetchall()

test6 = connection.execute(""" SELECT tracks FROM tracks
WHERE tracks LIKE 'Мой%%';
""").fetchall()

print(test1)
print(test2)
print(test3)
print(test4)
print(test5)
print(test6)

