# def check_ats_compliance(text):
#     suggestions = []
#     score = 0

#     if "experience" in text.lower(): score += 1
#     else: suggestions.append("Missing 'Experience' section")

#     if "skills" in text.lower(): score += 1
#     else: suggestions.append("Add a 'Skills' section")

#     if "education" in text.lower(): score += 1
#     else: suggestions.append("Missing 'Education' section")

#     if "email" in text.lower(): score += 1
#     else: suggestions.append("Missing contact info")

#     total_score = (score / 4) * 100
#     return total_score, suggestions
def check_ats_compliance(text):
    suggestions = []
    score = 0

    # Normalize text (case-insensitive and simplified)
    text = text.lower()

    checks = [
        ("experience", "Missing 'Experience' section"),
        ("skills", "Add a 'Skills' section"),
        ("education", "Missing 'Education' section"),
        ("email", "Missing contact email"),
        ("contact", "Missing phone number"),
        ("certification", "Consider adding certifications"),
        ("project", "List projects to highlight hands-on experience"),
        ("summary", "Include a professional summary at the top"),
        ("linkedin", "Add a LinkedIn URL"),
        ("achievement", "Include key achievements"),
    ]

    for keyword, message in checks:
        if keyword.lower() in text:
            score += 1
        else:
            suggestions.append(message)

    total_score = (score / len(checks)) * 100
    return round(total_score, 2), suggestions
