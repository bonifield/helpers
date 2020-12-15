#include <stdio.h>

// *pa and *pb are both pointers of type int
// a pointer stores the address of another object (variables etc)
// the "*" dereferences the pointer, meaning it accesses the value at the pointer's location
// swap() will change the variables inside main() directly by accessing their memory locations
void swap(int *pa, int *pb) {
	int t = *pa;
	*pa = *pb; // *pb gets dereferenced, *pa gets dereferenced, and value referenced by *pa is overwritten with the value referenced by *pb
	*pb = t; // the value held at the location of *pb is assigned the value of t
	return;
}

int main(void) {
	// declare variables
	int a = 21;
	int b = 17;
	// size_t = size of objects in bytes
	size_t a_size = sizeof a;
	size_t b_size = sizeof b;
	printf("main: a = %d, b = %d\n", a, b);
	// %ld = long int
	printf("sizeof: a = %ld, b = %ld\n", a_size, b_size);

	// "&" = unary "address-of" operators
	// since swap() takes pointers, we must also provide pointers
	// "call-by-reference" or "pass-by-reference": generate object addresses, pass them by value, dereference copied addresses to access the original objects (in this case, "a" and "b")
	swap(&a, &b);
	printf("swap: a = %d, b = %d\n", a, b);
	return 0;
}
