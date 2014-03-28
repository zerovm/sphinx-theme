from distutils.core import setup

setup(name='zerovm-sphinx-theme',
      version='1.0',
      description='ZeroVM theme for Sphinx',
      author='Martin Geisler',
      author_email='martin@geisler.net',
      url='https://github.com/zerovm/sphinx-theme',
      packages=['zerovm_sphinx_theme'],
      package_data={'zerovm_sphinx_theme': ['zerovm/theme.conf',
                                            'zerovm/static/*.css',
                                            'zerovm/static/*.css_t']}
)
