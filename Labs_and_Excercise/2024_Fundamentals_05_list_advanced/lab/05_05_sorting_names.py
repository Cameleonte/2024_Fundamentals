# def length_sort(z):
#     return len(z)
#
#
# input_names = input().split(', ')
# input_names.sort()
# input_names.sort(reverse=True, key=length_sort)
# print(input_names)

def sort_names():
    names = input().split(', ')
    sorted_names = sorted(names, key=lambda x: (-len(x), x))
    return sorted_names


print(sort_names())
