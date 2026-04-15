#!/usr/bin/env python3

try:
    x = 1 / 0
    y = "string" + 1
except ZeroDivisionError as e:
    print("You can't divide by zero.")
except TypeError as e:
    print(e)
except Exception as e:
    print("Unexpected exception.")
except:
    # Best to avoid using this catchall.
    print("Unexpected exception.")
else:
    print("No exceptions occurred.")
finally:
    print("Always run the finally block.")



