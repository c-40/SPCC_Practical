#include <stdio.h>
#include <stdbool.h>

const char *input;

// Function prototypes
bool E();
bool T();
bool F();

// Grammar rule: E -> T { ('+' | '-') T }
bool E() {
    printf("%-16s E -> T E'\n", input);
    if (T()) {
        while (*input == '+' || *input == '-') {
            printf("%-16s E' -> %c T E'\n", input, *input);
            input++;
            if (!T()) {
                return false;
            }
        }
        printf("%-16s E' -> $\n", input);
        printf("%-16s String is successfully parsed\n", input);
        return true;
    }
    return false;
}

// Grammar rule: T -> F { ('*' | '/') F }
bool T() {
    printf("%-16s T -> F T'\n", input);
    if (F()) {
        while (*input == '*' || *input == '/') {
            printf("%-16s T' -> %c F T'\n", input, *input);
            input++;
            if (!F()) {
                return false;
            }
        }
        printf("%-16s T' -> $\n", input);
        return true;
    }
    return false;
}

// Grammar rule: F -> '(' E ')' | 'i'
bool F() {
    printf("%-16s F -> %c\n", input, *input);
    if (*input == '(') {
        input++;
        if (E() && *input == ')') {
            input++;
            return true;
        }
        return false;
    }
    if (*input == 'i') {
        input++;
        return true;
    }
    return false;
}

int main() {
    puts("Enter the string");
    char string[64];
    scanf("%s", string); // Read input from the user
    input = string;
     puts("Grammar Rules:");
    puts("E -> T E'");
    puts("E' -> + T E' | $");
    puts("T -> F T'");
    puts("T' -> * F T' | $");
    puts("F -> ( E ) | i");

    puts("Input         Action");
    puts("--------------------------------");
    if (E() && *input == '\0') {
        puts("--------------------------------");
        puts("String is successfully parsed");
        return 0;
    } else {
        puts("--------------------------------");
        puts("Error in parsing String");
        return 1;
    }
}
