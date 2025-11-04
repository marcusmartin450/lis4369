def main():
    print("Developer: Marcus Martin, Python Dictionaries Program")
    

    my_dictionary = {
        'fname': 'Mark',
        'lname': 'Jowett',
        'degree': 'BSIT',
        'major': 'IT',
        'gpa': 4.0
    }
    
    print('Print my_dictionary:', my_dictionary)
    print('Return view of dictionary\'s (key, value) pair:', my_dictionary.items())
    print('Return view object of all keys:', my_dictionary.keys())
    print('Return view object of all values:', my_dictionary.values())
    
    print('Print only first and last names, using keys:', my_dictionary['fname'], my_dictionary['lname'])
    print('Print only first and last names, using get():', my_dictionary.get('fname'), my_dictionary.get('lname'))
    
    print('Count number of items (key:value pairs):', len(my_dictionary))
    
    my_dictionary.popitem()
    print('After removing last item (popitem):', my_dictionary)
    
    del my_dictionary['major']
    print('After deleting major key:', my_dictionary)
    
    print('Return object type:', type(my_dictionary))
    
    my_dictionary.clear()
    print('After clearing dictionary:', my_dictionary)
