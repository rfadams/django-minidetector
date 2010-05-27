from setuptools import setup, find_packages
 
setup(
    name='minidetector',
    version='0.1',
    description='Django middleware and view decorator to detect phones and small-screen devices',
    author='Moof, Chris Drackett',
    author_email='chris@shelfworthy.com',
    url='http://github.com/chrisdrackett/minidetector',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 1',
        'Environment :: Web Environment',
        'Intended Audience :: Developers :: Designers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Utilities'
    ],