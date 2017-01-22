import csv
import time

HOUNDS_OF_BASKERVILLE_FILE = './HoundOfBaskerville.txt'
IS_COUNTER = True
COUNTER = 0

def read(filename):
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        data = f.read().replace('\n', ' ').lower()

    f.close()

    return data


# create a suffix array with suffix returns array of tuples
def suffix(text):
    suffix_array = []
    for i in range(0, len(text)):
        suffix_array.append((text[i:len(text)], i))

    suffix_array = sorted(suffix_array)

    return suffix_array


# creates the suffix array out of the array with suffix array tuples
def create_idx_list(suffix_array_tuples):
    suffix_array_idx = []
    for key, value in suffix_array_tuples:
        suffix_array_idx.append(value)

    return suffix_array_idx


# calculates the longest common prefix of two terms
def lcp(term1, term2):
    for i in xrange(min(len(term1), len(term2))):
        if term1[i] != term2[i]:
            return i

    return min(len(term1), len(term2))


# creates an lcp array of a given string
def create_lcp_array(str, suffix_array):
    size = len(str)
    reverse_suffix_array = range(0,size)

    for x in range(0,size):
        reverse_suffix_array[suffix_array[x]] = x

    lcp = size * [None]
    h = 0
    for i in range(size):
        if reverse_suffix_array[i] > 0:
            j = suffix_array[reverse_suffix_array[i] - 1]
            while i != size - h and j != size - h and str[i + h] == str[j + h]:
                h += 1
            lcp[reverse_suffix_array[i]] = h
            if h > 0:
                h -= 1
    if size > 0:
        lcp.pop(0)
    return lcp


# compares a term with another term returnes a boolean
def compare_serachterm_anyterm(searchterm, term_to_check, searchterm_length):
    # True if searchterm and term_to_check is equal (hallo, hallo)
    # True if searchterm is in term_to_check (hal, hallo)
    # True if last char of searchterm is smaller than last char of term_to_check (hay, hallo) => false
    global COUNTER

    i = 0
    while i < searchterm_length and searchterm[i] == term_to_check[i]:
        if IS_COUNTER:
            COUNTER += 1

        i += 1
    if i == searchterm_length:
        return True
    else:
        return searchterm[i] < term_to_check[i]


# simple binary search returns the first appearance in the suffix array
def simple_binary_search(suffix_array, text, searchterm):
    global COUNTER

    term_length = len(searchterm)
    text_length = len(text)

    if IS_COUNTER:
        COUNTER += 1

    left = 0
    right = text_length - 1

    while right - left > 1:
        if IS_COUNTER:
            COUNTER += 1

        middle = (left + right) // 2

        # search left right border
        if compare_serachterm_anyterm(searchterm, text[suffix_array[middle]:], term_length):
            right = middle

        else:
            left = middle

    # right is the last value that gets updated
    result = right

    return result


# counts the words with an lcp and the first appearance in a suffix array
def count_word_appearance(suffix_array, text, searchterm):
    global COUNTER

    position_suffix_array = simple_binary_search(suffix_array, text, searchterm)
    lcp_array = create_lcp_array(text, suffix_array)
    counter = 0

    for n in lcp_array[position_suffix_array:]:
        if IS_COUNTER:
            COUNTER += 1

        if n < len(searchterm):
            counter += 1
            break

        counter += 1

    return counter


if __name__ == '__main__':
    text = read(HOUNDS_OF_BASKERVILLE_FILE)

    suffix_array_tuple = suffix(text)

    sa = create_idx_list(suffix_array_tuple)
    search_term = 'sherlock'
    search_term = 'watson'
    search_term = 'hound'


    time_start = time.time()
    COUNTER = 0
    print count_word_appearance(sa, text, search_term.lower())
    time_end = time.time()
    elapsed_time = time_end - time_start
    print COUNTER
    print elapsed_time
