# Boy and girl name generator

# Function that returns the list of boy names
def generate_boy_names():
    boy_names =  ["Liam", "Noah", "Oliver", "James", "William", 
                  "Benjamin", "Lucas", "Henry","Theodore", "Jack", 
                  "Alexander", "Jackson", "Daniel", "Michael", "Mason", 
                  "Sebastian", "Ethan", "Logan", "Owen", "Samuel", 
                  "Jacob", "Aiden", "John", "Joseph"]
    return boy_names

# Function that returns the list of girl names
def generate_girl_names():
    girl_names = ["Olivia", "Emma", "Charlotte", "Amelia", "Ava", 
                  "Sophia", "Isabella", "Mia", "Evelyn", "Harper",
                  "Luna", "Camila", "Gianna", "Elizabeth", "Eleanor", 
                  "Ella", "Abigail", "Sofia", "Avery", "Scarlett"]
    return girl_names

# Function that asks for the user's input
def get_num_letters(gender, min_len, max_len):
    # While loop which asks the user for the input until it's within the conditions
    while True:
        # The programs tries to task user for an integer, if receive value other than integer the program would not return a value error
        try:
            # Variable which asks for the numbers of letters in the name
            num_letters = int(input(f"How many letters do you want for the {gender}'s name? (Must be between {min_len} and {max_len}): "))
            # The program determines whether the integer is within required length, else the user is asked to input another value within the conditions
            if num_letters < min_len or num_letters > max_len:
                print("Invalid input")
            else:
                # Stores the input in a variable and returns it
                return num_letters
        except ValueError:
            print("Input must be an integer")

# Function that generates the names based on the user's inputs
def generate_names(gender):
    # If the gender is boy, this function calls the generate_boy_names function which returns the list of boy names then store it the names variable
    if gender == "boy":
        names = generate_boy_names()
        gender_text = "boy"
    # Else, this function calls the generate_girl_names function which returns the list of girl names then store it the names variable
    else:
        names = generate_girl_names()
        gender_text = "girl"
    
    # The two variables store the minimum and maximum number of letters in the "names" list
    min_len = len(min(names, key=len))
    max_len = len(max(names, key=len))
    
    # The variable calls the get_num_letters function which asks for the user's input
    num_letters = get_num_letters(gender_text, min_len, max_len)
    
    # The list of suggested names are store in the suggestions variable
    suggestions = [name for name in names if len(name) == num_letters]
    
    # The suggested names are then printed for the user
    print(f"Some name suggestions for {gender_text} are: {', '.join(suggestions)}")

# Executing the functions
print("Please select your gender")
# While loop which asks for user's input until it's within the conditions; else, the program continues to ask for the user's input
while True:
    # Input function which asks the user to select between 2 genders then stores in a variable
    select_gender = input("Enter 'b' for a boy or 'g' for a girl: ")
    # If the program receive the letter "b" or "g" from the user, the generate_names function is called with the correct gender as the required parameter
    if select_gender.lower() == "b":
        generate_names("boy")
        break
    elif select_gender.lower() == "g":
        generate_names("girl")
        break
     # The while loop is then stopped if user inputs the correct letter
    else:
        print("Please input a valid letter")
