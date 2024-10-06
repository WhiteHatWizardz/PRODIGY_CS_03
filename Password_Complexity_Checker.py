import re

def assess_password_strength(password):
    # Initialize strength criteria
    length_criteria = len(password) >= 8
    uppercase_criteria = re.search(r"[A-Z]", password) is not None
    lowercase_criteria = re.search(r"[a-z]", password) is not None
    number_criteria = re.search(r"[0-9]", password) is not None
    special_char_criteria = re.search(r"[@$!%*?&]", password) is not None

    # Initialize strength score
    score = 0

    # Assign points for each fulfilled criterion
    if length_criteria:
        score += 1
    if uppercase_criteria:
        score += 1
    if lowercase_criteria:
        score += 1
    if number_criteria:
        score += 1
    if special_char_criteria:
        score += 1

    # Provide feedback based on score
    if score == 5:
        return "Very Strong", score
    elif score == 4:
        return "Strong", score
    elif score == 3:
        return "Moderate", score
    elif score == 2:
        return "Weak", score
    else:
        return "Very Weak", score

def feedback(password):
    feedback_msgs = []
    
    if len(password) < 8:
        feedback_msgs.append("Password should be at least 8 characters long.")
    if not re.search(r"[A-Z]", password):
        feedback_msgs.append("Password should include at least one uppercase letter.")
    if not re.search(r"[a-z]", password):
        feedback_msgs.append("Password should include at least one lowercase letter.")
    if not re.search(r"[0-9]", password):
        feedback_msgs.append("Password should include at least one number.")
    if not re.search(r"[@$!%*?&]", password):
        feedback_msgs.append("Password should include at least one special character (@, $, !, %, *, ?, &).")

    if not feedback_msgs:
        feedback_msgs.append("Great password!")

    return feedback_msgs


if __name__ == "__main__":
    print("Password Strength Assessment Tool")
    
    # User input
    password = input("Enter a password to assess its strength: ")
    
    # Assess password strength
    strength, score = assess_password_strength(password)
    
    # Output the strength and score
    print(f"\nPassword strength: {strength}")
    print(f"Score: {score}/5\n")

    # Provide detailed feedback
    feedback_msgs = feedback(password)
    print("Feedback:")
    for msg in feedback_msgs:
        print(f"- {msg}")
