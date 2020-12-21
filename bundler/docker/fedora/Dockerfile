FROM fedora:32

RUN groupadd -g 9999 drFaustroll && useradd -r -u 9999 -g drFaustroll drFaustroll &&  mkdir /home/drFaustroll && chown -R \
drFaustroll:drFaustroll /home/drFaustroll && dnf upgrade -y && dnf clean all && dnf -y install openmpi-devel cmake \
make autoconf automake libtool sudo git wget gcc-c++ python-xmltramp scalapack-openmpi-devel hdf5-openmpi-devel \
gsl-devel patch openblas-devel vim blas-devel lapack-devel zlib-devel readline-devel check-devel libyaml-devel fftw3-devel fftw3-openmpi-devel && \
dnf -y clean all

WORKDIR /home/drFaustroll
USER drFaustroll
