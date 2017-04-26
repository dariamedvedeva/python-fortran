from ctypes import byref, cdll, c_int

add = cdll.LoadLibrary('./add.so')

def call_fortran_subroutine():
    a = c_int(2)
    b = c_int(4)
    print add.test_(byref(a), byref(b))
    print "Python part has been done."

call_fortran_subroutine()