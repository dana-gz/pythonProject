def lowercase_decorator(txt):
    def lower_case():
        return txt().lower()
    return lower_case

@lowercase_decorator
def recipe():
    return "Amerykańskie puszyste placuszki - Klasyczne, proste do wykonania, najlepsze na śniadanie lub brunch"
print(recipe())
