# Bai 7
# Capital letters after the dot
sentence = input().strip()

def capitalizeAfterDot(sentence: str) -> str:
    result = []
    i = 0
    while i < len(sentence):
        if i >= 1 and sentence[i - 1] == '.' and sentence[i] == ' ':
            result.append(sentence[i])
            
            if i + 1 < len(sentence) and sentence[i + 1].isalpha():
                result.append(sentence[i + 1].upper())
                i += 2
                continue
        
        result.append(sentence[i])
        i += 1

    return ''.join(result)

print(capitalizeAfterDot(sentence))