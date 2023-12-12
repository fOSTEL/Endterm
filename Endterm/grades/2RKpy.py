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

def readCourseScoresFromFile(filename):
    
    with open(filename, 'r') as file:
        lines = file.readlines()

    course_scores = [tuple(line.strip().split(',')) for line in lines]

    return course_scores

def translateScoresToPoints(course_scores):
    
    translated_scores = [(int(credit_hours), translateLetter(letter_grade)) for credit_hours, letter_grade in course_scores]

    return translated_scores

def saveTranslatedScoresToFile(translated_scores, output_filename):
    
    with open(output_filename, 'w') as file:
        for credit_hours, points in translated_scores:
            file.write(f"{credit_hours},{points}\n")

def main():
    input_filename = 'grades'
    input_filename = 'math.txt'
    input_filename = 'chemistry.txt'
    input_filename = 'english.txt'
    output_filename = 'overallGPAs.txt'

    course_scores = readCourseScoresFromFile(input_filename)

    translated_scores = translateScoresToPoints(course_scores)

    saveTranslatedScoresToFile(translated_scores, output_filename)

    gpa = calculateGPA(translated_scores)
    print(f"Overall GPA: {gpa:.2f}")

if __name__ == "__main__":
    main()
