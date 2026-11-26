
text = input("Enter any sentence: ")

print("\n===== STRING ANALYZER =====")

print("Original:", text)
print("Uppercase:", text.upper())
print("Lowercase:", text.lower())
print("Title Case:", text.title())
print("Total Characters:", len(text))
print("Total Words:", len(text.split()))
print("Reversed:", text[::-1])
