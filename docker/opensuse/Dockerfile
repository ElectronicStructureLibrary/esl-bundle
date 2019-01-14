FROM opensuse:tumbleweed 
#FROM opensuse-esl:tumbleweed

RUN groupadd -g 999 drFaustroll && useradd -r -u 999 -g drFaustroll drFaustroll &&  mkdir /home/drFaustroll && chown -R \
drFaustroll:drFaustroll /home/drFaustroll &&  zypper dup -y  && zypper  in -y  gnu-compilers-hpc gnu-compilers-hpc-devel \
openmpi3-gnu-hpc openmpi3-gnu-hpc-devel libscalapack2-gnu-openmpi3-hpc libscalapack2-gnu-openmpi3-hpc-devel libhdf5-gnu-openmpi3-hpc \
hdf5-gnu-openmpi3-hpc-devel cmake make autoconf automake libtool python python-xml sudo git wget curl blas-devel lapack-devel \
gsl-devel libblacs2_2_0_2-gnu-openmpi3-hpc libblacs2_2_0_2-gnu-openmpi3-hpc-devel patch lua53-devel zlib-devel readline-devel \
check-devel hdf5-gnu-hpc-devel fftw3-gnu-openmpi3-hpc-devel fftw3-gnu-hpc-devel 
WORKDIR /home/drFaustroll
USER drFaustroll
