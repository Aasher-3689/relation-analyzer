## Contents

1. [Title](#project-title)
2. [Description](#project-description)
3. [Dependencies](#dependencies)  
4. [Installation](#installation-instructions)  
5. [Usage Examples](#usage-example)  
6. [Project Structure](#project-structure)  
7. [Contributors](#contributors)
8. [Demo Video](#demo-video)

---

## Project Title
Relation Analyzer and classifier

---

## Project Description
It allows users to input a **set** and a **relation**, analyze fundamental relation properties (reflexive, symmetric, transitive, etc.), and classify relations as equivalence relations or partial orders.
All results are displayed in a **clear tabular format**.

---

## Dependencies
This project requires Python 3.6 or higher.
### Check Python version
```
python --version
```

---

## Installation Instructions

### Clone the repository
```
git clone https://github.com/Aasher-3689/relation-analyzer.git
```
### Navigate to the project directory
```
cd relation-analyzer
```

### Run the main program
```
python main.py
```

---

## Usage Example
### 1. Run the main program
```
python main.py
```
#### Sample Interaction
<img width="1021" height="923" alt="main" src="https://github.com/user-attachments/assets/5f1beed9-a630-4ad0-8c01-00cc6f612f8a" />

### 2. Run all Tests
Each test prints Passed/Failed to verify correctness.
```
python tests/main.py
```
#### Sample Interaction
<img width="1021" height="923" alt="test-main" src="https://github.com/user-attachments/assets/4ea660e4-5447-4ab3-a4c1-71be9dcc0970" />

---

## Project Structure
```
├── analyzers.py
├── classifiers.py
├── inputs.py
├── main.py
├── tests/
│   ├── classification.py
│   ├── reflexive.py
│   ├── symmetric.py
│   ├── transitive.py
│   └── main.py
└── README.md
```
---

## Contributors
*University of Engineering and Technology, Lahore*
| Name             | Roll#       |
|------------------|-------------|
| Abdullah Ahmad   | 2025-CS-51  |
| Muhammad Aasher  | 2025-CS-16  |

---

## Demo Video
Youtube: https://youtu.be/4BrXpQseAfU

---
