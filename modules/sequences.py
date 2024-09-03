def sort_by_age(person_list):
    # Sort the list of tuples by the second element (age) of each tuple
    return sorted(person_list, key=lambda person: person[1])
