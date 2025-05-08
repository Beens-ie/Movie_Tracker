# main.py 

class Movie: 
    def __init__(self, title, genre, year, rating):
        self.title = title 
        self.genre = genre
        self.year = year
        self.rating = rating

    def __str__(self):
        return f"{self.title} ({self.year}) - {self.genre} - Rating: {self.rating}/10"
#list to store movies    
movies = []
def add_movie():
    title = input("Title: ")
    genre = input("Genre: ")
    year = input("Year: ")
    rating = input("Rating (0 - 10): ")
    print("\n---Add a Movie ---")

    movie = Movie(title, genre, year, rating)
    movies.append(movie)

def list_movies():
    print("\n Your Movies:")
    if not movies:
        print("No Movies Found")
    else:
        for idx, movie in enumerate(movies, 1):
             print(f"{idx}. Movie")

def main():
    print("Welcome to the movie tracker")

    while True:
        print("n\=== Menu ===")
        print("1. Add a Movie")
        print("2. View all Movies")
        print("3. Exit")

        choice = input("Choose an option (1-3): ")

        if choice == "1":
            add_movie()
        elif choice == "2":
            list_movies()
        elif choice == "3":
            print("Goodbye.")
            break

if __name__ == "__main__":
    main()