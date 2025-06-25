#include "Car.h"

#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>

using namespace std;

Car::Car(string make, string registrationC, string model, int year, double price)
	: make(make), registrationC(registrationC), model(model), year(year), price(price) {

}


void Car::setMake(string nmake) {
	make = nmake;
}
string Car::getMake()const {
	return make;

}

void Car::setRegistrationC(string nregistrationC) {
	registrationC = nregistrationC;
}

string Car::getRegistrationC()const {
	return registrationC;
}

void Car::setModel(string nmodel) {
	model = nmodel;
}

string Car::getModel()const {
	return model;
}

void Car::setYear(int nyear) {
	year = nyear;
}

int Car::getYear()const {
	return year;
}

void Car::setPrice(double nprice){
	price = nprice;
}

double Car::getPrice()const {
	return price;
}