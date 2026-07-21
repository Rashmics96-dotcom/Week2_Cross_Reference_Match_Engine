# Week 2 - Cross Reference Match Engine

## Project Overview

This project demonstrates relational data matching and cross-referencing using pure Python. Two independent datasets are processed and merged based on a common Student ID to generate a unified performance summary.

The project is developed without using external libraries such as Pandas or NumPy, following the internship guidelines.

---

## Objective

- Read two separate datasets.
- Match records using Student ID.
- Merge related information into a single summary.
- Handle missing records gracefully.
- Implement the solution using only core Python.

---

## Project Structure

```
Week2_Cross_Reference_Match_Engine/
│── students.txt
│── marks.txt
│── cross_reference.py
│── README.md
```

---

## Input Dataset 1 (students.txt)

```
101,Alice,CSE
102,Bob,AIML
103,Charlie,ECE
104,David,ISE
```

---

## Input Dataset 2 (marks.txt)

```
101,85
102,91
104,78
105,88
```

---

## Execution Steps

1. Read student records from students.txt.
2. Read marks from marks.txt.
3. Cross-reference both datasets using Student ID.
4. Merge matching records.
5. Display "Marks Not Found" when marks are unavailable.
6. Display students present in marks.txt but missing in students.txt.

---

## Program Output

```
========== STUDENT PERFORMANCE SUMMARY ==========

Student ID : 101
Name       : Alice
Department : CSE
Marks      : 85
----------------------------------------

Student ID : 102
Name       : Bob
Department : AIML
Marks      : 91
----------------------------------------

Student ID : 103
Name       : Charlie
Department : ECE
Marks      : Marks Not Found
----------------------------------------

Student ID : 104
Name       : David
Department : ISE
Marks      : 78
----------------------------------------

Students available in marks.txt but missing in students.txt

Student ID : 105
Marks      : 88
```

---

## Technologies Used

- Python
- File Handling
- Lists
- Dictionaries
- Loops
- Conditional Statements
- Functions

---

## Key Features

- Pure Python implementation
- No Pandas or NumPy
- Efficient dictionary-based lookup
- Handles missing records
- Clean modular code
- Easy to understand and maintain

---

## Execution Snapshot

! [Program Output](output.png)

---

## Author

**Rashmi**
