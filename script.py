import json

# Define the content to be written to each JSON file
content = {
    "name": "EVAA Friend Card",
    "description": "Get benefits of being EVAA friend",
    "image": "https://telegra.ph/file/b3f72773d53da58cdadba.png"
}

# Loop through the range of file numbers (99 to 199)
for i in range(99, 200):  # 200 is exclusive, so it will stop at 199
    # Create a filename based on the current number
    filename = f"{i}.json"
    # Write the content to the file
    with open(filename, 'w') as f:
        json.dump(content, f, indent=4)  # indent=4 for pretty-printing
