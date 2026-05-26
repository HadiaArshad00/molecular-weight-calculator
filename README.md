# molecular-weight-calculator
Python tool to calculate molecular weight from chemical formulas
import re

atomic_weights = {
    "H": 1.008, "C": 12.011, "N": 14.007, "O": 15.999,
    "S": 32.06, "P": 30.974, "F": 18.998, "Cl": 35.45,
    "Br": 79.904, "Na": 22.990, "K": 39.098, "Ca": 40.078,
    "Mg": 24.305, "Fe": 55.845, "Zn": 65.38
}

def parse_formula(formula):
    pattern = r'([A-Z][a-z]?)(\d*)'
    matches = re.findall(pattern, formula)
    elements = {}
    for element, count in matches:
        if element:
            elements[element] = elements.get(element, 0) + (int(count) if count else 1)
    return elements

def calculate_mw(formula):
    elements = parse_formula(formula)
    total = 0
    for element, count in elements.items():
        if element not in atomic_weights:
            return f"Element '{element}' not found!"
        total += atomic_weights[element] * count
    return round(total, 3)

molecules = ["H2O", "C6H12O6", "NaCl", "C9H8O4"]

print("=== Molecular Weight Calculator ===")
print("Author: Hadia Arshad\n")
for m in molecules:
    print(f"{m} = {calculate_mw(m)} g/mol")
