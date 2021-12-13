# imports
# =====================================
import psycopg2
from youtubesearchpython import VideosSearch, ResultMode
import json
from imdb import IMDb
from colorama import Fore
import math
#======================================


sel = [] # Save user input
class Movie:
    def __init__(self):
        pass

    def db_initialization(self):
        conn = psycopg2.connect("dbname=postgres user=postgres password=prime9990999")
        conn.autocommit = True 
        cursor = conn.cursor()
        
        cursor.execute("SELECT datname FROM pg_database;")

        print (f"{Fore.RED}Databases available:")
        for i in cursor.fetchall():
            print (f"{Fore.RED} -- {Fore.BLUE}{Fore.BLUE}{i[0]}{Fore.RED} -- {Fore.WHITE}")
        
        user = input("If you want to create a DB type the DB name, else type a number from the list to use an existing DB:")
        if user.isdigit():
            print(user)
        elif not user.isdigit():
            cursor.execute(f"CREATE database {user}")
            print ("Database created succesfully!!!")
            conn.commit()


    def create_table(self):
        ''' This is the function to create a table in the database '''
        
        self.conn = psycopg2.connect(f"dbname=postgres user=postgres password=prime9990999")
        self.interact = self.conn.cursor()
        try:
            self.interact.execute('''CREATE TABLE movies(
                    title VARCHAR (50),
                    release_year VARCHAR (50), 
                    genre VARCHAR (50), 
                    duration VARCHAR (50),
                    imdb_rating VARCHAR (50),
                    trailer VARCHAR (200));''')

            print("Table created!!!")
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        self.conn.commit()
   


    def add_movie(self):
        ''' Function to add a movie to the database '''
        self.conn = psycopg2.connect("dbname=movies user=postgres password=prime9990999")
        self.interact = self.conn.cursor()

        self.yt_trailer()
        self.imdb_info()
        self.min_to_hours(self.imdb_duration)

        self.interact.execute("INSERT INTO movies (title, release_year, genre, duration, imdb_rating, trailer) VALUES (%s, %s, %s, %s, %s, %s)", (self.imdb_title, self.imdb_release, self.imdb_genre, self.result, self.imdb_rating, self.yt_link))
        
        self.conn.commit()



    def retrieve_movie(self):
        ''' This is the function to display movies according to the user search '''

        self.conn = psycopg2.connect("dbname=movies user=postgres password=prime9990999")
        self.interact = self.conn.cursor()

        select_user = input("Find a movie: ")
        # select = f"SELECT * FROM movies WHERE title='{select_user.title()}';"asdas
        # SELECT * FROM movies WHERE title LIKE '%{select_user.title()}%' OR title LIKE '%{INPUT}%'
        select = f"SELECT * FROM movies WHERE title LIKE '%{select_user.title()}%' OR release_year LIKE '%{select_user.title()}%' OR genre LIKE '%{select_user.title()}%' OR IMDB_rating LIKE '%{select_user.title()}%'"

        self.interact.execute (select)

        records = self.interact.fetchall()
        for movie in records:
            print(f"{Fore.RED}Title:{Fore.WHITE} ", f"{Fore.BLUE} {movie[0]} {Fore.WHITE}")
            print(f"{Fore.RED}Release Year:{Fore.WHITE} ", f"{Fore.BLUE} {movie[1]} {Fore.WHITE}")
            print(f"{Fore.RED}Genre:{Fore.WHITE} ", f"{Fore.BLUE} {movie[2]} {Fore.WHITE}")
            print(f"{Fore.RED}Duration:{Fore.WHITE} ", f"{Fore.BLUE} {movie[3]} {Fore.WHITE}")
            print(f"{Fore.RED}IMDB rating:{Fore.WHITE} ", f"{Fore.BLUE} {movie[4]} {Fore.WHITE}")
            print(f"{Fore.RED}Trailer:{Fore.WHITE} ", f"{Fore.BLUE} {movie[5]} {Fore.WHITE}")
            print("\n")

        self.conn.commit()



    def list_movies(self):
        ''' Function to list all the movies from the database '''

        self.interact = self.conn.cursor()
        select = "SELECT * FROM movies"
        self.interact.execute(select)
        records = self.interact.fetchall()

        for movie in records:
            print (f"{Fore.RED}Title:{Fore.WHITE} {movie[0]}\n {Fore.RED}Release year:{Fore.WHITE} {movie[1]}\n {Fore.RED}Genre:{Fore.WHITE} {movie[2]}\n {Fore.RED}Duration:{Fore.WHITE} {movie[3]}\n {Fore.RED}IMDB rating:{Fore.WHITE} {movie[4]}\n {Fore.RED}Trailer:{Fore.WHITE} {movie[5]} \n")
    
        self.conn.commit()



    def imdb_info(self):
        global sel
        ''' Function to retrieve some data about the movies from IMDb '''

        ia = IMDb()

        movie_name = ia.search_movie(sel[0])
        details = ia.get_movie(str(movie_name[0].movieID))
        
        self.genre = (details.get('genres'))
        self.imdb_genre = ', '.join(map(str, self.genre))
        self.imdb_title = details.get('title')
        self.imdb_duration = details.get('runtimes')[0]
        self.imdb_rating = details.get('rating')
        self.imdb_release = details.get('year')
        sel.insert(1, self.imdb_title)


        print (f"{Fore.BLUE}Movie {Fore.RED}{self.imdb_title}{Fore.BLUE} has been added to the database!\n")
        return self.imdb_title, self.imdb_rating, self.imdb_duration, self.imdb_release, self.imdb_genre


    def yt_trailer(self):
        ''' Function to retrieve a movie trailer '''

        global sel
        videosSearch = VideosSearch(f'{sel[0].title()} + Official Trailer', limit = 1)
        final = videosSearch.result(mode= ResultMode.json)
        data  = json.loads(final)

        for link in data['result']:
            self.yt_link = (f"{link['link']}")
            return self.yt_link
        self.conn.commit()


    def user_inp(self):
        ''' This is the function for the user input '''

        global sel
        user = input("Movie name: ")
        sel.insert(0, user)
        return sel


    def min_to_hours(self, time):
        ''' This is the function to convert minutes to hour:minutes for the movies '''

        h_val = (int(time) * (1 / 60))
        h = math.modf(h_val)
        m = h[0] * 60
        self.result =  (f"{int(h[1])}h: {round(m)}m")
        return self.result

    
    def check_movie_copy_db(self):
        ''' This is a function to check if the movie a user wants to add already exists in the DB'''

        global sel
        self.conn = psycopg2.connect("dbname=movies user=postgres password=prime9990999")
        self.interact = self.conn.cursor()
        select = "SELECT * FROM movies"
        self.interact.execute(select)
        records = self.interact.fetchall()

        for movie in records:
            if sel[0].title() == movie[0]:
                print(f"{Fore.BLUE}Movie {Fore.RED}   {sel[0].title()}   {Fore.BLUE} is already in the database!!!\n")
                return True
            
        self.conn.commit()       
        


    def menu(self):
        ''' This is the function for the movies menu '''

        self.conn = psycopg2.connect("dbname=movies user=postgres password=prime9990999")
        interact = self.conn.cursor()

        select = "SELECT * FROM movies"
        interact.execute(select)
        records = interact.fetchall()

        print (Fore.RED + "||========== Movie database 'Kollector' ==========||" + Fore.GREEN)
        print(f"{Fore.RED}Total movies: {Fore.WHITE}{len(records)}\n {Fore.GREEN}")

        print ("[1]. List all the movies from the database")
        print ("[2]. Find a specific movie in the database")
        print ("[3]. Add a movie to the database")
        print ("[4]. Create database")
        print ("[q]. Quit")

        main_input = input(Fore.WHITE + "Select an option: ")
            
        if main_input == '1':
            self.list_movies()
            return (self.menu())
        elif main_input == '2':
            self.retrieve_movie()
            return (self.menu())
        elif main_input == '3':
            self.user_inp()
            if self.check_movie_copy_db() == True:
                sel.clear()
                return (self.menu())
            else:
                self.add_movie()
                sel.clear()
                self.menu()
        elif main_input == 'q':
            quit()

        elif main_input == '4':
            self.db_initialization()
        else:
            print("Wrong option!\n") 
            return (self.menu())


if __name__ == "__main__":
    cmd = Movie()
    cmd.menu()
