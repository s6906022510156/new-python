
#--------------------------------------------------------------------------------------
# 1. indentify the languages that were chosen by all participants.
# 2. find the languages that were only chosen by a single participant.
# 3. determine the number of unique languages mentioned in the survey.
# 4. list the languages that were chosen by exactly two participants.
# 5. find participants who have the exact same set of favorite languages.

#section 2: survey analysis
survey_results = [
    ["python", "javascript", "c++"],
    ["python", "javascript", "c#"],
    ["python", "java"],
    ["python", "c++", "javascript"],
    ["python", "javascript", "c++", "java"],
]



survey_sets = [set(participant) for participant in survey_results]
print(survey_sets)

# 1. identify the languages that were chosen by all participants.
chosen_by_all = set.intersection(*survey_sets)
print("chosen by all participants:", chosen_by_all)


# 2. find the languages that were only chosen by a single participant.
all_languages = set.union(*survey_sets)

chosen_by_single_participant = set()

for language in all_languages:
    count = sum(language in participant for participant in survey_sets)

    if count == 1:
        chosen_by_single_participant.add(language)

print("chosen by a single participant:", chosen_by_single_participant)


# 3. determine the number of unique languages mentioned in the survey.
unique_languages_count = len(all_languages)
print("total unique languages:", unique_languages_count)


# 4. list the languages that were chosen by exactly two participants.
chosen_by_two_participants = set()

for language in all_languages:
    count = sum(language in participant for participant in survey_sets)

    if count == 2:
        chosen_by_two_participants.add(language)

print("chosen by exactly two participants:", chosen_by_two_participants)


# 5. find participants who have the exact same set of favorite languages.
same_favorites = []

for i in range(len(survey_sets)):
    for j in range(i + 1, len(survey_sets)):
        if survey_sets[i] == survey_sets[j]:
            same_favorites.append((i + 1, j + 1))

print("participants with the same favorite languages:", same_favorites)
