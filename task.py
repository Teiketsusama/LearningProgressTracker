import re

students = []
list_of_ids = []
students_points = {}


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
            elif email in [student[2] for student in students]:
                print("This email is already taken.")
            else:
                print("The student has been added.")
                students.append((f_name, l_name, email))
                list_of_ids.append(str(email.__hash__())[-6:])


def list_ids():
    print("Students:")
    if len(list_of_ids) == 0:
        print("No students found")
    [print(ids) for ids in list_of_ids]


def add_points():
    print("Enter an id and points or 'back' to return:")
    while True:
        input_str = input().strip()
        if input_str == "back":
            break
        try:
            student_id, c_py, c_dsa, c_db, c_fk = input_str.split(" ")
            c_py = int(c_py)
            c_dsa = int(c_dsa)
            c_db = int(c_db)
            c_fk = int(c_fk)
            if student_id not in list_of_ids:
                print(f"No student is found for id={student_id}.")
            elif c_py < 0 or c_dsa < 0 or c_db < 0 or c_fk < 0:
                print("Incorrect points format.")
            else:
                if student_id not in students_points.keys():
                    students_points[student_id] = [0, 0, 0, 0]
                students_points[student_id] = [x + y for x, y in
                                               zip(students_points[student_id], [c_py, c_dsa, c_db, c_fk])]
                print("Points updated.")
        except ValueError:
            print("Incorrect points format.")


def show_points():
    print("Enter an id or 'back' to return:")
    while True:
        input_id = input().strip()
        if input_id == "back":
            break
        if input_id not in list_of_ids:
            print(f"No student is found for id={input_id}.")
        else:
            points_list = students_points[input_id]
            print(f"{input_id} points: "
                  f"Python={points_list[0]}; DSA={points_list[1]}; Databases={points_list[2]}; Flask={points_list[3]}")


def main():
    print("Learning progress tracker")
    while True:
        user_input = input()
        if user_input == "add students":
            add_students()
        elif user_input == "list":
            list_ids()
        elif user_input == "add points":
            add_points()
        elif user_input == "find":
            show_points()
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
