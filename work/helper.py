def unpack(iter):
    unique = []

    for i in iter:
      unique.extend(i.split(','))

    return list(set(unique))