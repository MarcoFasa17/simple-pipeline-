def count_vowels(word):
    return sum(1 for ch in word.lower() if ch in 'aeiou')
if __name__ == "__main__":
    print(count_vowels(input()))