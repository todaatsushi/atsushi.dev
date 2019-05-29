def unpack(iter):
    """
    Input: List of multiple comma seperated values as string.
    
    Returns: list of unique values from the string.
    """
    unique = []

    for i in iter:
      unique.extend(i.split(','))

    return list(set(unique))