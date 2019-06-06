from work.models import Project

def unpack(iter):
    """
    Input: List of multiple comma seperated values as string.
    
    Returns: list of unique values from the string.
    """
    unique = []

    for i in iter:
      unique.extend(i.split(','))

    return list(set(unique))


def get_current_or_dummy():
    """
    Gets the Project object with the current field set to True. In case of none,
    makes an empty dummy project to not cause errors and returns it.
    """
    # Dummy class
    class NoProj(object):
        # Great SO anwser - https://stackoverflow.com/a/652417
        def __init__(self, **kwargs):
            self.__dict__.update(kwargs)
    
    try:
        current = Project.objects.get(current=True)
    except Project.DoesNotExist:
        current = NoProj(current=False, name="None", description="Hmm... There's nothing in the works at the moment but that will almost certainly change very soon. Watch this space!")

    return current