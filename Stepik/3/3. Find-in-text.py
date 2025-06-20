import sys

def read_data():
    return sys.stdin.readline().strip(), sys.stdin.readline().strip()

def poly_hash(s, p=10**9 + 7, x=263):
    hash_val = 0

    for c in reversed(s):
        hash_val = (hash_val * x + ord(c)) % p

    return hash_val

def precompute_hashes(text, pat_len, p=10**9 + 7, x=263):
    n = len(text)
    H = [0] * (n - pat_len + 1)
    S = text[-pat_len:]
    H[-1] = poly_hash(S, p, x)

    y = pow(x, pat_len, p)

    for i in range(n - pat_len - 1, -1, -1):
        H[i] = (x * H[i + 1] + ord(text[i]) - y * ord(text[i + pat_len])) % p
        H[i] = (H[i] + p) % p

    return H

def rabin_karp(pattern, text):
    p = 10**9 + 7
    x = 263
    result = []
    pat_len = len(pattern)
    text_len = len(text)

    p_hash = poly_hash(pattern, p, x)
    H = precompute_hashes(text, pat_len, p, x)

    for i in range(text_len - pat_len + 1):
        if H[i] == p_hash and text[i:i+pat_len] == pattern:
            result.append(i)

    return result

pattern, text = read_data()
positions = rabin_karp(pattern, text)
print(" ".join(map(str, positions)))
