import random

def generate_string(pattern: str) -> str:
    result = ""
    i = 0
    while i < len(pattern):
        char = pattern[i]
        if char == '(':
            j = i + 1
            subpattern = ""
            while pattern[j] != ')':
                subpattern += pattern[j]
                j += 1
            choices = subpattern.split('|')
            subpattern = random.choice(choices)
            repeat = 1
            i = j + 1
            # Handling special characters '^', '*', '+', '?'
            if j + 1 < len(pattern):
                next_char = pattern[j + 1]
                if next_char == '^':
                    if pattern[j + 2].isdigit():
                        repeat = int(pattern[j + 2])
                        i = j + 3
                elif next_char == '*':
                    repeat = random.randint(0, 3)
                    i = j + 2
                elif next_char == '+':
                    repeat = random.randint(1, 3)
                    i = j + 2
                elif next_char == '?':
                    repeat = random.randint(0, 1)
                    i = j + 2
            result += subpattern * repeat
            continue
        # Handling special characters '*', '+', '?', '^'
        next_char = pattern[i + 1] if i + 1 < len(pattern) else ""
        if next_char == '^':
            result += char * int(pattern[i+2])
            i += 3
            continue
        elif next_char == '*':
            result += char * random.randint(0, 5)
            i += 2
            continue
        elif next_char == '+':
            result += char * random.randint(1, 5)
            i += 2
            continue
        elif next_char == '?':
            result += char * random.randint(0, 1)
            i += 2
            continue
        result += char
        i += 1
    return result

def main():
    pattern1 = "(S|T)(U|V)w*y+24"
    pattern2 = "L(M|N)O^3P*Q(2|3)"
    pattern3 = "R*S(T|U|V)W(X|Y|Z)^2"

    print("RE1:")
    generated_strings = [generate_string(pattern1) for _ in range(5)]
    print(", ".join(generated_strings))

    print("RE2:")
    generated_strings = [generate_string(pattern2) for _ in range(5)]
    print(", ".join(generated_strings))

    print("RE3:")
    generated_strings = [generate_string(pattern3) for _ in range(5)]
    print(", ".join(generated_strings))

if __name__ == "__main__":
    main()


