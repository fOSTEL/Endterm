def calculateGPA(grades):
    totalcredits = 0
    totalgradepoints = 0

    for course in grades:
        credit_hours, letter_grade = course
        credit_points = translateLetter(letter_grade)
        totalcredits += credit_hours
        totalgradepoints += credit_hours * credit_points

    overall_gpa = totalgradepoints / totalcredits
    return overall_gpa

def translateLetter(letter_grade):
    grades = {
        'A+': 4.3,
        'A': 4.0,
        'A-': 3.7,
        'B+': 3.3,
        'B': 3.0,
        'B-': 2.7,
        'C+': 2.3,
        'C': 2.0,
        'C-': 1.7,
        'D+': 1.3,
        'D': 1.0,
        'D-': 0.7,
    }
    return grades.get(letter_grade, 0.0)

def translatePercentage(percentage):
    if percentage >= 95:
        return 'A+'
    elif percentage >= 90:
        return 'A'
    elif percentage >= 85:
        return 'A-'
    elif percentage >= 80:
        return 'B+'
    elif percentage >= 75:
        return 'B'
    elif percentage >= 70:
        return 'B-'
    elif percentage >= 65:
        return 'C+'
    elif percentage >= 60:
        return 'C'
    elif percentage >= 55:
        return 'C-'
    elif percentage >= 50:
        return 'D+'
    elif percentage >= 45:
        return 'D'
    else: 
        return 'D-'

grades = [("Maths: ", 4, 'A-'), ("Chemistry: ", 3, 'B-'), ( "English: ", 4, 'A')]
gpa = calculateGPA(grades)
print(f"Overall GPA: {gpa:.2f}")

#4.  An API, or Application Programming Interface, is a server that you can use to retrieve and send data to using code.
#4.  APIs are used to integrate new applications with existing software systems

#5.  Sockets and the socket API are used to send messages across a network.
#5.  In Python, the socket module provides a way to work with sockets. As we discussed earlier, sockets allow you to establish network connections over various network protocols such as TCP or UDP to send and receive data