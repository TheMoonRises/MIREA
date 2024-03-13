#include <iostream>
#include <fstream>
#include <string>
using namespace std;

struct Book {
    int id;
    string code;
    string authors;
    string title;
    int year;
};

void readData(Book books[], int n) {
    ifstream file("D:\\data.txt");
    if (file.is_open()) {
        for (int i = 0; i < n; i++) {
            file >> books[i].id >> books[i].code >> books[i].authors >> books[i].title >> books[i].year;
        }
        file.close();
        cout << "OK." << endl;
    }
    else {
        cout << "Error (open file)." << endl;
    }
}

void sortBooks(Book books[], int n) {
    for (int i = 0; i < n - 1; i++) {
        for (int j = 0; j < n - i - 1; j++) {
            if (books[j].id > books[j + 1].id) {
                Book temp = books[j];
                books[j] = books[j + 1];
                books[j + 1] = temp;
            }
        }
    }
    cout << "An array is sorted." << endl;
}

void printBooks(Book books[], int n) {
    cout << "Object data:" << endl;
    for (int i = 0; i < n; i++) {
        cout << "Registration number: " << books[i].id << endl;
        cout << "Code: " << books[i].code << endl;
        cout << "Authors: " << books[i].authors << endl;
        cout << "Name: " << books[i].title << endl;
        cout << "The year of publishing: " << books[i].year << endl;
        cout << endl;
    }
}

int searchBook(Book books[], int n, int target) {
    int left = 0;
    int right = n - 1;
    while (left <= right) {
        int mid = left + (right - left) / 2;
        if (books[mid].id == target) {
            return mid;
        }
        else if (books[mid].id < target) {
            left = mid + 1;
        }
        else {
            right = mid - 1;
        }
    }
    return -1;
}

int main() {
    int n;
    cout << "Enter the number of objects: ";
    cin >> n;
    if (n > 0 && n <= 50) {
        Book books[50];
        readData(books, n);
        sortBooks(books, n);
        printBooks(books, n);

        int target;
        cout << "Enter regestration number for search: ";
        cin >> target;
        int index = searchBook(books, n, target);
        if (index != -1) {
            cout << "Object on position " << index + 1 << endl;
        }
        else {
            cout << "Object is not found." << endl;
        }
    }
    else {
        cout << "Wrong number of objects" << endl;
    }

    return 0;
}