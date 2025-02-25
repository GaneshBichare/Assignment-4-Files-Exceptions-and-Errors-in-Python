file = "sample.txt"
if file == "sample.txt":
    with open("sample.txt", "r") as file:
        print("Reading file content:")
        for i, line in enumerate(file, start=1):
             print(f"Line {i}: {line.strip()}")
else:
     print(f"Error: The file '{file}' was not found.")
