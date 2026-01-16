import re

def translate(text):

    words = text.lower().split()
    translated_words = []
    

    for word in words:
        
        #rule 1 - word begins with a vowel, or starts with "xr" or "yt"
        if re.match(r"^(?:[aeiou]|xr|yt)", word):       
            pass
        #rule 3 - word starts with zero or more consonants followed by "qu"
        elif re.match(r"^[b-df-hj-np-tv-z]*qu", word):
            word = re.sub(r'^([b-df-hj-np-tv-z]*)(qu)(.*)$', r'\3\1\2', word)          
        
        #rule 4 - word starts with one or more consonants followed by "y"
        elif re.match(r"^[b-df-hj-np-tv-z]+y", word):
            word = re.sub(r'^([b-df-hj-np-tv-z]+)(y)(.*)$', r'\2\3\1', word)          
        
        #rule 2 - word begins with one or more consonants
        else:
            word = re.sub(r'^([b-df-hj-np-tv-z]+)(.*)$', r'\2\1', word)
        
        word += "ay"           
        translated_words.append(word)
        
    translation = " ".join(translated_words)
            
    return translation
       
