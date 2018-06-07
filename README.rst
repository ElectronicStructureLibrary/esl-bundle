.. image:: https://gitlab.e-cam2020.eu/esl/esl-bundle/badges/master/build.svg
     :target: https://gitlab.e-cam2020.eu/esl/esl-bundle/commits/master


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
applications in the field of electronic structure calculations. More details can
be found on the `ESL Wiki`_.


Requirements
------------

To work properly, the ``ESL Bundle`` requires Python 2.7 or above. Fortran and C
compilers are also required, as most modules are written in one or both of these
programming languages. Some modules also provide bindings for other
languages. Depending on the modules you wish to build, some additional packages
might be required. These are packages that are found in most Linux distributions
and/or commonly available in HPC facilities, and therefore it was deemed
necessary to include them in the ``ESL Bundle``.

Some modules support parallelization through MPI. A working MPI installation is
necessary to build modules with MPI support.


Packages
--------

This is a complete list of packages included in the ``ESL Bundle``.

+--------------+-------------+----------+--------------+--------------------+-----------------------------------------------------+
| Package      | Version     | Language | Bindings     | Other dependencies | Website                                             |
+==============+=============+==========+==============+====================+=====================================================+
| Fdict        | 0.5.0       | Fortran  |              |                    | https://github.com/zerothi/fdict                    |
+--------------+-------------+----------+--------------+--------------------+-----------------------------------------------------+
| Flook        | 0.7.0       | Fortran  |              | Lua                | https://github.com/ElectronicStructureLibrary/flook |
+--------------+-------------+----------+--------------+--------------------+-----------------------------------------------------+
| Futile       | 1.8         | Fortran  | C            |                    | http://bigdft.org/                                  |
+--------------+-------------+----------+--------------+--------------------+-----------------------------------------------------+
| Libfdf       | 0.1.1       | Fortran  |              |                    | https://launchpad.net/libfdf                        |
+--------------+-------------+----------+--------------+--------------------+-----------------------------------------------------+
| Libpsml      | 1.1.7       | Fortran  |              |                    | https://launchpad.net/libpsml                       |
+--------------+-------------+----------+--------------+--------------------+-----------------------------------------------------+
| Libxc        | 3.0.1       | C        | Fortran, C++ |                    | http://www.tddft.org/programs/libxc                 |
+--------------+-------------+----------+--------------+--------------------+-----------------------------------------------------+
| libGridXC    | 0.8.0.3     | Fortran  |              |                    | https://launchpad.net/libgridxc                     |
+--------------+-------------+----------+--------------+--------------------+-----------------------------------------------------+
| PSolver      | 1.8.1       | Fortran  |              |                    | http://bigdft.org/                                  |
+--------------+-------------+----------+--------------+--------------------+-----------------------------------------------------+
| pspio        | 0.2.4       | C        | Fortran      | GSL                | https://gitlab.e-cam2020.eu/esl/pspio               |
+--------------+-------------+----------+--------------+--------------------+-----------------------------------------------------+
| xmlf90       | 1.5.4       | Fortran  |              |                    | https://launchpad.net/xmlf90                        |
+--------------+-------------+----------+--------------+--------------------+-----------------------------------------------------+
| libyaml      | 0.1.6       | C        |              |                    | https://github.com/yaml/libyaml                     |
+--------------+-------------+----------+--------------+--------------------+-----------------------------------------------------+
| ELSI         | 180205      | Fortran  | C            |                    | http://elsi-interchange.org/                        |
+--------------+-------------+----------+--------------+--------------------+-----------------------------------------------------+
| ELPA         | 2016.11.001 |          |              |                    | https://gitlab.mpcdf.mpg.de/elpa/elpa               |
+--------------+-------------+----------+--------------+--------------------+-----------------------------------------------------+
| LibOMM       |             |          |              |                    | https://gitlab.e-cam2020.eu/esl/omm                 |
+--------------+-------------+----------+--------------+--------------------+-----------------------------------------------------+
| MatrixSwitch |             |          |              |                    | https://gitlab.e-cam2020.eu/esl/omm                 |
+--------------+-------------+----------+--------------+--------------------+-----------------------------------------------------+
| PEXSI        |             |          |              |                    | https://math.berkeley.edu/~linlin/pexsi             |
+--------------+-------------+----------+--------------+--------------------+-----------------------------------------------------+
| SIPs         |             |          |              |                    | http://bitbucket.org/keceli/qetsc                   |
+--------------+-------------+----------+--------------+--------------------+-----------------------------------------------------+
| superlu_dist | 5.3.0       |          |              |                    | http://crd-legacy.lbl.gov/~xiaoye/SuperLU           |
+--------------+-------------+----------+--------------+--------------------+-----------------------------------------------------+
| scotch       | 6.4.0       |          |              |                    | https://www.labri.fr/perso/pelegrin/scotch          |
+--------------+-------------+----------+--------------+--------------------+-----------------------------------------------------+



Installation
------------

The ``ESL Bundle`` comes with a version of JHBuild_ which has been tuned to fit
the context of the ESL. JHBuild_ supports a wide variety of build systems,
although it is not a build system itself. It is rather a tool designed to ease
the build of collections of related source packages, that it calls "modules". It
was originally written for the `Gnome Project`_, but its use has then been
extended to other situations.

Most of the operations are performed by executing the ``jhbuild.py`` script with
appropriate parameters. The command line syntax is the following:

  jhbuild.py [global-options] command [command-arguments]


The following global options are available:
  
  -f, --file config  Use an alternative configuration file instead of the default
                     ~/.config/jhbuildrc.
  
  -m, --moduleset moduleset  Use a module set other than the module set listed in
                             the configuration file. This option can be a
                             relative path if the module set is located in the
                             JHBuild moduleset folder, or an absolute path if
                             located elsewhere.

  --no-interact  Do not prompt the user for any input. This option is useful if
                 leaving a build unattended, in order to ensure the build is not
                 interrupted.

  
In the ``ESL Bundle``, the default module set is `esl`. This module set provides
a meta-module called `esl-bundle`, which builds and installs all the packages
included in the bundle. A second meta-module called `esl-bundle-mpi` is
provided, that builds the packages with MPI support. Note that not all packages
can be compiled with MPI support. In that case they will be built without it.

The ``jhbuild.py`` script does not need to be invoked from the directory where
it is located.

.. note::

   To keep the source directory clean, we highly recommended the use of a build
   directory.

Therefore, a typical way of installing the collection of ESL libraries is the
following:

    mkdir my_build_dir
    cd my_build_dir
    ../jhbuild.py build

By default, the `build` command will compile all the modules from the
`esl-bundle` meta-module and install them in the current directory. This, and a
few other options, can be changed in the configuration file. Several sample
configuration files are provided in the `rcfiles` directory. These files should
be suitable to build the bundle in a variety of systems, but they can also be
used as a starting point to write configuration files more suited to your needs.

The configuration files use Python syntax. Here is a list of some important
options:

- `modules`: dictionary of modules to build.
- `prefix`: directory where the modules should be installed.
- `checkoutroot`: where to unpack the module's sources.

Configuration options to be passed to the modules build systems can also be
specified in the configuration file. Here is an example of how to do this:

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

The `ESL Bundle` provides pkg-config_ files for all the modules. These can be
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

