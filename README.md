# Expense Tracker with WhatsApp Import

A Python-based command-line application that helps you track personal expenses, analyze spending habits, manage monthly budgets, and automatically import real payment data from exported WhatsApp chat logs.

This project is designed for users who want a simple, offline, and practical way to manage expenses without relying on third-party apps.

---

## Features

- Add, view, edit, and delete expenses (CRUD operations)
- Persistent data storage using JSON
- Category-wise expense analysis
- Month-wise expense summaries
- Monthly budget setting with overspending alerts
- Automatic expense extraction from exported WhatsApp chat `.txt` files

---

## WhatsApp Chat Import

Since WhatsApp messages are end-to-end encrypted, this project works with **exported chat logs**.

The application scans chat text files and detects real payment-related messages, converting them into structured expense entries.

### Supported Message Format (Example)

```text
[20/12/25, 3:48:51 PM] You: Paid ₹120 to Swiggy
```

Detected data:
- Amount: ₹120  
- Category: Food  
- Description: Swiggy  
- Date: 2025-12-20  

---

## How to Run

1. Ensure Python is installed on your system (Python 3 recommended).
2. Clone this repository or download the project files.
3. Open a terminal in the project directory.
4. Run the application:

```bash
python project1.py
```

## Data Storage

All expense data is stored locally in a JSON file.  
This makes the application lightweight, offline-friendly, and easy to extend.

---

## Tech Stack

- Python
- JSON (data persistence)
- File handling and text parsing
- Command-line interface (CLI)

---

## Project Use Cases

- Personal expense tracking
- Learning Python file handling
- Practicing JSON-based persistence
- Real-world text parsing from chat data
- Beginner-friendly finance automation project

---

## Future Improvements

- Export expenses to CSV
- Graph-based expense visualization
- Improved WhatsApp message pattern detection
- Multi-user support
- Smarter category prediction
