
def configuration(parent_package='',top_path=None):
    from numpy.distutils.misc_util import Configuration
    config = Configuration('supsmu',parent_package,top_path)

    config.add_extension('_supsmu',
                         sources = ['_supsmu.pyf','_supsmu.f'])
    return config

if __name__ == "__main__":
    from numpy.distutils.core import setup
    setup(**configuration(top_path='').todict())
