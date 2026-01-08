#f = input("File.txt")


with open("officequestion/File.txt", "r") as file: # provide absolute or relative path
    content = file.read()
    words = content.split()
    words_count = len(words)
    print("Number of words in file:", words_count)