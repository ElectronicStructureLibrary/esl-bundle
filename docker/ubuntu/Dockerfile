FROM ubuntu:latest

RUN groupadd -g 999 drFaustroll && useradd -r -u 999 -g drFaustroll drFaustroll && mkdir /home/drFaustroll && chown -R drFaustroll:drFaustroll \ 
/home/drFaustroll && apt update &&  apt install -y libscalapack-mpi-dev cmake make autoconf automake libtool \
python sudo git wget curl libblas-dev liblapack-dev libgsl-dev libhdf5-openmpi-dev pkg-config liblua5.2-dev zlib1g-dev check \
libhdf5-serial-dev g++ gfortran python-ruamel.yaml libyaml-dev libfftw3-mpi-dev libfftw3-dev
WORKDIR /home/drFaustroll
USER drFaustroll
