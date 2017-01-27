// Demonstate simple object-based programming in C using structs and function pointers.

#include <stdio.h> // printf()
#include <stdlib.h> // malloc()


// Let's create an object-like struct in C.
// Use a forward declaration so we can use Object in the definition of the struct.
typedef struct object Object;
struct object {
	// A public member var.  We can only restrict access by convention in C.
	int value; 
	// A setter method.
	// We can't use Object yet because we're in the middle of defining it.
	// We have to explicitly pass an Object* arg when invoke since no C++ syntactic sugar.
	void (*setValue)(Object* this, int arg); 

};


// The syntactic sugar in C++ is having a namespace for this struct, making the 'this' arg implicit, and
// making you not have to declare function pointers in struct using difficult syntax.
//
// Without C++ namespaces, this could cause trouble.  Do we even have function overloading to
// save us in C?  Or do we need to prefix the name of each function: Object_setValue(...), etc.
void setValue(Object* this, int arg) {
	this->value = arg;
}


// Creates an object instance on heap.  Returns a pointer to it.
// Caller is responsible for cleaning up.
Object* createObject(void) {
	Object* o = malloc(sizeof(Object)); // new Object
	o->setValue = setValue;
	return o;
}


// Let's use our new "class".
void main(void) {
	Object* object = createObject();	
	
	// WARNING:
	// It may be that calling a function that exists on the stack is perillous.
	// Probably because its stack frame goes away when you call it.
	// Object o;
	// o.setValue(&o, 3); // We must explicitly pass Object* as first arg.
	//
	// No, the problem is I'm forgetting to initialize the function pointers in the struct.
	// So, I'm doing a function call on a null pointer.  This causes a segfault.
	// We need some kind of creational function (like a constructor) to init the object.

	object->setValue(object, 3);
	printf("object->value = %d\n", object->value);
	
	free(object);
} // main(void)



