def response(hey_bob):

    #removing white space
    hey_bob = hey_bob.strip()
    
    #check for all caps
    yell_at_bob = hey_bob.isupper()

    #check for ending with a question mark
    question_for_bob = hey_bob.endswith("?")

    #check for nothing or various combinations of whitespace characters
    silence_at_bob = len(hey_bob) == 0

    if yell_at_bob:
        if question_for_bob:
            return "Calm down, I know what I'm doing!"
        else:
            return "Whoa, chill out!"
        
    elif question_for_bob:
        return "Sure."

    elif silence_at_bob:
        return "Fine. Be that way!"
    
    else:
        return "Whatever."

