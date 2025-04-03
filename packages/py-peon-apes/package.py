# Copyright 2025 DLR
#
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyPeonApes(PythonPackage):
    """Small helper scripts for APES"""

    homepage = "https://github.com/apes-suite/peon-apes"

    url = "https://github.com/apes-suite/peon-apes/archive/refs/tags/v2025.04.03.tar.gz"

    maintainers("haraldkl")

    version("2025.04.03", sha256="e539b8ca930884c98dfafb786ba34a56a3760bea2e68e9df963925b0e6773064")

    extends("python")

    depends_on("py-setuptools", type="build")

    depends_on("py-pyratemp", type=("build", "run"))
    depends_on("lua", type=("run"))
