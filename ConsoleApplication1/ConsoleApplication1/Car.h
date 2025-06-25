#pragma once


#include <string>

using namespace std;

class Car {
protected:
	string make;
	string registrationC;
	string model;
	int year;
	double price;

public:

	Car(string make, string registrationC, string model, int year, double price);

	void setMake(string nmake);

	string getMake()const;

	void setRegistrationC(string nregistrationC);

	string getRegistrationC()const;

	void setModel(string nmodel);

	string getModel()const;

	void setYear(int nyear);

	int getYear()const;

	void setPrice(double nprice);

	double getPrice()const;
};