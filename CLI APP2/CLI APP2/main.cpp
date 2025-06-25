#include "Car.h"
#include "User.h"
#include "sqlite3.h"

#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>

void userInput() {

	User myUser("", "", "", "");

	string input;

	string user;
	string registrationU;
	string email;
	string number;


	cout << "What is your first and last name" << "\n";
	getline(cin, user);
	myUser.setUser(user);

	cout << "What is your registration number" << "\n";
	getline(cin, registrationU);
	myUser.setRegistrationU(registrationU);

	cout << "What is your Email address" << "\n";
	getline(cin, email);
	myUser.setEmail(email);

	cout << "What is your phone number" << "\n";
	getline(cin, number);
	myUser.setNumber(number);

	sqlite3* db;

	sqlite3_open("C:\\Users\\NM041\\OneDrive\\Documents\\GitHub\\CarDealerShipDBMS\\dealership.db", &db);

	const char* sql = "INSERT INTO CUSTOMERS (NAME, EMAIL, PHONE, REGISTRATION) VALUES (?, ?, ?, ?)";


	
	sqlite3_stmt* stmt;
	sqlite3_prepare_v2(db, sql, -1, &stmt, NULL);

	sqlite3_bind_text(stmt, 1, myUser.getUser().c_str(), -1, SQLITE_TRANSIENT);
	sqlite3_bind_text(stmt, 2, myUser.getEmail().c_str(), -1, SQLITE_TRANSIENT);
	sqlite3_bind_text(stmt, 3, myUser.getNumber().c_str(), -1, SQLITE_TRANSIENT);
	sqlite3_bind_text(stmt, 4, myUser.getRegistrationU().c_str(), -1, SQLITE_TRANSIENT);

	sqlite3_step(stmt);

	sqlite3_finalize(stmt);
	sqlite3_close(db);
}


void carInput() {

	Car myCar("", "", "", 0, 0.0);


	string input;

	string make;
	string registrationC;
	string model;

	int year;
	double price;

	cout << "What is the make of your car?" << "\n";
	getline(cin, make);
	myCar.setMake(make);

	cout << "What is the Registration of your car?" << "\n";
	getline(cin, registrationC);
	myCar.setRegistrationC(registrationC);

	cout << "What is the model of your car?" << "\n";
	getline(cin, model);
	myCar.setModel(model);

	cout << "What is the year of your car?" << "\n";
	cin >> year;
	myCar.setYear(year);

	cout << "What is the price of your car?" << "\n";
	cin >> price;
	myCar.setPrice(price);


	sqlite3* db;

	sqlite3_open("C:\\Users\\NM041\\OneDrive\\Documents\\GitHub\\CarDealerShipDBMS\\dealership.db", &db);

	const char* sql = "INSERT INTO CARS(MAKE, REGISTRATION, MODEL, YEAR, PRICE) VALUES (?, ?, ?, ?, ?)";

	sqlite3_stmt* stmt;
	sqlite3_prepare_v2(db, sql, -1, &stmt, NULL);

	sqlite3_bind_text(stmt, 1, myCar.getMake().c_str(), -1, SQLITE_TRANSIENT);
	sqlite3_bind_text(stmt, 2, myCar.getRegistrationC().c_str(), -1, SQLITE_TRANSIENT);
	sqlite3_bind_text(stmt, 3, myCar.getModel().c_str(), -1, SQLITE_TRANSIENT);
	sqlite3_bind_int(stmt, 4, myCar.getYear());
	sqlite3_bind_double(stmt, 5, myCar.getPrice());

	sqlite3_step(stmt);

	sqlite3_finalize(stmt);
	sqlite3_close(db);
}

int main() {
	userInput();
	carInput();
	return 0;
}