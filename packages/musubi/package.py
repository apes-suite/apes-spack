# Copyright 2021,2025 DLR
#
# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (MIT)

from spack.package import *


class Musubi(WafPackage):
    """Lattice Boltzmann solver Musubi."""

    homepage = "https://www.apes-suite.org"
    git = "https://github.com/apes-suite/musubi.git"

    # notify when the package is updated.
    maintainers = ["haraldkl"]

    version("develop", preferred=True, get_full_repo=True, submodules=True)
    version("osdn", hg="https://hg.osdn.net/view/apes/musubi")
    version(
        "2.0.1",
        revision="77873c5b4c1eca128cde7c3f34fcf7144aeb2ba7",
        hg="https://hg.osdn.net/view/apes/musubi",
    )

    variant("openmp", default=False, description="Compile with OpenMP support")

    depends_on("mpi")
    depends_on("mercurial", type=("build",), when=("@2.0.1,osdn"))


class WafBuilder(spack.build_systems.waf.WafBuilder):
    def waf(self, *args, **kwargs):
        """Runs the waf ``Executable``."""
        import inspect
        import os

        jobs = inspect.getmodule(self.pkg).make_jobs
        wafexec = "waf"
        if self.spec.satisfies("@2.0.2:"):
            wafexec = os.path.join("bin", "waf")

        with working_dir(self.build_directory):
            self.python(wafexec, "-j{0}".format(jobs), *args, **kwargs)

    def configure_args(self):
        args = super(WafBuilder, self).configure_args()

        if self.spec.satisfies("+openmp"):
            args += ["--openmp"]

        return args

    def build_args(self):
        args = super(WafBuilder, self).build_args()
        args += ["--notests"]
        return args

    def install_args(self):
        args = super(WafBuilder, self).install_args()
        args += ["--notests"]
        return args

    def configure(self, pkg, spec, prefix):
        env["FC"] = spec["mpi"].mpifc
        super(WafBuilder, self).configure(pkg, spec, prefix)

    def build(self, pkg, spec, prefix):
        env["FC"] = spec["mpi"].mpifc
        super(WafBuilder, self).build(pkg, spec, prefix)

