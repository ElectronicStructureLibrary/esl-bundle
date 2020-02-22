.. image:: https://gitlab.com/ElectronicStructureLibrary/esl-bundle/badges/master/pipeline.svg
     :target: https://gitlab.com/ElectronicStructureLibrary/esl-bundle/-/commits/master


==============
The ESL Bundle
==============

The ``ESL Bundle`` is a collection of libraries and utilities broadly used in
electronic structure calculations, put together to make their use easier by
researchers and scientific software developers. It includes a building framework
helping users, developers and packagers in obtaining a working installation of
complex combinations of software packages without having to track the
dependencies themselves.

ESL stands for Electronic Structure Library, an initiative which distributes
quality software and promotes open standards for high-performance computing
applications in the field of electronic structure calculations. More details
can be found on the `ESL Wiki`_.


Requirements
------------

To work properly, the ``ESL Bundle`` requires Python 3.x but still works with
Python 2.7 for now. Fortran, C and C++ compilers are also required, as most
modules are written in one or more of these programming languages. Some modules
also provide bindings for other languages. Depending on the modules you wish to
build, some additional packages might be required. These are packages that are
found in most Linux distributions and/or commonly available in HPC facilities,
and therefore it was not deemed necessary to include them in the ``ESL
Bundle``.

Some modules support parallelization through MPI. A working MPI installation is
necessary to build modules with MPI support.


Packages
--------

This is a complete list of packages included in the ``ESL Bundle``.

+--------------+-------------+----------+--------------+--------------------+--------------------------------------------------------+
| Package      | Version     | Language | Bindings     | Other dependencies | Website                                                |
+==============+=============+==========+==============+====================+========================================================+
| ELSI-RCI     | 0.1.0       | Fortran  |              |                    | http://elsi-interchange.org/                           |
+--------------+-------------+----------+--------------+--------------------+--------------------------------------------------------+
| Fdict        | 0.7.1       | Fortran  |              |                    | https://github.com/zerothi/fdict                       |
+--------------+-------------+----------+--------------+--------------------+--------------------------------------------------------+
| Flook        | 0.7.0       | Fortran  |              | Lua                | https://github.com/ElectronicStructureLibrary/flook    |
+--------------+-------------+----------+--------------+--------------------+--------------------------------------------------------+
| Futile       | 1.8.3       | Fortran  | C            |                    | https://gitlab.com/l_sim/futile                        |
+--------------+-------------+----------+--------------+--------------------+--------------------------------------------------------+
| Libfdf       | 0.1.1       | Fortran  |              |                    | https://gitlab.com/siesta-project/libraries/libfdf     |
+--------------+-------------+----------+--------------+--------------------+--------------------------------------------------------+
| Libpsml      | 1.1.9       | Fortran  |              |                    | https://gitlab.com/siesta-project/libraries/libpsml    |
+--------------+-------------+----------+--------------+--------------------+--------------------------------------------------------+
| Libxc        | 4.3.4       | C        | Fortran, C++ |                    | http://www.tddft.org/programs/libxc                    |
+--------------+-------------+----------+--------------+--------------------+--------------------------------------------------------+
| libGridXC    | 0.8.5       | Fortran  |              |                    | https://gitlab.com/siesta-project/libraries/libgridxc  |
+--------------+-------------+----------+--------------+--------------------+--------------------------------------------------------+
| libvdwxc     | 0.4.0       | C        | Fortran      | FFTW               | https://libvdwxc.org/                                  |
+--------------+-------------+----------+--------------+--------------------+--------------------------------------------------------+
| NTPoly       | 2.3.1       | Fortran  |              |                    | https://github.com/william-dawson/NTPoly               |
+--------------+-------------+----------+--------------+--------------------+--------------------------------------------------------+
| PSolver      | 1.8.3       | Fortran  |              |                    | https://gitlab.com/l_sim/psolver                       |
+--------------+-------------+----------+--------------+--------------------+--------------------------------------------------------+
| pspio        | 0.2.4       | C        | Fortran      | GSL                | https://gitlab.com/ElectronicStructureLibrary/libpspio |
+--------------+-------------+----------+--------------+--------------------+--------------------------------------------------------+
| xmlf90       | 1.5.4       | Fortran  |              |                    | https://gitlab.com/siesta-project/libraries/xmlf90     |
+--------------+-------------+----------+--------------+--------------------+--------------------------------------------------------+
| ELSI         | 2.3.1       | Fortran  | C            |                    | http://elsi-interchange.org/                           |
+--------------+-------------+----------+--------------+--------------------+--------------------------------------------------------+
| ELPA         | 2019.05.002 |          |              |                    | https://gitlab.mpcdf.mpg.de/elpa/elpa                  |
+--------------+-------------+----------+--------------+--------------------+--------------------------------------------------------+
| LibOMM       |             |          |              |                    | https://gitlab.com/ElectronicStructureLibrary/omm      |
+--------------+-------------+----------+--------------+--------------------+--------------------------------------------------------+
| MatrixSwitch |             |          |              |                    | https://gitlab.com/ElectronicStructureLibrary/omm      |
+--------------+-------------+----------+--------------+--------------------+--------------------------------------------------------+
| PEXSI        | 1.2.0       | C++      | Fortran      |                    | http://www.pexsi.org                                   |
+--------------+-------------+----------+--------------+--------------------+--------------------------------------------------------+
| SIPs         |             |          |              |                    | http://bitbucket.org/keceli/qetsc                      |
+--------------+-------------+----------+--------------+--------------------+--------------------------------------------------------+
| SuperLU_DIST | 6.1.1       |          |              |                    | http://crd-legacy.lbl.gov/~xiaoye/SuperLU              |
+--------------+-------------+----------+--------------+--------------------+--------------------------------------------------------+
| scotch       | 6.0.0       |          |              |                    | https://www.labri.fr/perso/pelegrin/scotch             |
+--------------+-------------+----------+--------------+--------------------+--------------------------------------------------------+



Installation
------------

The ``ESL Bundle`` comes with a version of JHBuild_ which has been tuned to
fit the context of the ESL. JHBuild_ supports a wide variety of build
systems, although it is not a build system itself. It is rather a tool designed
to ease the build of collections of related source packages, that it calls
"modules".  It was originally written for the `Gnome Project`_, but its use has
then been extended to other situations.

To make the use of JHBuild_ easier in the context of the ``ESL Bundle``, we
provide a wrapper script called ``install-bundle`` that can be found in the
top source directory of the bundle. Most of the operations are performed by
executing this ``install-bundle`` script with appropriate parameters. The
command line syntax is the following:

  install-bundle [global-options] [package(s) ...]

The following global options are available and can be shown running the
following command from the top source directory of the bundle:

    ./install-bundle -h

In particular, this command shows the currently possible values for each of
the options:

- -c, --compilers VENDOR: Use compilers from VENDOR instead of the default (gcc).
- -f, --flavor FLAVOR: Use the build parameters corresponding to FLAVOR
  (usually a MPI implementation) instead of the default (serial).
- -m, --moduleset NAME: Use the module set NAME instead of the default (esl).
  Please note that some module sets are still under development (abinit,
  siesta).
- -s, --system SYSTEM: Use the operating system or Linux distribution labelled
  SYSTEM instead of the default (generic).
- --exit-on-error: Exit immediately if a module fails to build instead of
  continuing with other modules.
- --no-interact: Do not prompt the user for any input. This option is useful
  if leaving a build unattended, in order to ensure that JHBuild will not
  prompt the user for input.
- --conditions ARGS: Change the way modules are built according to ARGS
  instead of the defaults. ARGS can be specified as e.g. +no_elpa (to skip the
  build of ELPA) or +yaml (if libyaml is missing on your system). This
  feature is still experimental and provides the above-mentioned examples
  only for now.

In the ``ESL Bundle``, the default module set is ``esl``. It provides a
meta-module called ``esl-bundle``, which builds and installs all the packages
included in the bundle. A second meta-module, called ``esl-bundle-mpi``, is
provided to build the packages with MPI support. Note that not all packages
can be compiled with MPI support. In that case they will be built without it.

The ``install-bundle`` script does not need to be invoked from the directory
where it is located.

.. note::

   To keep the source directory clean, we highly recommended the use of a build
   directory.

Therefore, a typical way of installing the collection of ESL libraries is the
following::

    mkdir my_build_dir
    cd my_build_dir
    ../install-bundle

By default, the ``build`` command will compile all the modules from the
``esl-bundle`` meta-module and install them in the current directory. This, and
a few other options, can be changed using configuration files. Several sample
configuration files are provided in the ``rcfiles/`` subdirectory. These files
should be suitable to build the bundle in a variety of systems, but they can
also be used as a starting point to write configuration files more suited to
your needs.

If you want to use the ``install-bundle`` script with your own config files,
please follow the naming convention ``SYSTEM-VENDOR-FLAVOR.rc``, where:
``SYSTEM`` is the operating system or Linux distribution the file is meant for,
or *generic* if it does not matter; ``VENDOR`` is the vendor of the C, C++ and
Fortran compilers used to build the packages; ``FLAVOR`` is the MPI
implementation to use, or *serial* if there is none. If you add support for a
new compiler vendor, please create a file named ``generic-VENDOR-serial.rc``
with the corresponding options, else the ``install-bundle`` script will
complain.

The configuration files use Python syntax. Here is a list of some important
options:

- ``modules``: dictionary of modules to build.
- ``prefix``: directory where the modules should be installed.
- ``checkoutroot``: where to unpack the module's sources.

Configuration options to be passed to the modules build systems can also be
specified in the configuration file. Here is an example of how to do this::

   # Set the FC variable when invoking the configure script for all modules
   autogenargs="FC=gfortran"

   # Run make in parallel with two threads
   makeargs="-j2"

   # Here the futile module requires an extra configuration option.
   # Note that this will overwrite the global options set by autogenargs, so we
   # have to add it here explicitly.
   module_autogenargs['futile'] = "--with-ext-linalg='-lopenblas' " + autogenargs 



pkg-config
----------

The ``ESL Bundle`` provides pkg-config_ files for all the modules. These can be
used to make the installed packages available to other applications.

To use this feature, a working installation of pkg-config_ is necessary.  To
make the installed packages available to other applications, the most important
is to set the *PKG_CONFIG_PATH* environment variable. For a Bourne-like shell,
the command is::

  export PKG_CONFIG_PATH="/path/to/esl-bundle/my_build_dir/install/lib/pkgconfig:${PKG_CONFIG_PATH}"

while for a C-like shell it is::
  setenv PKG_CONFIG_PATH "/path/to/esl-bundle/my_build_dir/install/lib/pkgconfig:${PKG_CONFIG_PATH}"

where you replace ``/path/to/esl-bundle/my_build_dir`` by the full path to your
actual build directory.

Provided the application you wish to build is aware of pkg-config_, this command
will let it automatically configure all the libraries it needs to build and run.

.. note::

   Please read the pkg-config_ documentation on how to use pkg-config_ to
   compile your application.


.. _`ESL Demo`: https://gitlab.e-cam2020.eu/esl/esl-demo
.. _`ESL Wiki`: https://esl.cecam.org/
.. _`Gnome Project`: https://www.gnome.org/
.. _JHBuild: https://developer.gnome.org/jhbuild/stable/
.. _pkg-config: https://www.freedesktop.org/wiki/Software/pkg-config/

