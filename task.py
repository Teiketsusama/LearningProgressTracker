import re

students = []


def add_students():
    print("Enter student credentials or 'back' to return:")
    while True:
        input_str = input().strip()
        if input_str == "back":
            print(f"Total {len(students)} students have been added.")
            break

        input_list = input_str.split(" ")
        if len(input_list) < 3:
            print("Incorrect credentials.")
        else:
            f_name = input_list[0]
            email = input_list[-1]
            l_name = " ".join(input_list[1:-1])

            if not re.match(r"^[a-zA-Z]+(?:['-](?=[a-zA-Z]))*[a-zA-Z]+$", f_name) or len(f_name) < 2:
                print("Incorrect first name.")
            elif not re.match(r"^[\sa-zA-Z]+(?:['-](?=[a-zA-Z]))*(?:[\sa-zA-Z]+(?:['-](?=[a-zA-Z]))*)*$", l_name) or \
                    len(l_name) < 2:
                print("Incorrect last name.")
            elif not re.match(r"^[a-zA-Z0-9._\-]+@[a-zA-Z0-9._\-]+\.[a-zA-Z0-9]+$", email):
                print("Incorrect email.")
            else:
                print("The student has been added.")
                students.append((f_name, l_name, email))


def main():
    print("Learning progress tracker")
    while True:
        user_input = input()
        if user_input == "add students":
            add_students()
        elif user_input == "back":
            print("Enter 'exit' to exit the program.")
        elif user_input == "exit":
            print("Bye!")
            exit()
        elif len(user_input) == 0:
            print("No input")
        # Detect if a user has entered a blank line and print No input in response
        elif str.isspace(user_input):
            print("No input")
        else:
            print("Unknown command!")


if __name__ == "__main__":
    main()
