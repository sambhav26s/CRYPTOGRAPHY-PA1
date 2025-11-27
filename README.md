# RSA Primality Testing – Nth Prime Computer
This repository contains my submission for the Programming Assignment (PA-1) of the
Cryptography course.  
The goal of the assignment is to transform a **prime detector** into a **prime computer** —
a function that takes an input `n` and returns the `n`-th prime number.

---

## 1. Overview
The security of RSA depends on the hardness of factoring large integers. Many primality
tests ("prime detectors") exist.  
This assignment explores whether a detector can be turned into a **computer for primes**.

I implemented multiple primality detectors and a generic function that uses any detector
to compute the `n`-th prime.

The implementation is modular, readable, and self-contained.

---

## 2. Files in this repository

### **`PA1.py`**
This single file contains:
- **Wilson’s primality test** (very slow, theoretical)
- **Trial-division primality test**
- **Miller–Rabin probabilistic primality test**
- **Upper bound function** based on Dusart’s inequality
- **nth-prime computation** using any detector

Usage pattern (pseudo):

```python
nth_prime_via_detector(n, trial_division_is_prime)
nth_prime_via_detector(n, wilson_is_prime)
nth_prime_via_detector(n, miller_rabin_is_prime)
SUBMITTED BY SAMBHAV BHANDARI -2023A7PS0549P
I think i have done bonus option also but on a safe side  i will do PA2 also
