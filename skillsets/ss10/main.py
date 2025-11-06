from functions import *

def main():
    print("Developer: Marcus Martin, Python Dictionaries Program")
    print('-' * 50)

    my_dictionary = create_dictionary()

    print('Print my_dictionary:', my_dictionary)
    print("Return view of dictionary's (key, value) pair:", get_items_view(my_dictionary))
    print('Return view object of all keys:', get_keys_view(my_dictionary))
    print('Return view object of all values:', get_values_view(my_dictionary))

    fname, lname = get_names(my_dictionary)
    print('Print only first and last names, using keys:', my_dictionary['fname'], my_dictionary['lname'])
    print('Print only first and last names, using get():', fname, lname)

    print('Count number of items (key:value pairs):', count_items(my_dictionary))

    remove_last_item(my_dictionary)
    print('After removing last item (popitem):', my_dictionary)

    delete_key(my_dictionary, 'major')
    print('After deleting major key:', my_dictionary)

    print('Return object type:', type(my_dictionary))

    clear_dictionary(my_dictionary)
    print('After clearing dictionary:', my_dictionary)


if __name__ == '__main__':
    main()
