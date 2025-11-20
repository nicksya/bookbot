# get file content as string
def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents

# count the number of words in the string
def get_num_words(path_to_file):
    text = get_book_text(path_to_file)
    text_list = text.split()
    return len(text_list)

# get character count as dictionary
def get_book_stats(path_to_file):
    text = get_book_text(path_to_file)
    words = text.split()
    stats = {}
    for word in words:
        for char in word:
            char = char.lower()
            if char in stats:
                stats[char] += 1
            else:
                stats[char] = 1
    return stats 

def sort_on(items):
    return items["num"]

# get character count as list of dictionaries
# e.g. {"char": "b", "num": 4868}
def get_book_stats_sorted(path_to_file):
    stats_dict = get_book_stats(path_to_file)
    stats_sorted = []
    for key in stats_dict:
        if key.isalpha():
            # print(f"key: {key} value: {stats[key]}")
            new_dict = {}
            new_dict["char"] = key
            new_dict["num"] = stats_dict[key]
            stats_sorted.append(new_dict)
    stats_sorted.sort(reverse=True, key=sort_on)
    return stats_sorted
