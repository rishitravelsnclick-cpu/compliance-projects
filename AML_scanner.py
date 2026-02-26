# AML_scanner.py
# Simple AML transaction pattern detection

def aml_scan(transaction_amounts):
    suspicious = []
    for amt in transaction_amounts:
        if amt > 100000:  # threshold example
            suspicious.append(amt)
    return suspicious

if __name__ == "__main__":
    txns = [5000, 200000, 15000, 300000]
    flagged = aml_scan(txns)
    if flagged:
        print("Suspicious transactions:", flagged)
    else:
        print("No suspicious transactions found.")