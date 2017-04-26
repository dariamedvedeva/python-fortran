# python-fortran
1. Create fortran file. 

2. Compile fortran file like, for example, "gfortran -shared -fPIC -g -o add.so add.f90"
Description previous command: 
gfortran  ==  call compiler
-shared   ==  flag determined a type of generating lib
-fPIC     ==  flag that means "Generate position-independent code (PIC)"
-g        ==  
-o        ==  flag determaned to create object file with extension ".o"
add.so    ==  creating file
add.f90   ==  source file (file with source code)

3. Use in the terminal a command like "nm -ao add.so | grep test"
Description:
nm        ==  Linux command printed the information about binary files
-ao       ==  
add.so    ==  name of binary file
grep      ==  search
test      ==  name of my test fortran function
As a result you'll see the name of your function in the generated file, and it gives something like:

add.so: 0000000000000f8e - 01 0000   FUN _test_
add.so: 0000000000000f8e T _test_

In python file I called fortran function like "test_(variable_name, variable_name)".

4. Import .so file into python code.

5. Run python code. 
