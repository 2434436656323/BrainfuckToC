import sys

def optimize_bf(code):
    mem = [0] * 30000
    ptr = 0
    output_sequence = []
    
    i = 0
    while i < len(code):
        cmd = code[i]
        
        if cmd == '>':
            ptr += 1
        elif cmd == '<':
            ptr -= 1
        elif cmd == '+':
            mem[ptr] = (mem[ptr] + 1) % 256
        elif cmd == '-':
            mem[ptr] = (mem[ptr] - 1) % 256
        elif cmd == '.':
            output_sequence.append(mem[ptr])
        elif cmd == ',':
            pass
        elif cmd == '[':
            if mem[ptr] == 0:
                depth = 1
                while depth > 0 and i < len(code) - 1:
                    i += 1
                    if code[i] == '[': depth += 1
                    elif code[i] == ']': depth -= 1
        elif cmd == ']':
            if mem[ptr] != 0:
                depth = 1
                while depth > 0 and i > 0:
                    i -= 1
                    if code[i] == ']': depth += 1
                    elif code[i] == '[': depth -= 1
                continue
        
        i += 1

    return output_sequence

def generate_clean_c(output_bytes):
    c_code = """#include <stdio.h>

int main() {
"""
    if len(output_bytes) <= 20:
        for byte_val in output_bytes:
            char_repr = repr(chr(byte_val)) if 32 <= byte_val <= 126 else str(byte_val)
            c_code += f"    putchar({char_repr});\n"
        c_code += "    putchar('\\n');\n"
    else:
        text = "".join([chr(b) if 32 <= b <= 126 else "\\x{:02x}".format(b) for b in output_bytes])
        safe_text = text.replace('"', '\\"')
        c_code += f'    printf("{safe_text}\\n");\n'

    c_code += """    return 0;
}
"""
    return c_code

if __name__ == "__main__":
    bf_input = sys.stdin.read()
    if not bf_input.strip():
        print("Кидай BF код в stdin!")
        sys.exit(1)

    result_bytes = optimize_bf(bf_input)
    clean_c = generate_clean_c(result_bytes)
    print(clean_c)

