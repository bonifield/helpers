#include <stdio.h>


/* functions */
void forloop() {
	/* variable state; condition; action */
	for (int i; i < 6; i++) {
		printf("for counter is %d\n", i);
	}
}


void whileloop() {
	int x = 0;
	while (x < 6) {
		printf("while counter is %d\n", x);
		x++;
	}
}


void doloop() {
	/* do {actions;} while (condition);  */
	int x = 0;
	do {
		printf("do counter is %d\n", x);
		x++;
	} while (x < 6);
}


void nestedloop() {
	int a, b;
	for (int a = 0; a < 3; a++) {
		for (int b = 6; b < 10; b++) {
			printf("outer value: %d, inner value %d\n", a, b);
		}
	}
}


int main() {
	forloop();
	whileloop();
	doloop();
	nestedloop();
	return 0;
}
