# python3

def read_input():
    # this function acquires input both from keyboard and file
    choice = input().rstrip()
    if choice == "F":
        with open('input.txt', 'r') as f:
            pattern = f.readline().rstrip()
            text = f.readline().rstrip()
    elif choice == "I":
        pattern = input().rstrip()
        text = input().rstrip()
    return pattern, text

def print_occurrences(output):
    # this function prints the positions of the occurrences
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    # this function finds the occurrences using Rabin-Karp algorithm
    p = 1000000007  # prime number for hashing
    x = 263  # base for hashing
    m = len(pattern)
    n = len(text)
    results = []
    if n < m:
        return results
    p_hash = 0
    t_hash = 0
    h = pow(x, m - 1, p)  # precompute h
    for i in range(m):
        p_hash = (x * p_hash + ord(pattern[i])) % p
        t_hash = (x * t_hash + ord(text[i])) % p
    if p_hash == t_hash and text[:m] == pattern:
        results.append(0)
    for i in range(1, n - m + 1):
        t_hash = (x * (t_hash - ord(text[i - 1]) * h) + ord(text[i + m - 1])) % p
        if p_hash == t_hash and text[i:i + m] == pattern:
            results.append(i)
    return results

# this part launches the functions
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))
