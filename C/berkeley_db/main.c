// Berkeley DB
#include <db.h>

// C
#include <string.h> // memset()
#include <stdlib.h> // exit()

void main(void) {
	DB* dbp = 0; /* DB structure handle */
	u_int32_t flags = 0; /* database open flags */
	int ret = 0; /* function return value */
	
	/* Initialize the structure. This
	 * database is not opened in an environment,
	 * so the environment pointer is NULL. */
	ret = db_create(&dbp, NULL, 0);
	if (ret != 0) {
		/* Error handling goes here */
	}
	
	/* Database open flags */
	/* If the database does not exist, create it.*/
	flags = DB_CREATE; 
	
	/* open the database */
	ret = dbp->open(dbp, /* DB structure pointer */
		NULL, /* Transaction pointer */
		"my_db.db", /* On-disk file that holds the database. */
		NULL, /* Optional logical database name */
		DB_BTREE, /* Database access method */
		flags, /* Open flags */
		0 /* File mode (using defaults) */
	); 
	if (ret != 0) {
		/* Error handling goes here */
	}

	// Do some stuff with the database . . .
	// A database record has a key and a value.
	// BDB uses a DBT type to rep both.  It is a void* and a length.
	// So it is a serialize blob of some amount of any kind of data.
	DBT key, value;
	float money = 122.45;
	char *description = "Grocery bill.";
	
	/* Zero out the DBTs before using them. */
	memset(&key, 0, sizeof(DBT));
	memset(&value, 0, sizeof(DBT));
	key.data = &money;
	key.size = sizeof(float);
	value.data = description;
	value.size = strlen(description) + 1; // For \0.

	// Okay, so we have a key and value DBT.  How do we put that in the database?
	// 2nd arg is transaction this access is part of.  We're not using transactions.
	// Last argument is flags affecting execution of put().
	int error = dbp->put(dbp, NULL, &key, &value, 0);
	if (error) {
		printf("Failed to put record into database.\n");
		exit(1);
	}


	/* Zero out the DBTs before using them. */
	DBT key2, value2;	
	memset(&key2, 0, sizeof(DBT));
	memset(&value2, 0, sizeof(DBT));
	key2.data = &money;
	key2.size = sizeof(float);
	// value2.data = ""; // How do we init this?
	// value2.ulen = 1024;
	// value2.flags = DB_DBT_USERMEM; // Use our own memory to ward off alignment problems.
	error = dbp->get(dbp, NULL, &key2, &value2, 0);
	if (error) {
		printf("Failed to get record from database.");
		exit(1);
	}
	// char* retrieved = (char*) value2.data;
	printf("Retrieved: %s\n", (char*) value2.data);

	// Close the database.
	if (dbp != NULL) dbp->close(dbp, 0);

} // main(...)


 
