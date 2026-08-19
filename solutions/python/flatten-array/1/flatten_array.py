def flatten(iterable):
    final_list = []
    for item in iterable:
        if item is not None:
            if isinstance(item, list):
                final_list.extend(flatten(item))
            else:
                final_list.append(item)
    return final_list