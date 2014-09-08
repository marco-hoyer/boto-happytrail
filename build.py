
from pybuilder.core import use_plugin, init, Author

use_plugin("python.install_dependencies")
use_plugin("python.core")
use_plugin("python.unittest")
use_plugin("python.distutils")
use_plugin('copy_resources')
use_plugin("python.coverage")

name = "boto-happytrail"
default_task = "publish"

@init
def initialize(project):

    project.build_depends_on("mock")
    project.depends_on("boto")
    project.depends_on("prettytable")

