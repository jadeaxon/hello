-- PRE: You are running APEX 5.0 or higher.
-- Oracle Express 11gR2 comes with APEX 4.0.2.  The apex_json stuff DNE here.
-- https://www.oracle.com/technetwork/developer-tools/apex/learnmore/upgrade-apex-for-xe-154969.html
-- Yup, I was able to upgrade to APEX 5.0.4.
--
-- The API reference for apex_json is here:
-- https://docs.oracle.com/cd/E59726_01/doc.50/e39149/apex_json.htm#AEAPI29660

set serveroutput on;

declare
	value varchar2(256);

	bvalue boolean;

	v_count number;

	parsed_json apex_json.t_values;

	-- List of JSON paths.
	paths apex_t_varchar2;

	-- JSON representing a request to reclassify some transactions.
	request_json varchar2(32767) := '
{
	"request": {
		"id": "1",
		"requester_pidm": "54321",
		"completed": true,
		"approved": false,
		"ops": [
			{
				"seq": 1,
				"type": "reclassify",
				"to_acct": "13",
				"orig_trans_id": "T32"
			},
			{
				"seq": 2,
				"type": "reclassify",
				"to_acct": "14",
				"orig_trans_id": "T57"
			},
			{
				"seq": 3,
				"type": "move",
				"from_index": "I80",
				"from_acct": "217",
				"to_index": "I15",
				"from_acct": "1011",
				"orig_trans_id": "T222"
			},
			{
				"seq": 4,
				"type": "reverse",
				"orig_trans_id": "T321"
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
	-- By default, these functions read from g_values.
	-- You can supply a 3rd argument to read from another parsed JSON object.
	value := apex_json.get_varchar2('request.ops[%d].orig_trans_id', 1);
	dbms_output.put_line(value);

	-- Get a boolean value.
	bvalue := apex_json.get_boolean('request.completed');
	if bvalue then
		dbms_output.put_line('The request has been completed.');
	end if;

	-- Get number of elements in a array.  Loop over each op in the request.
	v_count := apex_json.get_count('request.ops');
	dbms_output.put_line('The request contains ' || v_count || ' operations.');
	for i in 1 .. v_count loop
		value := apex_json.get_varchar2('request.ops[%d].type', i);
		dbms_output.put_line(value);
	end loop;

	-- Check if something exists at a given path.
	if apex_json.does_exist('request.ops[%d].to_acct', 2) then
		dbms_output.put_line('request.ops[2].to_acct exists');
	end if;

	-- Get a list of related paths.
	-- We want to find all transaction reclassification operations within the request.
    -- Note that we're using parsed_json instead of the default g_values here.
	-- Basically, we return a list of all request.ops[*] paths for which request.ops[i].type == 'reclassify'.
	apex_json.parse(parsed_json, request_json);
    paths := apex_json.find_paths_like (
        p_values => parsed_json, -- The parsed JSON (g_values by default).
        p_return_path => 'request.ops[%]', -- The path starts to search and return.
        p_subpath       => '.type', -- A subpath to query.
        p_value           => 'reclassify' -- The specific value to find.
	);

	-- Print the seq # of each reclassification operation.
    dbms_output.put_line('Reclassification operations:');
    for i in 1 .. paths.count loop
        dbms_output.put_line(apex_json.get_varchar2(p_values => parsed_json, p_path => paths(i) || '.seq'));
    end loop;

END;
/


