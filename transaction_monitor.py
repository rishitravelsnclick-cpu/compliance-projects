import statistics

class TransactionMonitor:
    def __init__(self):
        self.account_profiles = {}  # store average transaction values per account

    def check_transaction(self, account_id, amount):
        notes = []
        status = "Normal"

        # Step 1: Flag transactions above 100k
        if amount > 100000:
            status = "Suspicious"
            notes.append("Transaction above 100k")

        # Step 2: Detect structuring (regular payments near 90k–100k)
        if 90000 <= amount < 100000:
            notes.append("Possible structuring: repeated payments near 100k")

        # Step 3: Detect unusual spikes compared to account profile
        if account_id in self.account_profiles:
            avg_amount = statistics.mean(self.account_profiles[account_id])
            if amount > 3 * avg_amount:  # heuristic: 3x average = unusual
                notes.append("Unusual spike compared to customer profile")

        # Update account profile history
        if account_id not in self.account_profiles:
            self.account_profiles[account_id] = []
        self.account_profiles[account_id].append(amount)

        return {
            "Account": account_id,
            "Amount": amount,
            "Status": status,
            "Notes": notes
        }


# Example usage
monitor = TransactionMonitor()

transactions = [
    ("CUST001", 50000),
    ("CUST001", 95000),
    ("CUST001", 120000),
    ("CUST002", 20000),
    ("CUST002", 300000)  # spike compared to profile
]

for acc, amt in transactions:
    result = monitor.check_transaction(acc, amt)
    print(result)