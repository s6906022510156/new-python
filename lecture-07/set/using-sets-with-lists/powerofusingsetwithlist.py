
attendance_week = [
    ["alice", "bob", "charlie", "david"],
    ["alice", "charlie", "david"],
    ["alice", "bob", "david"],
    ["alice", "david", "eve"],
    ["bob", "charlie", "david"]
]

# 1. find the set of students who were present every day.
# 2. determine the set of students who were absent at least one day.
# 3. create a list of student who were present on the first day but absent on the last day.
# 4. calculate the total number of unique students who attended at least one day.

attendance_sets = [set(day) for day in attendance_week]
print(attendance_sets)

present_every_day = set.intersection(*attendance_sets)
print("present every day:", present_every_day)

all_students = set.union(*attendance_sets)
absent_at_least_one_day = all_students - present_every_day
print("absent at least one day:", absent_at_least_one_day)

first_day_present = attendance_sets[0]
last_day_present = attendance_sets[-1]
first_day_but_not_last = list(first_day_present - last_day_present)
print("present on first day but absent on last day:", first_day_but_not_last)

unique_students_count = len(all_students)
print("total unique students", unique_students_count)



