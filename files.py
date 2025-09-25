def count_words_in_file(filename):
    try:
        with open(filename, "r") as file:
            text = file.read()
            words = text.split()
            return len(words)
    except FileNotFoundError:
        print(f"File not found: {filename}")
        return 0
     
# print(count_words_in_file("sample.txt"))

def write_lines_to_output(strings):
    with open("output.txt", "w") as file:
        for s in strings:
            file.write(s + "\n")

write_lines_to_output(["hello", "world"])