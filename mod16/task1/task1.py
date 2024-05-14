import sqlite3
with sqlite3.connect('cinematography.db') as conn:
    ENABLE_FOREIGN_KEY = "PRAGMA foreign_keys = ON;"
    cur = conn.cursor()
    cur.executescript('''
            drop table if exists actors;
            create table actors (
                act_id integer primary key autoincrement,
                act_first_name varchar(50) not null,
                act_last_name varchar(50) not null,
                act_gender varchar(1) not null
            );
        ''')
    cur.executescript('''drop table if exists movie;
                create table movie (
                mov_id integer primary key autoincrement,
                mov_title varchar(50) not null
                );''')
    cur.executescript('''drop table if exists director;
                create table director (
                dir_id integer primary key autoincrement,
                dir_first_name varchar(50) not null,
                dir_last_name varchar(50) not null
                );''')
    cur.executescript('''
        DROP TABLE IF EXISTS movie_cast;
        CREATE TABLE movie_cast (
            act_id INTEGER REFERENCES actors (act_id) ON DELETE CASCADE NOT NULL,
            mov_id INTEGER REFERENCES movie (mov_id) ON DELETE CASCADE NOT NULL,
            role VARCHAR(50) NOT NULL
        );
            ''')
    cur.executescript('''
        DROP TABLE IF EXISTS oscar_awarded;
        CREATE TABLE oscar_awarded (
        award_id INTEGER PRIMARY KEY AUTOINCREMENT,
        mov_id INTEGER REFERENCES movie (mov_id) ON DELETE CASCADE NOT NULL
        );
            ''')
    cur.executescript('''
            DROP TABLE IF EXISTS movie_direction;
            CREATE TABLE movie_direction (
            dir_id INTEGER REFERENCES director (dir_id) ON DELETE CASCADE NOT NULL,
            mov_id INTEGER REFERENCES movie (mov_id) ON DELETE CASCADE NOT NULL
            );
                ''')
    conn.commit()
