def translate(text):
    words = []
    for word in text.split():
        if word.startswith(('a', 'e', 'i', 'o', 'u', 'xr', 'yt')):
            words.append(word + 'ay')
        else:
            for i,char in enumerate(word):
                if char == 'u' and word[i-1] == 'q':
                    words.append(word[i+1:] + word[:i+1] + 'ay')
                    break
                elif char in ('aeiou'):
                    words.append(word[i:] + word[:i] + 'ay')
                    break
                elif char == 'y' and i > 0:
                    words.append(word[i:] + word[:i] + 'ay')
                    break
    return ' '.join(words)
            
