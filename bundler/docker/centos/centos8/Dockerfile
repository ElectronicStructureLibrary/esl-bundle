FROM centos:8

RUN groupadd -g 9999 drFaustroll && useradd -r -u 9999 -g drFaustroll drFaustroll &&  mkdir /home/drFaustroll && chown -R \
drFaustroll:drFaustroll /home/drFaustroll && yum update -y && yum -y install epel-release &&yum -y install openmpi-devel cmake \
make autoconf automake libtool sudo git wget gcc-c++ scalapack-openmpi-devel hdf5-openmpi-devel \
gsl-devel patch vim openblas-devel blas-devel lapack-devel zlib-devel readline-devel check-devel libyaml-devel fftw-devel

WORKDIR /home/drFaustroll
USER drFaustroll
