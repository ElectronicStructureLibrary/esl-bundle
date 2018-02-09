.. image:: https://gitlab.e-cam2020.eu/esl/esl-bundle/badges/master/build.svg
     :target: https://gitlab.e-cam2020.eu/esl/esl-bundle/commits/master


==============
The ESL Bundle
==============

The ``ESL Bundle`` is a collection of libraries and utilities broadly used in
electronic structure calculations, put together to make their use easier by
researchers and scientific software developers.

It has been created to improve the quality, robustness, portability, and
interoperability, of various packages developed independently but sharing
multiple interests and objectives.

The ``ESL Bundle`` downloads, builds and installs all necessary packages to
run an Electronic Structure Code as examplified by the `ESL Demo`_. It helps
users, developers and packagers obtain a working installation of complex
combinations of software packages without having to track the dependencies
themselves.

ESL stands for Electronic Structure Library, an initiative which distributes
quality software and promotes open standards for high-performance computing
applications in the field of electronic-structure calculations. More details
can be found on the `ESL Wiki`_.


Requirements
------------

To work properly, the ``ESL Bundle`` requires a series of Python 2.7 or above,
as well as a working installation of pkg-config_. Depending on the modules you
wish to build, some additional packages might be required (to be completed).


Installation
------------

The ``ESL Bundle`` comes with a version of JHBuild_ which has been tuned to
fit the context of electronic-structure applications. Most of the operations
are performed by executing the ``jhbuild.py`` script with appropriate
parameters.

JHBuild_ supports a wide variety of build systems, although it is not a build
system itself. It is rather a tool designed to ease the build of collections
of related source packages, that it calls "modules". It was originally written
for the `Gnome Project`_, but its use has then been extended to many other
situations.

.. note::

   It is highly recommended to use a build directory, in order to maintain the
   source tree in a clean state.

A typical way of installing the collection of ESL libraries is the following:

    mkdir my_build_dir
    cd my_build_dir
    ../jhbuild.py build

In the ``ESL Bundle``, JHBuild_ has been configured to build all ESL libraries
as one large metapackage. It installs all packages in an *install/*
subdirectory of the current directory.

To make the installed packages available to other applications, the most
important is to set the *PKG_CONFIG_PATH* environment variable. For a
Bourne-like shell, the command is::

  export PKG_CONFIG_PATH="/path/to/esl-bundle/my_build_dir/install/lib/pkgconfig:${PKG_CONFIG_PATH}"

while for a C-like shell it is::

  setenv PKG_CONFIG_PATH "/path/to/esl-bundle/my_build_dir/install/lib/pkgconfig:${PKG_CONFIG_PATH}"

where you replace ``/path/to/esl-bundle/my_build_dir`` by the full path to
your actual build directory.

Provided the application you wish to build is aware of pkg-config_, this
command will let it automatically configure all the libraries it needs to
build and run.

.. _`ESL Demo`: https://gitlab.e-cam2020.eu/esl/esl-demo
.. _`ESL Wiki`: https://esl.cecam.org/
.. _`Gnome Project`: https://www.gnome.org/
.. _JHBuild: https://developer.gnome.org/jhbuild/stable/
.. _pkg-config: https://www.freedesktop.org/wiki/Software/pkg-config/

