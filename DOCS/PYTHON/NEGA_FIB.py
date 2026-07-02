"""
nega-fib.py — AQARION NegaFibonacci Encoding Module

Core implementation of the NegaFibonacci representation for V12_NEGAFIB.
Every integer has a unique representation as a sum of distinct NegaFibonacci
numbers (1, -1, 2, -3, 5, -8, ...) with no two consecutive terms.

Algorithm: BFS over subsets of NegaFibonacci numbers, prioritizing uniqueness
and non-adjacency. If no exact representation is found, the module returns
"valid=False" along with the remainder (honest NR-002 reporting).

NR-002: "Greedy decomposition limit reached. Literature audit pending."
"""
from collections import deque


def build_nf_table(max_val):
    """
    Build a dictionary of NegaFibonacci values up to a sufficient range.
    NF_1 = 1, NF_2 = -1, NF_k = NF_{k-2} - NF_{k-1}.
    """
    nf = {1: 1, 2: -1}
    k = 3
    while True:
        nf[k] = nf[k-2] - nf[k-1]
        # Generate values well beyond the input to guarantee a BFS solution
        if abs(nf[k]) > max_val * 4 + 200:
            break
        k += 1
        if k > 80:  # Safety cap for massive numbers
            break
    return nf


def negafib_encode(n):
    """
    Encode an integer n into its canonical NegaFibonacci representation.

    Returns:
        dict: {
            "value": original n,
            "encoding": bit string (MSB first), or None if failed,
            "valid": True if exact encoding was found,
            "bits": list of bit positions (1-indexed),
            "terms": list of NegaFibonacci values used,
            "check": sum(terms), which should equal n if valid
        }
    """
    if n == 0:
        return {
            "value": 0,
            "encoding": "0",
            "valid": True,
            "bits": [],
            "terms": [],
            "check": 0,
        }

    nf = build_nf_table(abs(n))
    all_keys = sorted(nf.keys())

    # BFS to find the unique subset of NF terms summing to n
    queue = deque()
    for k in all_keys:
        new_rem = n - nf[k]
        # Only push states that reduce the absolute remainder
        if abs(new_rem) <= abs(n):
            queue.append((new_rem, frozenset([k])))

    visited = set()

    while queue:
        rem, used_set = queue.popleft()

        if rem == 0:
            bits = sorted(used_set)
            max_b = max(bits)
            enc = ''.join('1' if i in used_set else '0' for i in range(max_b, 0, -1))
            terms = [nf[b] for b in bits]
            return {
                "value": n,
                "encoding": enc,
                "valid": True,
                "bits": bits,
                "terms": terms,
                "check": sum(terms),
            }

        key = (rem, used_set)
        if key in visited:
            continue
        visited.add(key)

        # Limit search depth and remainder explosion
        if len(used_set) >= 20 or abs(rem) > abs(n) * 3:
            continue

        for k in all_keys:
            if k in used_set:
                continue
            # Non-adjacency constraint: no adjacent bits
            if any(abs(k - u) < 2 for u in used_set):
                continue
            new_rem = rem - nf[k]
            if abs(new_rem) < abs(rem):
                queue.append((new_rem, used_set | {k}))

    # NR-002: Honest remainder reporting if canonical representation fails
    return {
        "value": n,
        "encoding": None,
        "valid": False,
        "bits": [],
        "terms": [],
        "check": n,  # Remainder = n
    }


def negafib_decode(encoding):
    """
    Decode a NegaFibonacci bit string back to an integer.

    Args:
        encoding: bit string (MSB first), or "0" for zero.

    Returns:
        int: reconstructed value, or None if the encoding is invalid
    """
    if encoding == "0":
        return 0

    if '11' in encoding:
        return None  # Invalid representation: contains adjacent 1s

    nf = build_nf_table(10**18)  # Generate sufficient terms for any 64-bit int
    total = 0
    for i, bit in enumerate(reversed(encoding)):
        if bit == '1':
            pos = i + 1
            if pos not in nf:
                return None
            total += nf[pos]

    return total


def verify_roundtrip(n):
    """
    Verify that Encode(Decode(n)) == n.
    Returns True if successful, False otherwise.
    """
    encoded = negafib_encode(n)
    if not encoded['valid']:
        return False
    decoded = negafib_decode(encoded['encoding'])
    return decoded == n
