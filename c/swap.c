#include <stdio.h>

void swap(int a, int b) {
	int t = a;
	a = b;
	b = t;
	printf("swap: a = %d, b = %d\n", a, b);
}

int main(void) {
	// declare variables
	int a = 21;
	int b = 17;

	// printf %d = digit
	printf("main: a = %d, b = %d\n", a, b);

	// run swap function
	swap(a,b);
	return 0;
}
