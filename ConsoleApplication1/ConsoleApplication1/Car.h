#pragma once


#include <string>

using namespace std;

class Car {
protected:
	string make;
	string registration;
	string model;
	int year;
	double price;

public:

	Car(string make, string registration, string model, int year, double price);

	void setMake(string nmake);

	string getMake()const;

	void setRegistration(string nregistration);

	string getRegistration()const;

	void setModel(string nmodel);

	string getModel()const;

	void setYear(int nyear);

	int getYear()const;

	void setPrice(double nprice);

	double getPrice()const;
};