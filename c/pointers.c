#include <stdio.h>
#include <stdlib.h>

void printLocations(int* iptr) {
	printf("value pointed to by iptr:\t%d\n", *iptr); // "*" dereferences the pointer and prints value of "i" which is inside main() (%d = signed decimal int)
	printf("address pointed to by iptr:\t%p\n", iptr); // the address pointed to by iptr, of "i" inside main() (%p = hexadecimal)
	printf("address of iptr itself:\t\t%p\n", &iptr); // "&" = unary "address-of" operator, gets the actual location of iptr
}

int main() {
	int i = 12345;
	int* x = &i; // address of int variable "i" is stored using int pointer x
	printLocations(x);
	return 0;
}
