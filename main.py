print("Please select your gender")
select_gender = str(input("Enter 'b' for a boy or 'g' for a girl: "))


def generate_names(gender):
    boy_names = ["Liam", "Noah", "Oliver", "James", 
                 "William", "Benjamin", "Lucas", "Henry",
                 "Theodore", "Jack", "Alexander", "Jackson", 
                 "Daniel", "Michael", "Mason",
                 "Sebastian", "Ethan", "Logan", "Owen", "Samuel", 
                 "Jacob", "Aiden", "John", "Joseph"]

    girl_names = ["Olivia", "Emma", "Charlotte", "Amelia", "Ava", 
                  "Sophia", "Isabella", "Mia", "Evelyn", "Harper",
                  "Luna", "Camila", "Gianna", "Elizabeth", "Eleanor", 
                  "Ella", "Abigail", "Sofia", "Avery", "Scarlett"]

    max_boy_name_letter = len(max(boy_names, key=len))
    min_boy_name_letter = len(min(boy_names, key=len))

    max_girl_name_letter = len(max(girl_names, key=len))
    min_girl_name_letter = len(min(girl_names, key=len))

    list = []
    
    if gender == "boy":
        try:
            num_letter = int(input(f"How many letters would you prefer to have in the boy's name? (Must be between {min_boy_name_letter} and {max_boy_name_letter}) "))
            if num_letter < min_boy_name_letter:
                print("Invalid Interger")
            elif num_letter > max_boy_name_letter:
                print(f"Invalid Interger")
            elif num_letter >= min_boy_name_letter and num_letter <= max_boy_name_letter:
                for boy_name in boy_names:
                    if len(boy_name) == num_letter:
                        list.append(boy_name)
                result = ", ".join(list)
                print(f"Some name suggestions for the {gender} are: {result}")
        except ValueError:
            print("Input must be an interger")

    elif gender == "girl":
        try:
            num_letter = int(input(f"How many letters do you want for the girl's name to be? (Must be between {min_girl_name_letter} and {max_girl_name_letter}) "))
            if num_letter < min_girl_name_letter:
                print("Invalid Interger")
            elif num_letter > max_girl_name_letter:
                print("Invalid Interger")
            elif num_letter >= min_girl_name_letter and num_letter <= max_girl_name_letter:
                for girl_name in girl_names:
                    if len(girl_name) == num_letter:
                        list.append(girl_name)
                result = ", ".join(list)
                print(f"Some name suggestions for the {gender} are: {result}")
        except ValueError:
            print("Input must be an interger")
    
    else:
        print("Please input a valid gender")


if select_gender.lower() == "b":
    generate_names("boy")
elif select_gender.lower() == "g":
    generate_names("girl")
else:
    print("Please input a valid letter")
