def suggest_subs(ingredient, subs_map, available):
    """
    Suggest a substitution for an ingredient from available ones.
    """
    if ingredient not in subs_map:
        return None
    for option in subs_map[ingredient]:
        if option in available:
            return option
    return None
