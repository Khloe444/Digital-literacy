Problem statement: Digital literacy
Sub-problem: Lack of computer skills, no learning resources, and lack of ways to track progress
Sub-solution: Assessing computer skills, providing learning resources, and tracking progress

Start
    # Sub-Problem 1: Assessing Computer Skills
    Initialize user_age to 0
    Initialize computer_skills_level to ""
    Initialize has_computer_skills to False

    Prompt the user with "Please enter your age: "
    Read and store the user's age as user_age
    Prompt the user with "Please enter your computer skills level: "
    Read and store the user's computer skills level as computer_skills_level

    If computer_skills_level is equal to "basic", set has_computer_skills to True

    # Sub-Problem 2: Providing Learning Resources
    Initialize available_resources as ["Resource A", "Resource B", "Resource C"]
    Initialize selected_resource to ""
    Initialize resource_found to False

    Display "Available learning resources:"
    For each resource in available_resources, do:
        Display the resource

    Prompt the user with "Please select a learning resource: "
    Read and store the user's selection as selected_resource

    If selected_resource is in available_resources, set resource_found to True

    # Sub-Problem 3: Tracking Progress
    Initialize progress_percentage to 0.0
    Initialize completed_units to 0
    Initialize total_units to 10

    While completed_units is less than total_units, do:
        Display "Please complete the next learning unit."
        Increment completed_units by 1
        Calculate progress_percentage as (completed_units / total_units) * 100.0

    If completed_units is equal to total_units, display "Congratulations! You have completed all the learning units."

End
