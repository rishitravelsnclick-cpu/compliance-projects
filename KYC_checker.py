# 1. KYC Checker
# Define a banned countries list first
banned_list = {"Iran", "North Korea", "Syria"}

class Customer:
    def __init__(self, name, age, country):
        self.name = name
        self.age = age
        self.country = country
    
    def kyc_check(self):
        if self.age >= 18 and self.country not in banned_list:
            return "KYC PASSED"
        else:
            return "KYC FAILED"
        
cust1 = Customer("Rahul", 32, "India")
cust2 = Customer("Ali", 17, "Iran")
cust3 = Customer("John", 70, "USA")

print(cust1.kyc_check())   
print(cust2.kyc_check()) 
print(cust3.kyc_check())   



# 2. AML Transaction Scanner
def aml_check(amount, txn_type):
    if amount > 1000000 or txn_type.upper() == "CASH DEPOSIT":
        return "SUSPICIOUS"
    else:
        return "NORMAL"

# Multiple transactions stored properly
transactions = [
    {"amount": 20000000, "txn_type": "ONLINE"},
    {"amount": 2000, "txn_type": "CASH DEPOSIT"},
    {"amount": 2000, "txn_type": "ONLINE"}
]

# Loop through transactions and check each one
for t in transactions:
    print(f"Txn: {t} → {aml_check(t['amount'], t['txn_type'])}")

 


# 3. PEP Flagging System
class PEP:
    def __init__(self, name):
        self.name = name

    def pep_check(self):
        if self.name in pep_list:
            return "HIGH RISK"
        else:
            return "NORMAL"
        
pep_list = {"Rahul Gandhi", "Narendra Modi", "Joe Biden"}

pep1 = PEP("Joe Biden")
pep2 = PEP("Robin")
pep3 = PEP("Narendra Modi")
pep4 = PEP("Luv")
pep5 = PEP("Rahul Gandhi")

        
print (pep1.pep_check())
print (pep2.pep_check())
print (pep3.pep_check())
print (pep4.pep_check())
print (pep5.pep_check())
    











       

