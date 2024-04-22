#include <stdio.h>
#include <ctype.h>

void lexical_analysis(char input_string[]) {
    int i = 0;

    while (input_string[i] != '\0') {
        // If the current character is a letter or underscore, it's part of an identifier
        if (isalpha(input_string[i]) || input_string[i] == '_') {
            printf("Identifier: ");
            // Continue printing characters until a non-alphanumeric character is found
            while (isalnum(input_string[i]) || input_string[i] == '_') {
                printf("%c", input_string[i]);
                i++;
            }
            printf("\n");
        }
        // If the current character is a digit, it's part of a constant
        else if (isdigit(input_string[i])) {
            printf("Constant: ");
            // Continue printing digits until a non-digit character is found
            while (isdigit(input_string[i])) {
                printf("%c", input_string[i]);
                i++;
            }
            printf("\n");
        }
        // If the current character is an operator (+, -, *, /, =)
        else if (input_string[i] == '+' || input_string[i] == '-' || input_string[i] == '*' || input_string[i] == '/' || input_string[i] == '=') {
            printf("Operator: %c\n", input_string[i]);
            i++;
        }
        // Ignore whitespace characters
        else if (isspace(input_string[i])) {
            i++;
        }
        // If the character is none of the above, it's unrecognized
        else {
            printf("Unrecognized character: %c\n", input_string[i]);
            i++;
        }
    }
}

int main() {
    char input_string[100]; // Assuming input string won't exceed 100 characters

    printf("Enter a string: ");
    fgets(input_string, sizeof(input_string), stdin);

    lexical_analysis(input_string);
    return 0;
}
