# You can save simple Python values as JSON text files. And read them back in.

# Dump data structure to JSON string.

import os
script_dir = os.path.dirname(__file__)

from pathlib import Path
import json

data = {}
data['fruit'] = ['apple', 'banana', 'grape']
data['cities'] = ['New York', 'London', 'San Francisco']

# Think of "dumps" as "dump to string".
json_dump = json.dumps(data)
print('JSON string: ' + json_dump)

# Save JSON to file.
file = Path(f'{script_dir}/data.json')
file.write_text(json_dump)

# Let's restore the object from the JSON file.
json_from_file = file.read_text()

# Think of "loads" as "load from string".
data2 = json.loads(json_from_file) # Convert JSON string back to data structure.
print(data2['fruit'])





