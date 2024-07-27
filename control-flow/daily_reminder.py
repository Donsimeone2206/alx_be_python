task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()
reminder = f"'{task}' is a {priority} priority task"
match priority:
    case "high":
        reminder += " that requires your urgent attention!"
    case "low":
        reminder += " that can be done at your leisure."
if time_bound == "yes":
    reminder += " This task requires immediate attention today!"
print("Reminder:", reminder)
