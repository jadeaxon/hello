To run this these:
PRE: Install the Oracle 11gR2 client.
PRE: Use the right tnsnames.ora (for UVU).
PRE: Installe Oracle Database Express 11gR2 (for local access).
PRE: Install the rlwrap Cygwin package.

In Cygwin:
sqlplus <user>@<database>
# sqlplus baninst1@dev # At UVU.
# sqlplus system@localhost # At home.
This requires having tnsnames.ora correct and in the right place.
I think sqlplus is coming from the Oracle client install, not any Cygwin package.

In sqlplus:
@<SQL script>
@hello.sql

A lot of the examples don't need preloaded data.
For the ones that do, you'll need to run the scripts in setup/.
I run them against a blank Oracle Express 11gR2 instance installed locally too.

Install rlwrap in Cygwin and alias sqlpus to use that in .bashrc so that console works better.
You just install the rlwrap package using the Cygwin installer.
This wraps the command called with the readline library so that you get command history.
The 11gR2 version of sqlplus lacks that.


