# Copyright 2025 DLR
#
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack.package import *


class PyPyratemp(PythonPackage):
    """Simple Python templating library"""

    homepage = "https://www.simple-is-better.org/template/pyratemp.html"
    pypi = "pyratemp/pyratemp-0.3.2.tgz"

    maintainers("haraldkl", )

    version("0.3.2", sha256="c45ed656ada482a02fe780495f37a695e7671accb04f918f7e7f18abf877bc71")

    extends("python")
    depends_on("python@2.6:", type=("build", "run"))

    depends_on("py-setuptools", type="build")

#    # FIXME: Add additional dependencies if required.
#    # depends_on("py-foo", type=("build", "run"))
#
#    def config_settings(self, spec, prefix):
#        # FIXME: Add configuration settings to be passed to the build backend
#        # FIXME: If not needed, delete this function
#        settings = {}
#        return settings
