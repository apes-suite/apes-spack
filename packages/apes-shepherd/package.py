# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ApesShepherd(PythonPackage):
    """APES tool to run simulations parameterized"""

    homepage = "https://github.com/apes-suite/apes-shepherd"

    url = "https://github.com/apes-suite/apes-shepherd/archive/refs/tags/v2025.04.02.tar.gz"
    git = "https://github.com/apes-suite/apes-shepherd.git"

    maintainers("haraldkl")


    version("develop", preferred=True, get_full_repo=True)
    version("2025.04.02", sha256="57b57cae77abfc27b8e70636b35ec570362f7150911a3aaa3d4e3f542c0d4e50")

    extends("python@3:")
    #depends_on("python@3:", type=("build", "run"))

    depends_on("py-setuptools", type="build")

    depends_on("py-numpy", type=("build", "run"))
    depends_on("py-pyratemp", type=("build", "run"))
