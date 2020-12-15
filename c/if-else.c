#include <stdio.h> // printf, NULL
#include <stdlib.h> // srand, rand
#include <time.h> // time

void checkNumber(int i) {
	if (i < 50) {
		printf("%d is less than 50\n", i);
	} else if (i == 50) {
		printf("%d is equal to 50\n", i);
	} else if (i > 50) {
		printf("%d is greater than 50\n", i);
	} else {
		puts("something else");
	}
}

int main() {
	int i;
	time_t t;

	// srand is initialized with some distinctive runtime value, like time, as a pointer
	// srand can also be initialized with NULL
	// RAND_MAX = 2147483647
	//srand(time(&t));
	srand(time(NULL));

	// print 10 random numbers and compare them to the number 50
	// rand() % 100 = choose a random number between 0 and 100
	for (i=0; i<10; i++) {
		checkNumber(rand() % 100);
	}

	return 0;
}
