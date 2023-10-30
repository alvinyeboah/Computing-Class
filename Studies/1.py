def find_palindromes(word_list):
    def is_palindrome(word):
        if len(word) < 2:
            return True
        elif word[0] != word[-1]:
            return False
        return is_palindrome(word[1:-1])

    palindromes = [word for word in word_list if is_palindrome(word.lower())]
    return palindromes

# Example usage
word_list = ["radar", "level", "python", "madam", "civic", "hello"]
palindromes = find_palindromes(word_list)

print("Palindromes found:", palindromes)
