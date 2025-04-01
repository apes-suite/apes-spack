# Copyright 2025 DLR
#
# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (MIT)

from spack.package import *


class Ateles(WafPackage):
    """Discontinuous Galerkin Solver Ateles."""

    homepage = "https://www.apes-suite.org"
    git = "https://github.com/apes-suite/ateles.git"

    # notify when the package is updated.
    maintainers = ["haraldkl"]

    version("develop", preferred=True, get_full_repo=True, submodules=True)
    depends_on("mpi")


class WafBuilder(spack.build_systems.waf.WafBuilder):
    def waf(self, *args, **kwargs):
        """Runs the waf ``Executable``."""
        import inspect
        import os

        jobs = inspect.getmodule(self.pkg).make_jobs
        wafexec = os.path.join("bin", "waf")

        with working_dir(self.build_directory):
            self.python(wafexec, "-j{0}".format(jobs), *args, **kwargs)

    def configure_args(self):
        args = super(WafBuilder, self).configure_args()

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

