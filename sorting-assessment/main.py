"""Assessment 3.7: Sorting Algorithms
Sorts the letters of a full name using Insertion Sort.

Rules:
- Two arrays: unsorted and sorted
- Duplicate letters are discarded
- Names with symbols are excluded (rejected)
"""

FULL_NAME = "Kathleen Campaner"


def build_unsorted_array(full_name):
    """Return a list of unique letters (first occurrence kept, order preserved).
    Raises ValueError if the name contains a symbol (anything other than
    letters and spaces)."""
    letters = []
    for ch in full_name:
        if ch == " ":
            continue
        if not ch.isalpha():
            raise ValueError(f"Name contains a symbol: {ch!r}")
        ch = ch.lower()
        if ch not in letters:  # discard duplicates
            letters.append(ch)
    return letters


def insertion_sort(arr):
    """Sort a copy of arr in ascending (A-Z) order using Insertion Sort."""
    result = arr.copy()
    for i in range(1, len(result)):
        key = result[i]
        j = i - 1
        while j >= 0 and result[j] > key:
            result[j + 1] = result[j]
            j -= 1
        result[j + 1] = key
    return result


def main():
    unsorted_array = build_unsorted_array(FULL_NAME)
    sorted_array = insertion_sort(unsorted_array)

    print("Full name:      ", FULL_NAME)
    print("Unsorted array: ", unsorted_array)
    print("Sorted array:   ", sorted_array)


if __name__ == "__main__":
    main()
