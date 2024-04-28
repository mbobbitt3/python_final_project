#include <stdio.h>
#include <string.h>

// Function to add two numbers
void add() {
    float a, b;
    printf("Enter two numbers to add: ");
    scanf("%f %f", &a, &b);
    printf("The result of %.2f + %.2f = %.2f\n", a, b, a + b);
}

// Function to concatenate two strings
void concatenate_strings() {
    char str1[100], str2[100];
    printf("Enter first string: ");
    scanf("%s", str1);
    printf("Enter second string: ");
    scanf("%s", str2);

    char result[200];
    strcpy(result, str1);
    strcat(result, str2);

    printf("Concatenated string: %s\n", result);
}

// Function to find the maximum number in an array
void find_max_in_array() {
    int n;
    printf("Enter the number of elements in the array: ");
    scanf("%d", &n);

    int arr[n];
    printf("Enter the elements of the array: ");
    for (int i = 0; i < n; i++) {
        scanf("%d", &arr[i]);
    }

    int max = arr[0];
    for (int i = 1; i < n; i++) {
        if (arr[i] > max) {
            max = arr[i];
        }
    }

    printf("The maximum number in the array is: %d\n", max);
}

// Function to display the menu
void display_menu() {
    printf("\nSelect an option:\n");
    printf("1. Add two numbers\n");
    printf("2. Concatenate two strings\n");
    printf("3. Find the maximum number in an array\n");
    printf("4. Exit\n");
    printf("Enter your choice: ");
}

int main() {
    int choice;
    while (1) {
        display_menu();
        scanf("%d", &choice);

        switch (choice) {
            case 1:
                add();
                break;
            case 2:
                concatenate_strings();
                break;
            case 3:
                find_max_in_array();
                break;
            case 4:
                printf("Exiting program. Goodbye!\n");
                return 0;
            default:
                printf("Invalid choice. Please try again.\n");
                break;
        }
    }

    return 0;
}
