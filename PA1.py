# nth_prime_computer.py
"""
Modular implementation of primality detectors and an nth-prime computer.
Submitted for the RSA Primality Testing assignment.

This file contains:
  • Wilson's primality test
  • Trial-division primality test
  • Miller–Rabin primality test
  • Upper bound function for nth prime
  • nth prime finder using any detector
"""

import math
import random
from typing import Callable


# ------------------------------------------------------------
# Upper bound on nth prime
# ------------------------------------------------------------

def upper_bound_nth_prime(n: int) -> int:
    """Return an upper bound B(n) such that p_n ≤ B(n).
    Uses Dusart’s bound for n ≥ 6:  p_n ≤ n (ln n + ln ln n).
    """
    if n < 6:
        # Exact small upper bounds
        small_bounds = [2, 3, 5, 7, 11]
        return small_bounds[n - 1]
    return math.ceil(n * (math.log(n) + math.log(math.log(n))))


# ------------------------------------------------------------
# Primality detectors (Part 2)
# ------------------------------------------------------------

def wilson_is_prime(k: int) -> int:
    """Primality test using Wilson's theorem.
    Returns 1 if prime, 0 otherwise.
    Very slow for large k; purely theoretical.
    """
    if k < 2:
        return 0
    if k == 2:
        return 1
    res = 1
    for i in range(1, k):
        res = (res * i) % k
        if res == 0:
            return 0
    return 1 if res == (k - 1) % k else 0


def trial_division_is_prime(k: int) -> int:
    """Deterministic sqrt(k) primality test."""
    if k < 2:
        return 0
    if k in (2, 3):
        return 1
    if k % 2 == 0:
        return 0
    limit = int(math.isqrt(k))
    i = 3
    while i <= limit:
        if k % i == 0:
            return 0
        i += 2
    return 1


def _mr_try_composite(a: int, d: int, n: int, s: int) -> bool:
    """Internal helper for Miller–Rabin."""
    x = pow(a, d, n)
    if x == 1 or x == n - 1:
        return False
    for _ in range(s - 1):
        x = (x * x) % n
        if x == n - 1:
            return False
    return True


def miller_rabin_is_prime(n: int, rounds: int = 8) -> int:
    """Probabilistic Miller–Rabin test.
    Returns 1 for probably prime, 0 if composite.
    """
    if n < 2:
        return 0

    # Quick elimination using small primes
    small_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    for p in small_primes:
        if n % p == 0:
            return 1 if n == p else 0

    # Write n - 1 as d * 2^s
    d = n - 1
    s = 0
    while d % 2 == 0:
        d //= 2
        s += 1

    # Witness loop
    for _ in range(rounds):
        a = random.randrange(2, n - 1)
        if _mr_try_composite(a, d, n, s):
            return 0
    return 1


# ------------------------------------------------------------
# nth prime using any detector (Part 3)
# ------------------------------------------------------------

def nth_prime_via_detector(
    n: int,
    detector: Callable[[int], int],
    upper_bound_func: Callable[[int], int] = upper_bound_nth_prime
) -> int:
    """Compute the nth prime using the provided primality detector.
    detector(k) must return 1 if k is prime, 0 otherwise.
    """
    if n <= 0:
        raise ValueError("n must be positive")

    if n == 1:
        return 2

    B = upper_bound_func(n)
    count = 0

    for m in range(2, B + 1):
        if detector(m):
            count += 1
            if count == n:
                return m

    raise RuntimeError(
        f"Upper bound {B} was insufficient to find the {n}th prime."
    )
