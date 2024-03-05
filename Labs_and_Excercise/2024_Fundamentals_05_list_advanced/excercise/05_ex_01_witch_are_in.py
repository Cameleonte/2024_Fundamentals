first_string = input().split(', ')
second_string = input().split(', ')
new_list = []
for word in first_string:
    for word2 in second_string:
        if word in word2:
            new_list.append(word)
            break
print(new_list)

check_for_the_words = [element if element in word else 'no' for element in first_string for word in second_string]
new_list1 = list(set(element for element in check_for_the_words if element != 'no'))
print(new_list1)
