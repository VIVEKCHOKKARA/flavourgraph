def greedy_match(available, recipes):
    """
    Pick recipe with the maximum overlap with available ingredients.
    """
    best = None
    best_score = -1
    for recipe in recipes:
        score = sum(1 for i in recipe["ingredients"] if i in available)
        if score > best_score:
            best_score = score
            best = recipe
    return best


def backtracking(available, recipes, idx=0, chosen=None):
    """
    Backtracking search to find a sequence of recipes covering ingredients.
    """
    if chosen is None:
        chosen = []

    if idx >= len(recipes):
        return chosen

    recipe = recipes[idx]
    if all(i in available for i in recipe["ingredients"]):
        with_recipe = backtracking(available, recipes, idx + 1, chosen + [recipe])
        without_recipe = backtracking(available, recipes, idx + 1, chosen)
        return with_recipe if len(with_recipe) > len(without_recipe) else without_recipe
    else:
        return backtracking(available, recipes, idx + 1, chosen)
