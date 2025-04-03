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

    version("2025.04.04", sha256="da5f0f36caf84335dc30a60439e3dbe5edfb47077d3ce0c3def24d915dacabfa")

    extends("python")

    depends_on("py-setuptools", type="build")

    depends_on("py-pyratemp", type=("build", "run"))
    depends_on("lua", type=("run"))
