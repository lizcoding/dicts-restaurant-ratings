"""Restaurant rating lister."""

# put your code here

def create_restaurant_dict(filename):
    with open(filename) as file:
        dictionary = {}
        data = file.readlines()
        data = [line.strip() for line in data]
        for value in data:
            value = value.split(":")
            dictionary[value[0]] = value[1]
    return dictionary


def add_rating(ratings):
    new_restaurant = input("Enter restaurant name -> ")
    restaurant_score = input("Enter restaurant score -> ")
    ratings[new_restaurant] = restaurant_score
    print(f'{new_restaurant} added to ratings!')
    print()


def sorted_ratings(ratings):
    for item in sorted(ratings.items()):
        print(f"{item[0]} is rated at {item[1]}.")
    print()



ratings_dict = create_restaurant_dict('scores.txt')
sorted_ratings(ratings_dict)
add_rating(ratings_dict)
sorted_ratings(ratings_dict)