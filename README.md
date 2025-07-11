# 🔐 PasswordCracker – Multithreaded Brute Force Password Tester

A desktop application that **evaluates password strength** by attempting to crack it using brute-force and dictionary attacks.

This project uses **multi-process parallelization** to simulate how vulnerable certain passwords are, based on character types and dictionary appearance.

> Educational purpose only — Do **not** use for unauthorized access or real-world attacks.

---

## 🎯 Purpose

This tool helps users understand:

- How password composition (length, symbols, mixed case) impacts security
- The speed of brute-force attempts under multi-core systems
- The vulnerability of passwords present in known leaked dictionaries like **rockyou.txt**

---
> 💡 The full `rockyou.txt` is not included due to GitHub file size limits.  
You can download it here:
https://github.com/danielmiessler/SecLists/blob/master/Passwords/Leaked-Databases/rockyou.txt.tar.gz


## 🧠 Features

- ✅ Brute-force attacks with multiprocessing
- ✅ Character set selection (digits, letters, symbols, etc.)
- ✅ Dictionary attack using `rockyou.txt`
- ✅ Password strength estimation in time and iterations
- ✅ Modern GUI with real-time output (built with `tkinter`)
- ✅ Adjustable number of threads and attempts per thread
- ✅ Interactive explanation panel with clickable links

---

## 📺 Interface Preview

- GUI with input field for passwords
- Real-time logging panel (terminal emulator)
- Selection buttons for different character sets:
  - `Letters`, `Numbers`, `Letters+Numbers`, `All + Symbols`

---

## 🛠️ Technologies Used

- Python 3.x
- `tkinter` — GUI
- `multiprocessing`, `threading` — for parallel processing
- `PIL (Pillow)` — image support
- `string`, `itertools`, `ctypes` — character logic
- `rockyou.txt` — dictionary file (optional, user must provide)

---

## 📦 Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/PasswordCracker.git
cd PasswordCracker

