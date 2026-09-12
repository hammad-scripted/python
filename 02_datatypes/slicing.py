
word="Python"

print(word[0])
print(word[1])
print(word[2])
print(word[3])
print(word[4])
print(word[5])                  

print(word[-1])

print(word[0:2])
print(word[2:4])
print(word[4:6])

print(word[:2])  # 0 to 2
print(word[2:])  # 2 to end

print(word[::2])


# reversing a string
print(word[::-1])

# concatenation
print(word + " is a programming language")


print("ha"*3)


text="Python is a programming language"

print("Python" in text)
print("Java" in text)


# Escape characters when you need special behavior
tabbed = "Name:\tAlex"      # \t = tab
newline = "Line1\nLine2"    # \n = new line
quote = "She said \"hi\""   # \" = literal quote inside quotes
path = "C:\\Users\\Alex"    # \\ = literal backslash

print(quote)
print(path)
print(tabbed)
print(newline)