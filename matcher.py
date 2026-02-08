from difflib import SequenceMatcher

def similarity(a, b):
    return SequenceMatcher(None, a.lower(), b.lower()).ratio()

def find_best_answer(user_question, faq_data, threshold=0.35):
    best_score = 0
    best_answer = "Sorry, I couldn't find a relevant answer."

    for question, answer in faq_data.items():
        score = similarity(user_question, question)
        if score > best_score:
            best_score = score
            best_answer = answer

    if best_score < threshold:
        return "Sorry, I couldn't find a relevant answer."

    return best_answer