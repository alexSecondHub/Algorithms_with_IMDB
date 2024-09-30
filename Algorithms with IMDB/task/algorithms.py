import pandas as pd
import urllib.request
import time

# Const
INPUT_FILE_URL = 'https://stepik.org/media/attachments/lesson/518027/movies.csv'
TARGET_FILE = 'movies.csv'


# Functions
def linear_search(movies):
    #start = time.time()
    for title, rate in movies:
        if float(rate) == 6.0:
            print(title + ' - ' + rate)
    #end = time.time()
    #print('Linear search:', end - start)


def bubble_sort(movies):
    #start = time.time()
    length = len(movies)
    for i in range(length - 1):
        for j in range(length - 1):
            if float(movies[j][1]) > float(movies[j + 1][1]):
                # swap
                movies[j], movies[j + 1] = movies[j + 1], movies[j]
    #end = time.time()
    #print('Bubble sort:', end - start)
    return movies


def binary_search_half(movies, last):
    low = 0
    high = len(movies) - 1
    result_index = -1
    while low <= high:
        middle = (high + low) // 2
        title, rate = movies[middle][0], movies[middle][1]
        #print(middle, rate)
        if float(rate) == 6.0:
            result_index = middle
            if last:
                low = middle + 1
            else:
                high = middle - 1
        elif float(rate) < 6.0:
            low = middle + 1
        else:
            high = middle - 1
    return result_index


def merge_sort(movies):
    # Base case: if the list has one element or is empty, it's already sorted
    if len(movies) <= 1:
        return movies

    # Find the middle point and divide the array into two halves
    mid = len(movies) // 2
    left_half = movies[:mid]
    right_half = movies[mid:]

    # Recursively sort both halves
    left_sorted = merge_sort(left_half)
    right_sorted = merge_sort(right_half)

    # Merge the sorted halves
    return merge(left_sorted, right_sorted)


def merge(left, right):
    sorted_list = list()
    i = j = 0

    # Merge the two halves while maintaining order
    while i < len(left) and j < len(right):
        if left[i][1] < right[j][1]:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1

    # Add the remaining elements from the left half, if any
    while i < len(left):
        sorted_list.append(left[i])
        i += 1

    # Add the remaining elements from the right half, if any
    while j < len(right):
        sorted_list.append(right[j])
        j += 1

    return sorted_list


# Main
def main():
    try:
        urllib.request.urlretrieve(INPUT_FILE_URL, TARGET_FILE)
        movies_df = pd.read_csv(filepath_or_buffer=TARGET_FILE, header=None, dtype=str)
        # test_df = pd.DataFrame(movies_df.head(10))
        list_of_lists_movies = movies_df.values.tolist()

        #linear_search(list_of_lists_movies)
        #list_of_lists_movies = bubble_sort(list_of_lists_movies)
        list_of_lists_movies = merge_sort(list_of_lists_movies)
        #linear_search(list_of_lists_movies)

        result_index_high = binary_search_half(list_of_lists_movies, True)
        result_index_low = binary_search_half(list_of_lists_movies, False)
        for row_index in range(result_index_low, result_index_high + 1):
            print(list_of_lists_movies[row_index][0] + ' - ' + list_of_lists_movies[row_index][1])
    except Exception as error_text:
        print('Something went wrong:', error_text)


# Body
main()
