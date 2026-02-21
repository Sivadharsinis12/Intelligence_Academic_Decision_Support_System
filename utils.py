def calculate_risk(avg_mark, attendance):
    if avg_mark < 50 or attendance < 60:
        return "High"
    elif avg_mark < 70:
        return "Medium"
    else:
        return "Low"