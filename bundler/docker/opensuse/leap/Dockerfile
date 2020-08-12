FROM opensuse/leap:15.2
#FROM opensuse-esl:tumbleweed

RUN zypper dup -y  && zypper  in -y  gnu-compilers-hpc gnu-compilers-hpc-devel \
openmpi3-gnu-hpc openmpi3-gnu-hpc-devel libscalapack2-gnu-openmpi3-hpc libscalapack2-gnu-openmpi3-hpc-devel libhdf5-gnu-openmpi3-hpc \
hdf5-gnu-openmpi3-hpc-devel cmake make autoconf automake libtool python3 python3-xml  python2 python2-xml sudo git wget curl blas-devel lapack-devel \
gsl-devel patch lua-devel zlib-devel readline-devel libopenblas-gnu-hpc-devel \
check-devel hdf5-gnu-hpc-devel fftw3-gnu-openmpi3-hpc-devel fftw3-gnu-hpc-devel libyaml-devel vim

RUN /usr/sbin/groupadd -g 999 drFaustroll && /usr/sbin/useradd -r -u 999 -g drFaustroll drFaustroll &&  mkdir /home/drFaustroll && chown -R drFaustroll:drFaustroll /home/drFaustroll
WORKDIR /home/drFaustroll
USER drFaustroll
