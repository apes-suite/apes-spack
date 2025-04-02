# Copyright 2025 DLR
#
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (MIT)

from spack.package import *


class Gleaner(PythonPackage):
    """Postprocessing of text files in APES."""

    homepage = "https://github.com/apes-suite/gleaner"
    git = "https://github.com/apes-suite/gleaner.git"

    maintainers("haraldkl")

    version("develop", preferred=True, get_full_repo=True)

    depends_on("py-setuptools", type="build")
    extends("python")
