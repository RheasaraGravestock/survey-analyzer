import csv


def get_response():
    user_age = int(input("Please enter your age: "))
    favorite_app = input("Please enter your favorite app: ")
    hours_online = float(input("Please enter how many hours you spend online per day: "))
    user_rating = int(input("Please rate your favorite app out of 10: "))
    
    return {
        "user_age": user_age,
        "favorite_app": favorite_app,
        "hours_online": hours_online,
        "user_rating": user_rating
    }

def get_continue_choice():
    choice = input("Add another response? (y/n): ").strip().lower()

    if choice not in ["y", "yes", "no", "n"]:
        raise ValueError("Input must be yes/y or no/n")
        
    return choice


def display_responses(responses):
    print()
    print("ALL RESPONSES")
    print()
    
    for response in responses:
        print("User age:", response["user_age"])
        print("Favorite app:", response["favorite_app"])
        print("Hours online:", response["hours_online"])
        print("Rating out of 10:", response["user_rating"])
        print()

def calculate_average_age(responses):
    total_age = 0
    
    for response in responses:
        total_age += response["user_age"]

    average_age = total_age / len(responses)

    return average_age

def calculate_average_rating(responses):
    total_rating = 0

    for response in responses:
        total_rating += response["user_rating"]

    average_rating = total_rating / len(responses)

    return average_rating


def find_most_common_app(responses):
    app_counts = {}

    for response in responses:
        app = response["favorite_app"]

        if app in app_counts:
            app_counts[app] +=1
        else:
            app_counts[app] = 1

    most_common_app = ""
    highest_count = 0

    for app in app_counts:
        if app_counts[app] > highest_count:
            highest_count = app_counts[app]
            most_common_app = app
    
    return most_common_app

def save_to_csv(responses):
    file = open("survey_results.csv", "w", newline="")

    writer = csv.writer(file)

    writer.writerow([
        "Age",
        "Favorite App",
        "Hours Online",
        "User Rating"
    ])

    for response in responses:
        writer.writerow ([
            response["user_age"],
            response["favorite_app"],
            response["hours_online"],
            response["user_rating"]
        ])
    
    file.close()

def main():
    print("Survey Analyzer")

    responses = []

    while True:
        response = get_response()

        responses.append(response)


        try:
            choice = get_continue_choice()
       
            if choice in ["n", "no"]:
                break

        except ValueError as e:
            print(e)
            break

    display_responses(responses)

    average_age = calculate_average_age(responses)
    print("Average age:", average_age)

    average_rating = calculate_average_rating(responses)
    print("Average user rating:", average_rating)

    most_common_app = find_most_common_app(responses)
    print("Most common app:", most_common_app)

    save_to_csv(responses)

    print("Survey results saved to survey_results.csv")


if __name__ == "__main__":
    main()
