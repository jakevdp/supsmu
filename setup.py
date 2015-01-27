from numpy.distutils.core import setup

DESCRIPTION = "Python wrapper of Friedman's Supersmoother code"
LONG_DESCRIPTION = open('README.md').read()
NAME = "supsmu"
AUTHOR = "Jake VanderPlas"
AUTHOR_EMAIL = "jakevdp@uw.edu"
MAINTAINER = "Jake VanderPlas"
MAINTAINER_EMAIL = "jakevdp@uw.edu"
URL = 'http://github.com/jakevdp/supsmu/'
DOWNLOAD_URL = 'http://github.com/jakevdp/supsmu/'
LICENSE = '(c) Jerome Friedman, All Rights Reserved'
VERSION = '0.1'

def configuration(parent_package='', top_path=None):
    from numpy.distutils.misc_util import Configuration
    config = Configuration(None, parent_package, top_path)

    # Avoid non-useful msg:
    # "Ignoring attempt to set 'name' (from ... "
    config.set_options(ignore_setup_xxx_py=True,
                       assume_default_configuration=True,
                       delegate_options_to_subpackages=True,
                       quiet=True)

    config.add_subpackage('supsmu')
    return config

setup(configuration=configuration,
      name=NAME,
      version=VERSION,
      description=DESCRIPTION,
      long_description=LONG_DESCRIPTION,
      author=AUTHOR,
      author_email=AUTHOR_EMAIL,
      maintainer=MAINTAINER,
      maintainer_email=MAINTAINER_EMAIL,
      url=URL,
      download_url=DOWNLOAD_URL,
      license=LICENSE,
      packages=['supsmu'
            ],
      classifiers=[
        'Development Status :: 4 - Beta',
          ],
     )
