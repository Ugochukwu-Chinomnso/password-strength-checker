# Password Strength Checker

A lightweight Python command-line utility that evaluates password security strength based on length, digits, uppercase letters, and special characters.

## Project Overview

This project demonstrates how Python can validate password security policies and classify strength into **Weak**, **Medium**, or **Strong**. 

The program validates inputs against four security criteria:
* **Minimum Length:** At least 8 characters
* **Numeric Characters:** At least one digit (`0–9`)
* **Uppercase Letters:** At least one uppercase letter (`A–Z`)
* **Special Characters:** At least one symbol or punctuation mark (evaluated via Unicode character categories)

Each requirement met adds +1 point toward the final strength score.

---

## How It Works

1. **Masked Input:** Prompts for input using Python's standard `getpass` module to keep passwords hidden in the terminal.
2. **Character Inspection:** Analyzes character composition using built-in string methods and Unicode properties (`unicodedata`).
3. **Scoring:** Calculates an aggregate score out of 4 points.
4. **Feedback & Rating:** Outputs real-time warnings for missing criteria alongside the final score and classification.

---

## Strength Classification

| Score | Classification | Assessment |
| :---: | :--- | :--- |
| **0 – 1** | Weak | High vulnerability; fails most standard complexity checks |
| **2 – 3** | Medium | Moderate security; lacks one or two complexity requirements |
| **4** | Strong | Meets all standard complexity and length checks |