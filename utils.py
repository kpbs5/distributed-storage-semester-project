import random
import string
import os
from typing import Optional, List, Any, Iterable
import time

random.seed(time.time())


def random_string(length:int = 8) -> str:
    """
    Returns a random alphanumeric string of the given length. 
    Only lowercase ascii letters and numbers are used.

    :param length: Length of the requested random string 
    :return: The random generated string
    """
    return ''.join([random.SystemRandom().choice(string.ascii_letters + string.digits) for n in range(length)])
#

def write_file(data: bytes, filename: Optional[str] = None) -> Optional[str]:
    """
    Write the given data to a local file with the given filename

    :param data: A bytes object that stores the file contents
    :param filename: The file name. If not given, a random string is generated
    :return: The file name of the newly written file, or None if there was an error
    """
    if not filename:
        # Generate random filename
        filename = random_string(8)
        # Add '.bin' extension
        filename += ".bin"
    
    try:
        # Open filename for writing binary content ('wb')
        # note: when a file is opened using the 'with' statment, 
        # it is closed automatically when the scope ends
        with open(f'./{filename}', 'wb') as f:
            f.write(data)
    except EnvironmentError as e:
        print("Error writing file: {}".format(e))
        return None
    
    return filename
#

def is_raspberry_pi() -> bool:
    """
    Returns True if the current platform is a Raspberry Pi, otherwise False.
    """
    return os.uname().nodename == 'raspberrypi'
#

def remove_duplicate_from_list(lst: List[Any]) -> List[Any]:
    """
    Returns a new list with duplicate elements removed.
    """
    assert isinstance(lst, list), "The given argument is not a list, but a {}".format(type(lst))
    return list(set(lst))


def flatten_list(lst: List[Iterable[Any]]) -> List[Any]:
    """
    Returns a new list with all elements of the given list flattened.
    """
    assert isinstance(lst, list), "The given argument is not a list, but a {}".format(
        type(lst)
    )
    return [item for sublist in lst for item in sublist]
