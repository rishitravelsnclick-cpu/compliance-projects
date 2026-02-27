# compliance-projects

![Python](https://img.shields.io/badge/Python-3.10-blue)
![GitHub](https://img.shields.io/badge/GitHub-Repo-success)
![Status](https://img.shields.io/badge/Compliance-Automation-green)

A collection of Python-based mini systems for AML/KYC automation, built for RegTech and FinTech interviews.



## Projects
- **KYC Checker** → Age & country validation  
- **AML Scanner** → Transaction pattern detection  
- **PEP Flagger** → Politically Exposed Persons screening  
- **Risk Engine** → Combined scoring system (KYC + AML + PEP)

## Features
- Python OOP design
- Robust error handling
- Recruiter-friendly structure
- Real-world compliance mapping

## How to Run

<img width="1266" height="537" alt="image" src="https://github.com/user-attachments/assets/95b957af-d52b-4391-b77f-762ed5f4cfe2" />

## Example Run
**Input:**
Name: John Doe  
Age: 17  
Country: USA

**Output:**

KYC Failed: Age below threshold


## Risk Engine Example
**Input:**
Age = 17, Country = USA, Transactions = [5000, 200000], Name = John Doe  

**Output:**
Final Risk Score: 160

## Roadmap
- [x] KYC Checker  
- [x] AML Scanner  
- [x] PEP Flagger  
- [x] Risk Engine  
- [ ] External dataset integration  
- [ ] Dashboard visualization  
- [ ] API endpoints for real-time checks  


Clone the repo and run:
```bash
python KYC_checker.py
