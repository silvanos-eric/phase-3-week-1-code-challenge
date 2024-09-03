def merge_dicts(dict1, dict2):
    # Create a new dictionary to hold the merged results
    merged_dict = dict1.copy()  # Start with the contents of dict1
    
    for key, value in dict2.items():
        if key in merged_dict:
            # If the key is already in merged_dict, sum the values
            merged_dict[key] += value
        else:
            # If the key is not in merged_dict, add it
            merged_dict[key] = value
    
    return merged_dict
