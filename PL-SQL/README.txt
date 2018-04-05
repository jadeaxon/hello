To run this these:
In Cygwin:
sqlplus <user>@<database>
# sqlplus baninst1@dev
This requires having tnsnames.ora correct and in the right place.
I think sqlplus is coming from the Oracle client install, not any Cygwin package.

In sqlplus:
@<SQL script>
@hello.sql

A lot of the examples don't need preloaded data.
For the ones that do, you'll need to run the scripts in setup/.
I run them against a blank Oracle Express 11gR2 instance.


