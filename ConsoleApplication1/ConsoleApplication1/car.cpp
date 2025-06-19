#include "Car.h"

#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>

using namespace std;

Car::Car(string make, string registration, string model, int year, double price)
{
	make = "";
	registration = "";
	model = "";
	year = 0;
	price = 0.0;
}

void Car::setMake(string nmake) {
	make = nmake;
}
string Car::getMake()const {
	return make;

}

void Car::setRegistration(string nregistration) {
	registration = nregistration;
}

string Car::getRegistration()const {
	return registration;
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