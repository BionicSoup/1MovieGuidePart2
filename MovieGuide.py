def create_movies_file():
    # Part 1: Create movies.txt and add initial movie titles
    movies = ["Cat on a Hot Tin Roof", "On the Waterfront", "Monty Python and the Holy Grail"]
    with open("movies.txt", "w") as file:
        for movie in movies:
            file.write(movie + "\n")

def display_menu():
    # Part 2: Display heading and menu choices
    print("The Movie List program")
    print("COMMAND MENU")
    print("list - List all movies")
    print("add - Add a movie")
    print("del - Delete a movie")
    print("exit - Exit program")

def read_movies():
    # Part 3: Open movies.txt and populate a list with movie titles
    movies = []
    try:
        with open("movies.txt", "r") as file:
            for line in file:
                movies.append(line.strip())
    except FileNotFoundError:
        # If file doesn't exist, create it with initial movies
        create_movies_file()
        with open("movies.txt", "r") as file:
            for line in file:
                movies.append(line.strip())
    return movies

def write_movies(movies):
    # Write the current list back to movies.txt
    with open("movies.txt", "w") as file:
        for movie in movies:
            file.write(movie + "\n")

def display_movies(movies):
    # Display all titles in the list, numbered starting from 1
    if not movies:
        print("No movies in the list.")
    else:
        for i, movie in enumerate(movies, 1):
            print(f"{i}. {movie}")

def add_movie(movies):
    # Add a movie title to the list, write to file, and display updated list
    movie = input("Movie: ")
    movies.append(movie)
    write_movies(movies)
    print(f"{movie} was added.")
    display_movies(movies)

def delete_movie(movies):
    # Delete a movie by number, handle invalid input, write to file, and display updated list
    display_movies(movies)
    try:
        number = int(input("Number: ")) - 1  # Convert to 0-based index
        if 0 <= number < len(movies):
            deleted_movie = movies.pop(number)
            write_movies(movies)
            print(f"{deleted_movie} was deleted.")
            display_movies(movies)
        else:
            print("Invalid movie number.")
    except ValueError:
        print("Invalid movie number.")

def main():
    # Initialize movie list from file
    movies = read_movies()

    while True:
        # Display menu
        display_menu()

        # Get user command
        command = input("Command: ").lower()

        if command == "list":
            display_movies(movies)
        elif command == "add":
            add_movie(movies)
        elif command == "del":
            delete_movie(movies)
        elif command == "exit":
            print("Bye!")
            break
        else:
            print("Not a valid command. Please try again.")

if __name__ == "__main__":
    main()
