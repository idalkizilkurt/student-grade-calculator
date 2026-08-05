def calculate_average(midterm: float, final: float) -> float:
    """
    Calculates the weighted average.
    Midterm: 40%
    Final: 60%
    """
    return midterm * 0.4 + final * 0.6

def determine_letter_grade(average: float) -> str:
    """
    Returns the letter grade according to the average.
    """

    if average >= 85:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 50:
        return "C"
    else:
        return "F"