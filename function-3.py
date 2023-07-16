# Sub-Problem 1: Assessing Computer Skills
user_age = 0
computer_skills_level = ""
has_computer_skills = False

user_age = int(input("Please enter your age: "))
computer_skills_level = input("Please enter your computer skills level: ")

if computer_skills_level == "basic":
    has_computer_skills = True

# Sub-Problem 2: Providing Learning Resources
available_resources = ["Resource A", "Resource B", "Resource C"]
selected_resource = ""
resource_found = False

for resource in available_resources:
    print(resource)

selected_resource = input("Please select a learning resource: ")

if selected_resource in available_resources:
    resource_found = True

# Sub-Problem 3: Tracking Progress
progress_percentage = 0.0
completed_units = 0
total_units = 10

while completed_units < total_units:
    print("Please complete the next learning unit.")
    completed_units += 1
    progress_percentage = (completed_units / total_units) * 100.0

    if completed_units == total_units:
        print("Congratulations! You have completed all the learning units.")
