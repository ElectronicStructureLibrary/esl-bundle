Changelog
~~~~~~~~~

All notable changes to this project will be documented in this file.

The format is based on `Keep a Changelog <https://keepachangelog.com/en/1.0.0/>`_,
and this project adheres to `Semantic Versioning <https://semver.org/spec/v2.0.0.html>`_.

[0.6.0-1] - To be released
==========================

Changed
-------
- Libpsml to v1.1.10.

[0.5.0-1] - 2020-05-08
======================

Added
-----
- sgplib v1.14.1
- wannier90 v3.0.0
- ELSI-RCI v0.1.0
- MatrixSwitch v1.0.0 as a stand-alone library.
- LibOMM v1.0.0 as a stand-alone library.
- install-bundle wrapper to make the use of JHBuild easier.

  Changed
-------
- Fdict to v0.8.0.
- Flook to v0.8.1.
- Libfdf to v0.2.2.
- LibGridXC to v0.9.5
- NTPoly to v2.4.0
- SuperLU_DIST to v6.2.0
- ELSI to v2.5.0
- JHBuild to a new version supporting Python 3.

[0.4.2-1] - 25-02-2020
======================

Changed
-------
- LibPSML to v1.1.9.
- ELPA to v2019.05.002.

[0.4.1-1] - 2020-02-22
======================

Fixed
-----
- URLs of several package websites.

Changed
-------
- LibPSML to v1.1.8.

[0.4.0-1] - 2020-02-21
======================

Fixed
-----
- Compilation of Futile with recent intel compilers.
- Installation of Flook and Fdict on MacOS.

Changed
-------
- LibGridXC with autotoolized build system to 0.8.5.1.
- Fdict to v0.7.1.
- libvdwxc to v0.4.0.
- Libxc to v4.3.4.
- ELPA to v2019.05.001.
- NTPoly to v2.3.1.
- SuperLU_DIST to v6.1.1.
- ELSI to v2.3.1
- PEXSI to v1.2.0.

[0.3.1-2] - 2019-01-18
==========================

Added
-----
- Documentation about the bundle release process.

[0.3.1-1] - 2019-01-17
==========================

Fixed
-----
- Name of Libvdwxc in documentatation.
- ChangeLog.
- LibGridXC build-system by updating to v0.8.4.2.

Changed
-------
- Futile to align it with upstream BigDFT/Futile v1.8.3.
- PSolver to align it with upstream BigDFT/PSolver v1.8.3.

[0.3.0-2] - 2019-01-15
========================

Added
-----
- Configuration files: ubuntu-gcc-serial.rc, ubuntu-gcc-openmpi.rc, fedora-gcc-serial.rc, fedora-gcc-openmpi.rc, centos-gcc-serial.rc, centos-gcc-openmpi.rc.
  
[0.3.0-1] - 2019-01-14
========================

Added
-----
- Libvdwxc v0.3.2.
- NTPoly v2.1.
- PEXSI as a stand-alone library.
  
Changed
-------
- Fdict to v0.6.0.
- Libxc to v4.2.3.
- LibGridXC to v0.8.4.
- ELSI to v2.1.0.
- ELPA to v2018.11.001.
- PEXSI to v1.0.3.
- scotch to v6.0.0.

Removed
-------
- libyaml v0.1.6.

[0.2.0-4] - 2019-01-14
========================

Fixed
-----
- Incorrect Python requirements in documentation.

[0.2.0-3] - 2019-01-12
========================

Fixed
-----
- Incorrect ELPA version number in documentation.
- Bug in configuration files:  compilation of xmlf90 was failing with GCC because of long lines.

[0.2.0-2] - 2019-01-12
========================

Fixed
-----
- Typo in documentation.
  
[0.2.0-1] - 2018-07-09
========================

Added
-----
- ELPA as a stand-alone library.
- Author and license information for scotch and superlu_dist.
- Configuration files: debian-gcc-serial.rc, opensuse-gcc-serial.rc.
  
Changed
-------
- ELSI to v2.0.2
- ELPA to v2018.05.001.
- Configuration files for new ELSI version.
  
Fixed
-----
- Incorrect scotch version number in documentation.
  
[0.1.0] - 2018-06-07
========================

Added
-----
- Fdict v0.5.0.
- Flook v0.7.0.
- Futile v1.8.
- Libfdf v0.1.1.
- Libpsml v1.1.7.
- Libxc v3.0.1.
- libGridXC v0.8.0.3.
- PSolver v1.8.1.
- pspio v0.2.4.
- xmlf90 v1.5.4.
- libyaml v0.1.6.
- ELSI v180205.
- ELPA v2016.11.001.
- LibOMM (included in ELSI).
- MatrixSwitch (included in ELSI).
- PEXSI (included in ELSI).
- SIPs (included in ELSI).
- superlu_dist v5.3.0.
- scotch v6.0.4
- esl module set.
- esl-bundle and esl-bundle-mpi meta-modules.
- Configuration files: debian-gcc-openmpi.rc, gfortran+mpi.rc, opensuse-gcc-openmpi.rc.
