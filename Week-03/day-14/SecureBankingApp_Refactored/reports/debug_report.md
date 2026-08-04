# Debug Report

## Project

Secure Banking Application

---

## Bug 1

### Problem

Program crashed when user entered letters instead of numbers.

### Cause

Invalid numeric input.

### Solution

Added try-except block.

### Status

Fixed

---

## Bug 2

### Problem

Negative amount accepted during deposit.

### Cause

No validation.

### Solution

Added amount > 0 validation.

### Status

Fixed

---

## Bug 3

### Problem

Withdrawal allowed even with insufficient balance.

### Cause

Balance checking missing.

### Solution

Added balance validation.

### Status

Fixed

---

## Bug 4

### Problem

Duplicate account numbers.

### Cause

No duplicate checking.

### Solution

Checked account number before creating account.

### Status

Fixed

---

## Bug 5

### Problem

Application had no activity logs.

### Cause

Logging not implemented.

### Solution

Added Logger, FileHandler and Formatter.

### Status

Fixed

---

## Bug 6

### Problem

Unexpected program crash.

### Cause

Unhandled exception.

### Solution

Added Exception Logging.

### Status

Fixed