def make_dict(arr1, arr2):
  new_dict = {}
new_dict = dict(zip(name, favorite_animal))
return new_dict


def new_dict(arr1, arr2):
    return dict(zip(arr1, arr2 + [None] * (len(arr1) - len(arr2))))
