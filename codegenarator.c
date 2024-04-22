#include<stdio.h>
#include<string.h>

static int j = 0; // Global variable

void generateMachine(char op[], char arg1[], char arg2[], char result[]) {
    if (strcmp(op, "+") == 0) {
        printf("\nMOV R%d, %s", j, arg1);
        printf("\nMOV R%d, %s", j + 1, arg2);
        printf("\nADD R%d, R%d", j, j + 1);
        printf("\nMOV %s, R%d\n", result, j);
        j=j+2;
    }
    else if (strcmp(op, "-") == 0) {
        printf("\nMOV R%d, %s", j, arg1);
        printf("\nMOV R%d, %s", j + 1, arg2);
        printf("\nSUB R%d, R%d", j, j + 1);
        printf("\nMOV %s, R%d\n", result, j);
        j=j+2;

    }
    else if (strcmp(op, "*") == 0) {
        printf("\nMOV R%d, %s", j, arg1);
        printf("\nMOV R%d, %s", j + 1, arg2);
        printf("\nMUL R%d, R%d", j, j + 1);
        printf("\nMOV %s, R%d\n", result, j);
                j=j+2;

    }
    else if (strcmp(op, "/") == 0) {
        printf("\nMOV R%d, %s", j, arg1);
        printf("\nMOV R%d, %s", j + 1, arg2);
        printf("\nDIV R%d, R%d", j, j + 1);
        printf("\nMOV %s, R%d\n", result, j);
                j=j+2;

    }
}

int main() {
    int num_object;
    printf("Enter the number of expressions: ");
    scanf("%d", &num_object);

    char expression[num_object][20];
    for (int i = 0; i < num_object; i++) {
        printf("Enter expression %d: ", i + 1);
        scanf("%s", expression[i]);
    }

    printf("Rearranged expression: \n");
    char op[5], arg1[5], arg2[5], result[5];
    for (int i = 0; i < num_object; i++) {
        sscanf(expression[i], "%c=%c%c%c", &result[i], &arg1[i], &op[i], &arg2[i]);
        printf("%c %c %c %c\n", arg1[i], arg2[i], result[i], op[i]);
        generateMachine(&op[i], &arg1[i], &arg2[i], &result[i]);
    }

    return 0;
}
