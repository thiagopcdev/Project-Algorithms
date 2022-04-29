from challenges.helper.merge_sort import merge_sort


def is_anagram(first_string, second_string):

    if first_string == '' or second_string == '':
        return False

    first_list = list(first_string.casefold())
    second_list = list(second_string.casefold())

    first_list = merge_sort(first_list)
    second_list = merge_sort(second_list)

    anagram_stats = True

    for i in range(len(first_string)):
        if first_list[i] != second_list[i]:
            anagram_stats = False
            break

    return anagram_stats
