# Password_strength_checker_project
Cybersecurity project that evaluates password strength using character analysis, scoring system, and rockyou password list detection.


This project was created as part of a cybersecurity learning project to demonstrate basic password security analysis techniques.

## Features

- Detects:
  - Uppercase letters
  - Lowercase letters
  - Numbers
  - Special characters
- Checks password length
- Compares password against the **rockyou password list**
- Uses a **score-based system** to determine password strength
- Outputs password rating:
  - Weak
  - Medium
  - Strong

## How It Works

The program evaluates password security using several checks:

1. Password length
2. Character diversity (uppercase, lowercase, numbers, symbols)
3. Presence in common password lists (rockyou.txt)
4. Score calculation based on password complexity

Each condition adds points to the total score.

Example scoring logic:

- Length ≥ 8 → +1
- Contains uppercase → +1
- Contains lowercase → +1
- Contains number → +1
- Contains special character → +1

Total score determines strength:

| Score | Strength |
|------|---------|
| 0–1 | Weak |
| 2-3| Medium |
| 4-5 | Strong |

## Example Output

```

Loading password list...

Enter your password: Password123

This password is too common! Choose another.

Enter your password: #Pa$sword123

Score: 5
Password Strength: Strong
```

## Installation

Clone the repository:

```
git clone https://github.com/neringakvaukaite-bot/password_strength_checker.git
```

Move into the project folder:

```
cd password-strength-checker
```

Run the script:

```
python3 password_strength.py
```

## Requirements

- Python 3
- rockyou.txt wordlist (optional but recommended)

## Security Concepts Demonstrated

This project demonstrates several cybersecurity concepts:

- Password complexity analysis
- Wordlist-based password detection
- Basic password security evaluation
- Defensive security practices

## Educational Purpose

This tool is intended for **educational and security awareness purposes only**.

## Author

Neringa Kvaukaite
