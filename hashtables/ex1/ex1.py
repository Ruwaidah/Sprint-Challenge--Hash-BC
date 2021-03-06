#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_retrieve)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    """
    YOUR CODE HERE
    """
    # loop through the list
    for i in range(length):
        item = weights[i]
        diff = hash_table_retrieve(ht, limit - item)
        if diff is None:
            hash_table_insert(ht, item, i)
        else:
            return (i, diff)

    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")


weights_3 = [4, 6, 10, 15, 16]
name = "ruwaidahalfakhri"
print(name[len(name)-5:])
print(get_indices_of_item_weights(weights_3, 5, 21))
