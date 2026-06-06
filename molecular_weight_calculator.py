import re

atomic_weights = {
    'H': 1.008, 'C': 12.011, 'N': 14.007,
    'O': 15.999, 'Na': 22.990, 'Cl': 35.453,
    'Ca': 40.078, 'K': 39.098, 'S': 32.06,
    'P': 30.974, 'Mg': 24.305, 'Fe': 55.845
}

def molecular_weight(formula):
    pattern = re.findall(r'([A-Z][a-z]?)(\d*)', formula)
    total = 0
    for element, count in pattern:
        if element in atomic_weights:
            total += atomic_weights[element] * (int(count) if count else 1)
        else:
            return f"Unknown element: {element}"
    return round(total, 3)

formula = input("Enter chemical formula (e.g. H2O): ")
result = molecular_weight(formula)
print(f"Molecular weight of {formula} = {result} g/mol")
