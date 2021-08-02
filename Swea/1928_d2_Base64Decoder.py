T = int(input())

for tc in range(1, T+1):
    test_case = input()
    
    binary_str = ''
    for char in test_case:
        if 'A' <= char <= 'Z':
            num = ord(char) - 65
        elif 'a' <= char <= 'z':
            num = ord(char) - 71
        elif '0' <= char <= '9':
            num = ord(char) + 4
        elif char == '+':
            num = ord(char) + 19
        elif char == '/':
            num = ord(char) + 16
        
        binary_char = bin(num)[2:].zfill(6)
        binary_str += binary_char

    ans = ''
    for j in range(0, len(binary_str)-7, 8):
        ans += chr(int(binary_str[j:j+8], 2))

    print(f'#{tc} {ans}')