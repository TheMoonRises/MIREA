#include <iostream>

using namespace std;

int main() {
	int a[100][50];
	int n, k, m;
	cout << "Enter n and m" << endl;
	cin >> n >> m;
	if (n < 1 or n > 100 or m < 1 or m > 50) {
		cout << "Error";
		return 0;
	}
	cout << "Enter k" << endl;
	cin >> k;
	cout << "Enter ur array" << endl;
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			cin >> a[i][j];
		}
	}
	for (int q = 0; q < k; q++) {
		for (int i = 0; i < n; i++) {
			for (int j = m - 1; j > 0; --j) {
				swap(a[i][j], a[i][j - 1]);
			}
		}
	}


	cout << "Result: " << endl;
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			cout << a[i][j] << " ";
		}
		cout << endl;
	}
}