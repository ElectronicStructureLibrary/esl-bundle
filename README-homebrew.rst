iHomebrew instructions
======================

*note at the moment there is not one to one correspondence between linux and MacOS bundles due to various issues.*

we do not build due to problems 
with the build system
- fdict
- flook

with dependencies
- libvdwxc, for mpi missing fftw3 with mpi support

setup brew
----------


.. code-block:: bash

  /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"


install esl-bundle dependencies
-------------------------------

.. code-block:: bash
  
   brew install open-mpi

one also needs to setup various environment variables to be sure right compilers are used

.. code-block:: bash

  export CC=gcc-8
  export CXX=g++-8
  export FC=gfortran-8
  export CPP=cpp-8
  export OMPI_CC=$CC
  export OMPI_CXX=$CXX
  export OMPI_FC=$FC
  # to fight bad build systems
  alias gcc=$CC
  alias g++=$CXX
  alias gfortran=$FC


you can save the above variables in a file and source them in the environment when needed.

install needed libraries

.. code-block:: bash 

   brew install scalapack fftw libyaml pkgconfig cmake zlib autoconf gsl

install bubdle
--------------

serial version

.. code-block:: bash

  ./jhbuild.py -f rcfiles/mojave-gcc-serial.rc build esl-bundle-mac

MPI version

.. code-block:: bash

  ./jhbuild.py -f rcfiles/mojave-gcc-openmpi.rc build esl-bundle-mpi-mac







