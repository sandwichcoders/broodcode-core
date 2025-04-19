def get_vegan_sandwiches(sandwiches: dict[str, tuple[str, str, int, str]]) -> list:
    """
    Return a list of (possible) vegan sandwiches.
    Args:
        sandwiches: Available price calculated sandwiches

    Returns: A list of (possible) vegan sandwiches
    """
    vegan_sandwiches = []

    for sandwich in sandwiches.values():
        if sandwich[0] in vegan_sandwiches or f'{sandwich[0]} (Can be made vegan on request)' in vegan_sandwiches:
            continue

        title = sandwich[0].split(" ")
        subtitle = sandwich[-1].split(" ")
        if _is_vegan(title):
            vegan_sandwiches.append(sandwich[0])
        elif _is_vegan(subtitle):
            vegan_sandwiches.append(f'{sandwich[0]} (Can be made vegan on request)')

    return vegan_sandwiches


def _is_vegan(sentence):
    for word in sentence:
        if word.lower() == "(vegan)" or word.lower() == "vegan?":
            return True
    return False