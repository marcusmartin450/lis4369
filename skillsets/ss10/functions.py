def create_dictionary():
    """Create and return the initial student dictionary."""
    return {
        'fname': 'Mark',
        'lname': 'Jowett',
        'degree': 'BSIT',
        'major': 'IT',
        'gpa': 4.0
    }

def get_items_view(d):
    """Return a view of (key, value) pairs."""
    return d.items()

def get_keys_view(d):
    """Return a view of all keys."""
    return d.keys()

def get_values_view(d):
    """Return a view of all values."""
    return d.values()

def get_names(d):
    """Return first and last name safely."""
    return d.get('fname'), d.get('lname')

def count_items(d):
    """Return number of key:value pairs."""
    return len(d)

def remove_last_item(d):
    """Remove the last inserted item (if any) and return the dict."""
    if d:
        d.popitem()
    return d

def delete_key(d, key):
    """Delete a key if it exists; return the dict."""
    if key in d:
        del d[key]
    return d

def clear_dictionary(d):
    """Clear all items and return the dict."""
    d.clear()
    return d
