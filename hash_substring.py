# python3

def read_input():
    # this function needs to acquire input both from keyboard and file
    # as before, use capital i (input from keyboard) and capital f (input from file) to choose which input type will follow
    
    input_type = input()
    
    if input_type == "I":
        pattern = input().rstrip()
        text = input().rstrip()
    elif input_type == "F":
        with open("input.txt") as f:
            pattern = f.readline().rstrip()
            text = f.readline().rstrip()
    
    # return both lines in one return
    return pattern, text

def print_occurrences(output):
    # this function should control output, it doesn't need any return
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    # this function should find the occurrences using Rabin Karp algorithm 
    
    # compute some constants
    prime = 1000000007
    multiplier = 263
    
    # compute hash value of pattern and first window of text
    pattern_hash = 0
    window_hash = 0
    for i in range(len(pattern)):
        pattern_hash = (pattern_hash * multiplier + ord(pattern[i])) % prime
        window_hash = (window_hash * multiplier + ord(text[i])) % prime
    
    # compute (multiplier^len(pattern)) % prime
    multiplier_power = pow(multiplier, len(pattern), prime)
    
    occurrences = []
    
    # slide the window and compare hash values
    for i in range(len(text) - len(pattern) + 1):
        if pattern_hash == window_hash and text[i:i+len(pattern)] == pattern:
            occurrences.append(i)
        
        # compute hash value for next window
        if i < len(text) - len(pattern):
            window_hash = (multiplier * (window_hash - ord(text[i]) * multiplier_power) + ord(text[i+len(pattern)])) % prime
    
    return occurrences

# this part launches the functions
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))
