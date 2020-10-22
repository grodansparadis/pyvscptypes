# the inclusion of the tests module is not meant to offer best practices for
# testing in general, but rather to support the `find_packages` example in
# setup.py that excludes installing the "tests" package

import sys
sys.path.append('../pyvscptypes')
import vscp_type

def test_success():
    print(vscp_type.VSCP_TYPE_PROTOCOL_ACTIVATE_NEW_IMAGE_ACK)
    assert True

if __name__ == "__main__":
    test_success()
    print("Everything passed")