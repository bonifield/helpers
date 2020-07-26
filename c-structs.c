#include <stdio.h>
#include <string.h>


/* declare structure */
struct People {
	char fname[50];
	char lname[50];
	int age;
};

/* initialize instances of the structure with type struct */
struct People Person1;
struct People Person2;

/* initialize functions */
void printStruct(struct People person);

/* main function */
int main() {
	/* Person1 */
	strcpy(Person1.fname, "Alice");
	strcpy(Person1.lname, "Alison");
	Person1.age = 30;

	/* Person2 */
	strcpy(Person2.fname, "Bob");
	strcpy(Person2.lname, "Robertson");
	Person2.age = 90;

	/* print details from main() */
	/*printf("Person1: %s %s, Age %d\n", Person1.fname, Person1.lname, Person1.age);
	printf("Person2: %s %s, Age %d\n", Person2.fname, Person2.lname, Person2.age);*/

	/* print via printStruct() */
	printStruct(Person1);
	printStruct(Person2);

	return 0;
}

void printStruct(struct People person) {
	printf("Name: %s %s, Age: %d\n", person.fname, person.lname, person.age);
}
