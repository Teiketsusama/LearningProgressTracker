from re import match
from decimal import Decimal, ROUND_HALF_UP

students = []
list_of_ids = []
students_points = {}
submission = [0, 0, 0, 0]
students_notified = []


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

            if not match(r"^[a-zA-Z]+(?:['-](?=[a-zA-Z]))*[a-zA-Z]+$", f_name) or len(f_name) < 2:
                print("Incorrect first name.")
            elif not match(r"^[\sa-zA-Z]+(?:['-](?=[a-zA-Z]))*(?:[\sa-zA-Z]+(?:['-](?=[a-zA-Z]))*)*$", l_name) or \
                    len(l_name) < 2:
                print("Incorrect last name.")
            elif not match(r"^[a-zA-Z0-9._\-]+@[a-zA-Z0-9._\-]+\.[a-zA-Z0-9]+$", email):
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
                    students_points[student_id] = {"python": 0, "dsa": 0, "databases": 0, "flask": 0}
                students_points[student_id]["python"] += c_py
                if c_py > 0:
                    submission[0] += 1
                students_points[student_id]["dsa"] += c_dsa
                if c_dsa > 0:
                    submission[1] += 1
                students_points[student_id]["databases"] += c_db
                if c_db > 0:
                    submission[2] += 1
                students_points[student_id]["flask"] += c_fk
                if c_fk > 0:
                    submission[3] += 1
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
            points_list = [students_points[input_id]["python"], students_points[input_id]["dsa"],
                           students_points[input_id]["databases"], students_points[input_id]["flask"]]
            print(f"{input_id} points: "
                  f"Python={points_list[0]}; DSA={points_list[1]}; Databases={points_list[2]}; Flask={points_list[3]}")


def course_statistics(course: str) -> list:
    n_enrolled = 0
    sum_points = 0
    avg_points = 0
    # Calculate the number of students who have enrolled the course, and average points
    for points in students_points.values():
        if points[course] > 0:
            n_enrolled += 1
            sum_points += points[course]
    if n_enrolled > 0:
        avg_points = sum_points / n_enrolled
    # Submission
    if course == "python":
        n_submission = submission[0]
    elif course == "dsa":
        n_submission = submission[1]
    elif course == "databases":
        n_submission = submission[2]
    elif course == "flask":
        n_submission = submission[3]

    return [n_enrolled, n_submission, avg_points]


def course_comparison() -> list:
    courses = {
        "Python": course_statistics("python"),
        "DSA": course_statistics("dsa"),
        "Databases": course_statistics("databases"),
        "Flask": course_statistics("flask")
    }
    # Compare the number of students enrolled in each course
    most_popular = []
    least_popular = []
    [most_popular.append(course) for course in courses
     if 0 < courses[course][0] == max(courses.values(), key=lambda x: x[0])[0]]
    [least_popular.append(course) for course in courses
     if 0 < courses[course][0] == min(courses.values(), key=lambda x: x[0])[0] and course not in most_popular]
    # Compare the number of completed tasks in each course
    highest_activity = []
    lowest_activity = []
    [highest_activity.append(course) for course in courses
     if 0 < courses[course][1] == max(courses.values(), key=lambda x: x[1])[1]]
    [lowest_activity.append(course) for course in courses
     if 0 < courses[course][1] == min(courses.values(), key=lambda x: x[1])[1] and course not in highest_activity]
    # Compare the average points in each course
    easiest_course = []
    hardest_course = []
    [easiest_course.append(course) for course in courses
     if 0 < courses[course][2] == max(courses.values(), key=lambda x: x[2])[2]]
    [hardest_course.append(course) for course in courses
     if 0 < courses[course][2] == min(courses.values(), key=lambda x: x[2])[2] and course not in easiest_course]

    return [most_popular, least_popular, highest_activity, lowest_activity, easiest_course, hardest_course]


def display_statistics():
    print("Type the name of a course to see details or 'back' to quit:")
    comparison_list = ["Most popular", "Least popular", "Highest activity", "Lowest activity", "Easiest course",
                       "Hardest course"]
    for i in range(len(comparison_list)):
        if len(course_comparison()[i]) == 1:
            print(f"{comparison_list[i]}: {course_comparison()[i][0]}")
        elif len(course_comparison()[i]) > 1:
            print(f"{comparison_list[i]}: {', '.join(course_comparison()[i])}")
        else:
            print(f"{comparison_list[i]}: n/a")

    while True:
        input_course = input().strip().lower()
        if input_course == "back":
            break
        elif input_course in ["python", "dsa", "databases", "flask"]:
            """
            To complete each of these courses, a student must earn a certain number of points that are different 
            for each course: 600 for Python, 400 for DSA, 480 for Databases, and 550 for Flask.
            The list must be sorted by the total number of points in descending order, and if two or more students
            have the same number of points, they must be sorted by their ID in ascending order.
            """
            sorted_students = sorted(students_points.items(), key=lambda x: (-x[1][input_course], x[0]))
            print(f"{input_course.capitalize()}\nid     points    completed")
            for student, points in sorted_students:
                if input_course == "python":
                    cpl_perc = Decimal(points[input_course] / 6).quantize(Decimal(".0"), ROUND_HALF_UP)
                elif input_course == "dsa":
                    cpl_perc = Decimal(points[input_course] / 4).quantize(Decimal(".0"), ROUND_HALF_UP)
                elif input_course == "databases":
                    cpl_perc = Decimal(points[input_course] / 4.8).quantize(Decimal(".0"), ROUND_HALF_UP)
                elif input_course == "flask":
                    cpl_perc = Decimal(points[input_course] / 5.5).quantize(Decimal(".0"), ROUND_HALF_UP)

                print(f"{student} {points[input_course]:<6} {cpl_perc:>6}%")
        else:
            print("Unknown course.")


def notify_students():
    completion_students = {
        "Python": [],
        "DSA": [],
        "Databases": [],
        "Flask": []
    }
    for student, points in students_points.items():
        if points["python"] >= 600:
            index = list_of_ids.index(student)
            completion_students["Python"].append(students[index])
        if points["dsa"] >= 400:
            index = list_of_ids.index(student)
            completion_students["DSA"].append(students[index])
        if points["databases"] >= 480:
            index = list_of_ids.index(student)
            completion_students["Databases"].append(students[index])
        if points["flask"] >= 550:
            index = list_of_ids.index(student)
            completion_students["Flask"].append(students[index])

    students_to_notify = []
    for course in completion_students:
        if len(completion_students[course]) > 0:
            for student_info in completion_students[course]:
                if student_info not in students_notified:
                    students_to_notify.append(student_info)
                    f_name, l_name, email = student_info
                    print(f"To: {email}\n"
                          f"Re: Your Learning Progress\n"
                          f"Hello, {f_name} {l_name}! You have accomplished our {course} course!")

    unique_students = {frozenset(student): student for student in students_to_notify}
    num_of_students = len(unique_students)
    print(f"Total {num_of_students} students have been notified.")
    students_notified.extend(unique_students.values())


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
        elif user_input == "statistics":
            display_statistics()
        elif user_input == "notify":
            notify_students()
        elif user_input == "back":
            print("Enter 'exit' to exit the program.")
        elif user_input == "exit":
            print("Bye!")
            exit()
        elif len(user_input) == 0:
            print("No input")
        elif str.isspace(user_input):
            print("No input")
        else:
            print("Unknown command!")


if __name__ == "__main__":
    main()
