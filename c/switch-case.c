#include <stdio.h> // printf, NULL
#include <stdlib.h> // srand, rand
#include <time.h> // time

void checkGrade(int i) {
	printf("YOUR SCORE: %d\n", i);
	// divide the score by 10
	switch(i / 10) {
		case 0 ... 5:
			puts("\tYOUR GRADE: F");
			break;
		case 6:
			puts("\tYOUR GRADE: D");
			break;
		case 7:
			puts("\tYOUR GRADE: C");
			break;
		case 8:
			puts("\tYOUR GRADE: B");
			break;
		case 9:
			puts("\tYOUR GRADE: A");
			break;
		case 10:
			puts("\tYOUR GRADE: A+");
			break;
		default:
			puts("\tYOUR GRADE: F");
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

	// rand() % 100 = choose a random number between 0 and 100
	for (i=0; i<10; i++) {
		checkGrade(rand() % 100);
	}

	return 0;
}
