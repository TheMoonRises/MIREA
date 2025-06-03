#include <iostream>
#include <fstream>
#include <string>
#include <map>
#include <algorithm>

struct Abonent {
    std::string name;
    std::string passportData;
};

class Dictionary {
private:
    std::map<std::string, Abonent> dict;

public:
    Dictionary() {}

    void add(const std::string& phoneNumber, const Abonent& abonent) {
        dict[phoneNumber] = abonent;
    }

    void remove(const std::string& phoneNumber) {
        dict.erase(phoneNumber);
    }

    Abonent find(const std::string& phoneNumber) const {
        auto it = dict.find(phoneNumber);
        if (it != dict.end()) {
            return it->second;
        }
        Abonent emptyAbonent;
        return emptyAbonent;
    }

    void update(const std::string& phoneNumber, const std::string& name, const std::string& passportData) {
        auto it = dict.find(phoneNumber);
        if (it != dict.end()) {
            it->second.name = name;
            it->second.passportData = passportData;
        }
    }

    void print() const {
        for (const auto& [number, abonent] : dict) {
            std::cout << "Phone Number: " << number << std::endl;
            std::cout << "Name: " << abonent.name << std::endl;
            std::cout << "Passport Data: " << abonent.passportData << std::endl;
            std::cout << std::endl;
        }
    }

    void readFromFile(const std::string& filename) {
        std::ifstream file(filename);
        if (!file) {
            std::cerr << "Failed to open file" << std::endl;
            return;
        }

        std::string line;
        while (std::getline(file, line)) {
            std::string phoneNumber, name, passportData;
            size_t pos = line.find(',');
            if (pos != std::string::npos) {
                phoneNumber = line.substr(0, pos);
                line = line.substr(pos + 1);
                pos = line.find(',');
                if (pos != std::string::npos) {
                    name = line.substr(0, pos);
                    passportData = line.substr(pos + 1);

                    Abonent abonent;
                    abonent.name = name;
                    abonent.passportData = passportData;
                    dict[phoneNumber] = abonent;
                }
            }
        }
        file.close();
    }

    void writeToFile(const std::string& filename) const {
        std::ofstream file(filename);
        if (!file) {
            std::cerr << "Failed to open file" << std::endl;
            return;
        }

        for (const auto& [number, abonent] : dict) {
            file << number << "," << abonent.name << "," << abonent.passportData << std::endl;
        }

        file.close();
    }
};

bool CheckPhone(const std::string& phoneNumber) {
    if (phoneNumber.length() != 11) return false;
    if (phoneNumber[0] != '8' && phoneNumber[0] != '7') return false;
    for (char digit : phoneNumber) {
        if (!isdigit(digit)) return false;
    }
    return true;
}

bool CheckName(const std::string& name) {
    for (char ch : name) {
        if (isdigit(ch)) return false;
    }
    return !name.empty();
}

bool CheckPassport(const std::string& passportData) {
    if (passportData.length() != 10) return false;
    for (char digit : passportData) {
        if (!isdigit(digit)) return false;
    }
    return true;
}

int main() {
    Dictionary dictionary;
    std::string filename = "D:\\map.txt";
    dictionary.readFromFile(filename);

    std::string choice;
    while (true) {
        std::cout << "1. Add abonent\n"
                  << "2. Remove abonent\n"
                  << "3. Find abonent\n"
                  << "4. Update abonent\n"
                  << "5. Print dictionary\n"
                  << "6. Create empty dictionary\n"
                  << "7. Exit\n"
                  << "Enter your choice: ";
        std::cin >> choice;
        std::cin.ignore(); // Очистка буфера после ввода числа

        std::cout << std::endl;

        if (choice == "1") {
            std::string phoneNumber, name, passportData;

            std::cout << "Enter phone number: ";
            std::getline(std::cin, phoneNumber);
            if (!CheckPhone(phoneNumber)) {
                std::cout << "Wrong phone number\n";
                continue;
            }

            std::cout << "Enter name: ";
            std::getline(std::cin, name);
            if (!CheckName(name)) {
                std::cout << "Wrong name\n";
                continue;
            }

            std::cout << "Enter passport data: ";
            std::getline(std::cin, passportData);
            if (!CheckPassport(passportData)) {
                std::cout << "Wrong passport data\n";
                continue;
            }

            Abonent abonent;
            abonent.name = name;
            abonent.passportData = passportData;
            dictionary.add(phoneNumber, abonent);
            dictionary.writeToFile(filename);

        } else if (choice == "2") {
            std::string phoneNumber;
            std::cout << "Enter phone number: ";
            std::getline(std::cin, phoneNumber);
            dictionary.remove(phoneNumber);
            dictionary.writeToFile(filename);

        } else if (choice == "3") {
            std::string phoneNumber;
            std::cout << "Enter phone number: ";
            std::getline(std::cin, phoneNumber);

            Abonent abonent = dictionary.find(phoneNumber);
            if (abonent.name.empty()) {
                std::cout << "Abonent not found\n";
            } else {
                std::cout << "Phone number: " << phoneNumber << "\n"
                          << "Name: " << abonent.name << "\n"
                          << "Passport data: " << abonent.passportData << "\n";
            }
            std::cout << std::endl;

        } else if (choice == "4") {
            std::string phoneNumber, name, passportData;

            std::cout << "Enter phone number: ";
            std::getline(std::cin, phoneNumber);

            std::cout << "Enter name: ";
            std::getline(std::cin, name);
            if (!CheckName(name)) {
                std::cout << "Wrong name\n";
                continue;
            }

            std::cout << "Enter passport data: ";
            std::getline(std::cin, passportData);
            if (!CheckPassport(passportData)) {
                std::cout << "Wrong passport data\n";
                continue;
            }

            dictionary.update(phoneNumber, name, passportData);
            dictionary.writeToFile(filename);

        } else if (choice == "5") {
            dictionary.print();

        } else if (choice == "6") {
            std::ofstream file(filename, std::ofstream::trunc); // Очистка файла
            file.close();
            break;

        } else if (choice == "7") {
            std::cout << "Stopping program...\n";
            break;

        } else {
            std::cout << "Invalid choice. Try again.\n";
        }
    }

    return 0;
}