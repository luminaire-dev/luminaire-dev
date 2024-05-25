import datetime

# Read the current README content
with open("README.md", "r") as file:
    readme_content = file.readlines()

# Generate the greeting
today = datetime.datetime.now()
day_of_week = today.strftime("%A")
greeting = f"Hello! Today is {day_of_week}.\n"

# Insert the greeting at the top of the README
readme_content.insert(1, greeting)  # Adjust the index as needed

# Write the updated content back to the README
with open("README.md", "w") as file:
    file.writelines(readme_content)
