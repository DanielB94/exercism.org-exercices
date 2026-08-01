def response(hey_bob):
    question = hey_bob.strip()
    is_question = question.endswith("?")
    is_yelling = question.isupper()
    is_silence= not question

    if is_question and is_yelling:
        return "Calm down, I know what I'm doing!"
    elif is_question:
        return "Sure."
    elif is_yelling:
        return 'Whoa, chill out!'
    elif is_silence:
        return "Fine. Be that way!"
    else:
        return "Whatever."
