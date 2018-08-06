# -*- coding: utf-8 -*-
"""
Created on Sat Jun 23 18:38:55 2018

@author: SilverDoe
"""

'''

>> dtype objects are constructed by combinations of fundamental data types
>> With the aid of dtype we are capable to create "Structured Arrays", - also known as "Record Arrays".
>> The structured arrays provide us with the ability to have different data types per column.

>> A data type object describes interpretation of fixed block of memory corresponding 
    to an array, depending on the following aspects :
        
        1. Type of data
        2. Size of data
        3. Byte order. The byte order is decided by prefixing '<' or '>' to data type
        
numpy.dtype(object, align, copy)

    Object − To be converted to data type object
    Align − If true, adds padding to the field to make it similar to C-struct
    Copy − Makes a new copy of dtype object. If false, the result is reference to builtin data type object

'''


import numpy as np 
dt = np.dtype(np.int32) #int8, int16, int32, int64 can be replaced by equivalent string 'i1', 'i2','i4', etc. 
print(dt)

# using endian notation 
import numpy as np 
dt = np.dtype('>i4') 
print(dt)

# structured data type 
import numpy as np 
dt = np.dtype([('age',np.int8)]) 
print(dt) 
# and applying to ndarray object
a = np.array([(10,),(20,),(30,)], dtype = dt)
print(a)


# creating structured arrays
import numpy as np
dt = np.dtype([('Name', 'S20'), ('Age', 'i4')])
data =[
    ('Natsu', 20),
    ('Lucy', 20),
    ('Erza', 23),
    ('Gray', 23),
    ('Wendy', 12),
    ('Gellal', 23),]

members = np.array(data,dtype=dt)
print(members[:4])



'''===================== Data Types ===========================================

1. bool_       : Boolean (True or False) stored as a byte

2. int_        : Default integer type (same as C long; normally either int64 or int32)

3. intc        : Identical to C int (normally int32 or int64)

4.	intp        : Integer used for indexing (same as C ssize_t; normally either int32 or int64)

5. int8        : Byte (-128 to 127)

6. int16       : Integer (-32768 to 32767)

7. int32       : Integer (-2147483648 to 2147483647)

8. int64       : Integer (-9223372036854775808 to 9223372036854775807)

9. uint8       : Unsigned integer (0 to 255)

10. uint16     : Unsigned integer (0 to 65535)

11. uint32     : Unsigned integer (0 to 4294967295)

12. uint64     : Unsigned integer (0 to 18446744073709551615)

13. float_     : Shorthand for float64

14. float16    : Half precision float: sign bit, 5 bits exponent, 10 bits mantissa

15. float32    : Single precision float: sign bit, 8 bits exponent, 23 bits mantissa

16. float64    : Double precision float: sign bit, 11 bits exponent, 52 bits mantissa

17. complex_   : Shorthand for complex128

18. complex64  : Complex number, represented by two 32-bit floats (real and imaginary components)

19. complex128 : Complex number, represented by two 64-bit floats (real and imaginary components)


'''



np.dtype(float).itemsize
np.dtype(np.float32).itemsize
np.dtype('|S4').itemsize
np.dtype('int8').itemsize
np.dtype('int16').itemsize


np.arange(100).size
np.arange(100).itemsize
np.arange(100).nbytes











