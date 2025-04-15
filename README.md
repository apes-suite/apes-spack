# apes-spack

This repository provides Spack packages for the APES tools.
To use:

```
git clone https://github.com/apes-suite/apes-spack.git
spack repo add apes-spack
```

Then you can install musubi, seeder, ateles, gleaner and apes-shepherd
accordingly via `spack install`.

## Development environment

After installing spack and getting this repo as described above, you
can set up a development environment for example for musubi like this:

```
spack env create -d dev
cd dev
spack env activate .
spack add musubi@develop seeder gleaner apes-shepherd py-peon-apes
spack develop musubi@develop
spack concretize -f
spack install
```

The `dev` directory is an arbitrary name, and you should end up with
`dev/musubi` holding the source code of Musubi and you can work in that
as usually, just using `spack install` instead of `bin/waf build`.
