def find_anagrams(word, candidates):
    anagrams = [candidate for candidate in candidates if sorted(word.lower()) == sorted(candidate.lower()) and word.lower() != candidate.lower()]
    return anagrams
             
    
