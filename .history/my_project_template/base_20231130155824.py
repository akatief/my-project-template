"""
my_project_template base module.

This is the principal module of the my_project_template project.
here you put your main classes and objects.

Be creative! do whatever you want!

If you want to replace this with a Flask application run:

    $ make init

and then choose `flask` as template.
"""

# example constant variable
NAME = "my_project_template"

# example of code duplication across three classes
class BaseClass:
    """Base class."""

    def __init__(self):
        self.name = NAME

    def __str__(self):
        return self.name
    
    def __repr__(self):
        return self.name
    
    def __eq__(self, other):
        return self.name == other.name

class SubClass1(BaseClass):
    """Sub class 1."""

    def __init__(self):
        self.name = NAME

    def __str__(self):
        return self.name
    
    def __repr__(self):
        return self.name + "1"
    
    def __eq__(self, other):
        return self.name == other.name
