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
> 💡 **Note:** The full `rockyou.txt` file is not included in this repository due to GitHub's file size limits.

To enable the dictionary-based password testing feature, follow these steps:

1. Download the compressed file from the following official source:  
   🔗 https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt

2. Rename the extracted file to `rockyou.txt` .

3. Place the `rockyou.txt` file in the **same directory** as `versao_multiprocess.py`.

Once this is done, the dictionary attack feature will automatically load the file and compare input passwords against it.



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

## 👤 Author

João Vitor de Oliveira Lima

📧 ghostcode541@gmail.com

🔗 [LinkedIn](www.linkedin.com/in/joãovitordeoliveira-lima) --> www.linkedin.com/in/joãovitordeoliveira-lima

## 📦 Installation

1. Clone the repository:

```bash
git clone https://github.com/JOHNcoding9/PasswordCracker.git
cd PasswordCracker

