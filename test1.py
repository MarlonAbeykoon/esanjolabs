import requests
import json
import copy


ids = []
tree = []
tree_ar = []


def flatten(structure, flattened=None):
    '''

    :param structure: Dict to make it flatten
    :param flattened: Already flattened list of dicts if available
    :return: Final list fattened dicts
    '''

    if flattened is None:
        flattened = []

    flat_d = copy.deepcopy(structure)  # Deep copied to make the copying process recursive for its children
    flat_d['objectID'] = flat_d.pop('id')  # renamed the key as objectID
    del(flat_d['children_data'])  # removed the key children_data
    if 'ids' and 'tree' not in flat_d:  # If need keys are absent create them
        flat_d['ids'] = []
        flat_d['tree'] = ''
        flat_d['tree_ar'] = ''
    ids.append(structure['id'])  # Assign the current dict id
    tree.append(structure['name'])  # Assign current dict name
    tree_ar.append('' if structure['name_ar'] is None else structure['name_ar'])  # Replaced None with an empty string
    flat_d['ids'].extend(ids)  # merge two lists
    flat_d['tree'] = ' > '.join(tree)
    flat_d['tree_ar'] = ' > '.join(tree_ar)
    flattened.append(flat_d)
    if structure['children_data']:  # check the current dict has children
        for i, item in enumerate(structure['children_data']):
            flatten(item, flattened)
        del ids[-1], tree[-1], tree_ar[-1]  # Clear the closest parent_id, tree and tree_ar after all same level
    else:
        del ids[-1], tree[-1], tree_ar[-1]  # Delete the current id and name from the list if it has no children

    return flattened


def get_data():

    r = requests.get('https://res.cloudinary.com/esanjolabs/raw/upload/v1529967088/tests/categories-test.json')
    return r.json()['children_data'][0]['children_data']


def main():

    data = get_data()
    
    flatten_data = []

    for elem in data:  # Iterate data for each dictionary
        flatten_data.extend(flatten(elem))
        del ids[:], tree[:], tree_ar[:]  # Empty the list after each iteration
    print(json.dumps(flatten_data, ensure_ascii=False))  # Final result


if __name__ == "__main__":
    main()
