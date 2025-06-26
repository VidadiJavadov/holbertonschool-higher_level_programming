#!/usr/bin/python3
"""this is a class that inherits from list"""


class MyList(list):
    """Sorted Mylist"""

    def print_sorted(self):
        """Method for soring list"""

        print(sorted(self))

