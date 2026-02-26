# PEP_flagger.py
# Simple Politically Exposed Persons (PEP) screening

PEP_LIST = ["John Doe", "Jane Smith", "Carlos Perez"]

def pep_check(name):
    if name in PEP_LIST:
        return f"{name} flagged as PEP"
    else:
        return f"{name} cleared"

if __name__ == "__main__":
    test_names = ["John Doe", "Alice Brown"]
    for n in test_names:
        print(pep_check(n))