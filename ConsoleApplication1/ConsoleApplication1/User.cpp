#include "User.h"

#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>

using namespace std;

User::User(string user, string registrationU, string email, string number) :
	user(user), registrationU(registrationU), email(email), number(number) {

}

void User::setUser(string nUser) {
	user = nUser;
}


string User::getUser()const {
	return user;
}

void User::setRegistrationU(string nRegistrationU) {
	registrationU = nRegistrationU;
}

string User::getRegistrationU()const {
	return registrationU;
}

void User::setEmail(string nEmail) {
	email = nEmail;
}

string User::getEmail()const {
	return email;
}

void User::setNumber(string nNumber) {
	number = nNumber;
}

string User::getNumber()const {
	return number;
}