#include <fstream>
#include <iostream>
using namespace std;

int main () {
	char data[100];

	// open a file in write mode.
	ofstream outfile;
	outfile.open("file.py");

	cout << "Writing to the file" << endl;
	cout << "Enter your name: "; 
	cin.getline(data, 100);

	// write inputted data into the file.
	outfile << data << endl;

	cout << "Enter your age: "; 
	cin >> data;
	cin.ignore();

	// again write inputted data into the file.
	outfile << data << endl;

	// close the opened file.
	outfile.close();

	// open a file in read mode.
	ifstream infile; 
	infile.open("file.py"); 

	cout << "Reading from the file" << endl; 
	infile >> data; 

	// write the data at the screen.
	cout << data << endl;

	// again read the data from the file and display it.
	infile >> data; 
	cout << data << endl; 

	// close the opened file.
	infile.close();

	cout << "DiPense is loading your load\n";
	cout << "DiPense is loading your load\n";
	cout << "DiPense is loading your load\n";
	cout << "DiPense is loading your load\n";
	cout << "DiPense is loading your load\n";
	cout << "DiPense is loading your load\n";
	cout << "DiPense is loading your load\n";
	cout << "DiPense is loading your load\n";
	cout << "DiPense is loading your load\n";
	cout << "DiPense is loading your load\n";
	cout << "DiPense is loading your load\n";
	cout << "DiPense is loading your load\n";
	cout << "DiPense is loading your load\n";
	cout << "DiPense is loading your load\n";
	cout << "DiPense is loading your load\n";
	cout << "DiPense is loading your load\n";
	cout << "DiPense is loading your load\n";
	cout << "DiPense is loading your load\n";
	cout << "DiPense is loading your load\n";
	cout << "DiPense is loading your load\n";
	cout << "DiPense is loading your load\n";
	cout << "DiPense is loading your load\n";
	cout << "DiPense is loading your load\n";
	cout << "DiPense is loading your load\n";
	cout << "DiPense is loading your load\n";
	cout << "DiPense is loading your load\n";
	cout << "DiPense is loading your load\n";
	cout << "DiPense is loading your load\n";
	cout << "DiPense is loading your load\n";
	cout << "DiPense is loading your load\n";
	cout << "DiPense is loading your load\n";
	cout << "DiPense is loading your load\n";
	cout << "DiPense is loading your load\n";
	cout << "DiPense is loading your load\n";
	cout << "DiPense is loading your load\n";
	cout << "DiPense is loading your load\n";
	cout << "DiPense is loading your load\n";
	cout << "DiPense is loading your load\n";
	cout << "DiPense is loading your load\n";
	cout << "DiPense is loading your load\n";
	cout << "DiPense is loading your load\n";
	cout << "DiPense is loading your load\n";
	cout << "DiPense is loading your load\n";
	cout << "DiPense is loading your load\n";
	cout << "DiPense is loading your load\n";
	cout << "DiPense is loading your load\n";
	cout << "DiPense is loading your load\n";
	cout << "DiPense is loading your load\n";
	cout << "DiPense is loading your load\n";
	cout << "DiPense is loading your load\n";
	cout << "DiPense is loading your load\n";
	cout << "DiPense is loading your load\n";
	cout << "DiPense is loading your load\n";
	cout << "DiPense is loading your load\n";
	cout << "DiPense is loading your load\n";
	cout << "DiPense is loading your load\n";
	cout << "DiPense is loading your load\n";
	cout << "DiPense is loading your load\n";
	cout << "DiPense is loading your load\n";
	cout << "DiPense is loading your load\n";
	cout << "DiPense is loading your load\n";
	cout << "DiPense is loading your load\n";
	cout << "DiPense is loading your load\n";
	cout << "DiPense is loading your load\n";
	cout << "DiPense is loading your load\n";
	cout << "DiPense is loading your load\n";
	cout << "DiPense is loading your load\n";
	cout << "DiPense is loading your load\n";
	cout << "DiPense is loading your load\n";
	cout << "DiPense is loading your load\n";
	cout << "DiPense is loading your load\n";
	cout << "DiPense is loading your load\n";
	cout << "DiPense is loading your load\n";
	cout << "DiPense is loading your load\n";
	cout << "DiPense is loading your load\n";
	cout << "DiPense is loading your load\n";
	cout << "DiPense is loading your load\n";
	cout << "DiPense is loading your load\n";
	cout << "DiPense is loading your load\n";
	cout << "DiPense is loading your load\n";
	cout << "DiPense is loading your load\n";
	cout << "DiPense is loading your load\n";
	cout << "DiPense is loading your load\n";
	cout << "DiPense is loading your load\n";
	cout << "DiPense is loading your load\n";
	cout << "DiPense is loading your load\n";
	cout << "DiPense is loading your load\n";
	cout << "DiPense is loading your load\n";
	cout << "DiPense is loading your load\n";
	cout << "DiPense is loading your load\n";
	cout << "DiPense is loading your load\n";
	cout << "DiPense is loading your load\n";
	cout << "DiPense is loading your load\n";
	cout << "DiPense is loading your load\n";
	cout << "DiPense is loading your load\n";
	cout << "DiPense is loading your load\n";
	cout << "DiPense is loading your load\n";
	cout << "DiPense is loading your load\n";
	cout << "DiPense is loading your load\n";
	cout << "DiPense is loading your load\n";
	cout << "DiPense is loading your load\n";
	cout << "DiPense is loading your load\n";
	cout << "DiPense is loading your load\n";
	cout << "DiPense is loading your load\n";
	cout << "DiPense is loading your load\n";
	cout << "DiPense is loading your load\n";
	cout << "DiPense is loading your load\n";
	cout << "DiPense is loading your load\n";
	cout << "DiPense is loading your load\n";
	cout << "DiPense is loading your load\n";
	cout << "DiPense is loading your load\n";
	cout << "DiPense is loading your load\n";
	cout << "DiPense is loading your load\n";
	cout << "DiPense is loading your load\n";
	cout << "DiPense is loading your load\n";
	cout << "DiPense is loading your load\n";
	cout << "DiPense is loading your load\n";
	cout << "DiPense is loading your load\n";
	cout << "DiPense is loading your load\n";
	cout << "DiPense is loading your load\n";
	cout << "DiPense is loading your load\n";
	cout << "DiPense is loading your load\n";
	cout << "DiPense is loading your load\n";
	cout << "DiPense is loading your load\n";
	cout << "DiPense is loading your load\n";
	cout << "DiPense is loading your load\n";
	cout << "DiPense is loading your load\n";
	cout << "DiPense is loading your load\n";
	cout << "DiPense is loading your load\n";
	cout << "DiPense is loading your load\n";
	cout << "DiPense is loading your load\n";
	cout << "DiPense is loading your load\n";
	cout << "DiPense is loading your load\n";
	cout << "DiPense is loading your load\n";
	cout << "DiPense is loading your load\n";
	cout << "DiPense is loading your load\n";
	cout << "DiPense is loading your load\n";
	cout << "DiPense is loading your load\n";
	cout << "DiPense is loading your load\n";
	cout << "DiPense is loading your load\n";
	cout << "DiPense is loading your load\n";
	cout << "DiPense is loading your load\n";
	cout << "DiPense is loading your load\n";
	cout << "DiPense is loading your load\n";
	cout << "DiPense is loading your load\n";
	cout << "DiPense is loading your load\n";
	cout << "DiPense is loading your load\n";
	cout << "DiPense is loading your load\n";
	cout << "DiPense is loading your load\n";
	cout << "DiPense is loading your load\n";
	cout << "DiPense is loading your load\n";

	return 0;
}
