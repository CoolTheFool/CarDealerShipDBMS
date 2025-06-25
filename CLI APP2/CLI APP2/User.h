#pragma once

#include <string>

using namespace std;

class User {
protected:
	string user;
	string registrationU;
	string email;
	string number;

public:

	User(string user, string registrationU, string email, string number);

	void setUser(string nUser);

	string getUser()const;

	void setRegistrationU(string nRegistrationU);

	string getRegistrationU()const;

	void setEmail(string nEmail);

	string getEmail()const;

	void setNumber(string nNumber);

	string getNumber()const;



};