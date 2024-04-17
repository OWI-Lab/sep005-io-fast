import os
import re
from setuptools import setup

base_path = os.path.dirname(__file__)

# Read the project version from "__init__.py"
regexp = re.compile(r'.*__version__ = [\'\"](.*?)[\'\"]', re.S)

init_file = os.path.join(base_path, 'sep005_io_fast', '__init__.py')
with open(init_file, 'r') as f:
    module_content = f.read()

    match = regexp.match(module_content)
    if match:
        version = match.group(1)
    else:
        raise RuntimeError(
            'Cannot find __version__ in {}'.format(init_file))

# Read the "README.rst" for project description
with open('README.md', 'r') as f:
    readme = f.read()


if __name__ == '__main__':
    setup(
        name='sep005_io_fast',
        description='OpenFAST file read functions compliant with SDyPy SEP005',
        long_description=readme,
        license='MIT license',
        url='https://github.com/Abdulelah96/sep005_io_fast',
        version=version,
        author='Abdulelah Al-Ghuwaidi',
        author_email='Abdulelah.Al-Ghuwaidi@vub.be',
        maintainer='Abdulelah Al-Ghuwaidi',
        maintainer_email='Abdulelah.Al-Ghuwaidi@vub.be',
        keywords=['io','fast','SEP005'],
        packages=['sep005_io_fast'],
        classifiers=['Development Status :: 3 - Alpha',
                     'Intended Audience :: Developers',
                     'Programming Language :: Python :: 3.9']
    )