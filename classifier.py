def classify_domain(message: str)-> str:
    m = message.lower()
    if any(w in m for w in ["study", "exam","homework", "learn"]):
        return "education"
    if any(w in m for w in ["health", "diet", "excercize", "sleep"]):
        return "health"
    if any(w in m for w in ["climate", "eco", "recycle", "carbon"]):
        return "sustainability"
    return "mixed"