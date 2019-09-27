from setuptools import setup, find_packages, Extension
from Cython.Build import cythonize

sourcefiles = ['app/bootstrap.pyx', 'app/mod1.py', 'app/mod2.py']

extensions = cythonize(Extension(
            name="app.bootstrap",
            sources = sourcefiles,
    ))


kwargs = {
      'name':'app',
      'packages':find_packages(),
      'ext_modules':  extensions,
}


setup(**kwargs)
