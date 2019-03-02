-- PRE: You are running APEX 5.0 or higher.
-- Oracle Express 11gR2 comes with APEX 4.0.2.  The apex_json stuff DNE here.
-- https://www.oracle.com/technetwork/developer-tools/apex/learnmore/upgrade-apex-for-xe-154969.html
-- Yup, I was able to upgrade to APEX 5.0.4.

set serveroutput on;

declare
	value varchar2(256);

	-- JSON representing a request to reclassify some transactions.
	request_json varchar2(32767) := '
{
	"request": {
		"id": "1",
		"requester_pidm": "54321",
		"ops": [
			{
				"type": "reclassify",
				"to_acct": "13",
				"orig_trans_id": "T32"
			},
			{
				"type": "reclassify",
				"to_acct": "14",
				"orig_trans_id": "T57"
			}
		]
	}
}';

BEGIN
	-- Yup, it's this easy.
	dbms_output.put_line('Let''s parse some JSON!');

	-- This creates a g_values of type apex_json.t_values.
	-- The subsequent apex_json.get_varchar2() calls read from that value by default.
    -- You can call an overload of parse to supply a destination value as the first arg.
	--
	apex_json.parse(request_json);

	value := apex_json.get_varchar2('request.id');
    dbms_output.put_line(value);

	-- This uses 1-based indexes.
	value := apex_json.get_varchar2('request.ops[%d].orig_trans_id', 1);
	dbms_output.put_line(value);

	-- Check if something exists at a given path.
	if apex_json.does_exist('request.ops[%d].to_acct', 2) then
		dbms_output.put_line('request.ops[2].to_acct exists');
	end if;

END;
/


