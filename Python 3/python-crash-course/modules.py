# Modules.
# Basically namespaces.

# You can import a module into your program.
# We get some kind of warning here if we remove the comment below, but it still works.
import module # type: ignore

# The module 'module' is defined in module.py.
module.module_function()

# This imports the given function(s) into the current namespace.
# from <module> import <symbol1>, ..., <symbolN>
# from <module> import * # Shy away from using this though.
from module import module_function

module_function()

# Give the function a different name here.
from module import module_function as mf

mf()

# Give the entire module a different name here.
# This is probably the best way to import anything.
import module as m
m.module_function()
