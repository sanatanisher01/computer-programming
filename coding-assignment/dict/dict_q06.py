# Program to create grade calculator in Python
grade_scale = {
    90: 'A - Excellent',
    80: 'B - Good',
    70: 'C - Satisfactory',
    60: 'D - Pass',
    0:  'F - Fail'
}

def calculate_grade(score):
    for min_score in sorted(grade_scale.keys(), reverse=True):
        if score >= min_score:
            return grade_scale[min_score]
    return grade_scale[0]
score = float(input("Enter score: "))
if 0 <= score <= 100:
    result = calculate_grade(score)
    print(f"Score: {score}")
    print(f"Grade: {result}")
else:
    print("Invalid score. Please enter a score between 0 and 100.")