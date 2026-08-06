print("=====================IMDB Rating Using For and While===================")

total_movies = int(input("enter number of movies: "))

excellent_rating = 0
good_rating = 0
average_rating = 0

for movie_number in range (1, total_movies + 1):
    print(f"movie number is : {movie_number}")

    movie_name = input("enter movie name: ")
    rating = int(input("enter movie rating: "))

    while rating < 1 or rating>10:
        print("Invalid rating, please enter number between 1 and 10.")

        rating = int(input("enter correct rating: "))

    if rating >=8:
        print(f"Movie {movie_name} IMDB Rating is {rating} Excellent.")
        excellent_rating += 1

    elif rating >=5:
        print(f"Movie {movie_name} IMDB Rating is {rating} Good.")
        good_rating += 1

    else:
        print(f"Movie {movie_name} IMDB Rating is {rating} Average.")
        average_rating += 1

print(f"Total Movies: {total_movies}")
print(f"Total Excellent Movies : {excellent_rating}")
print(f"Total Good Movies : {good_rating}")
print(f"Total Average Movies : {average_rating}")

Excellent_movie_percentage = ((excellent_rating/total_movies)*100)
Good_movie_percentage = ((good_rating/total_movies)*100)
Average_movie_percentage = ((average_rating/total_movies)*100)

print(f"Excellent Movies Percentage : {Excellent_movie_percentage:.2f}%")
print(f"Good Movies Percentage: {Good_movie_percentage:.2f}%")
print(f"Average Movies Percentage: {Average_movie_percentage:.2f}%")

print("=============IMDB Ratings==============")
print("===========Thanks for watching ===========")
print("==========If you like my practice sessions please like and subscribe. Thank you!========")

