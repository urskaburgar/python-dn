with open("csv_files.py", "r") as list_files:
    contents = list_files.read().splitlines()

    for row in contents:
        row_data = row.split(",")
        print(f"{row_data[0]} is {row_data[1]} years old and {row_data[2]}.")
