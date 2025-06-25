#include "Car.h"
#include "User.h"
#include <sqlite>

#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>

string userInput() {

	User myUser("", "", "", "");

	string input;

	string user;
	string registrationU;
	string email;
	string number;


	cout << "What is your first and last name" << "\n";
	cin >> input;
	myUser.setUser(input);

	cout << "What is your registration number" << "\n";
	cin >> input;
	myUser.setRegistrationU(input);

	cout << "What is your Email address" << "\n";
	cin >> input;
	myUser.setEmail(input);

	cout << "What is your phone number" << "\n";
	cin >> input;
	myUser.setNumber(input);



}

void carInput(){
	userInput();

	Car myCar("", "", "", 0, 0.0);


	string input;


	int year;
	double price;

	cout << "What is the make of your car?" << "\n";
	cin >> input;
	myCar.setMake(input);

	cout << "What is the Registration of your car?" << "\n";
	cin >> input;
	myCar.setRegistrationC(input);

	cout << "What is the model of your car?" << "\n";
	cin >> input;
	myCar.setModel(input);

	cout << "What is the year of your car?" << "\n";
	cin >> year;
	myCar.setYear(year);

	cout << "What is the price of your car?" << "\n";
	cin >> price;
	myCar.setPrice(price);





}


int main() {

	

	return 0;
}