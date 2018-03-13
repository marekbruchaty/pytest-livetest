from setuptools import setup

setup(
    name='livetest',
    description='todo',
    long_description='todo',
    version='0.0.1',
    license='MIT',
    platforms=['osx'],
    packages=['livetest'],
    url='https://github.com/marekbruchaty/pytest-livetest/',
    author_email='marekbruchaty@gmail.com',
    author='Marek Bruchaty',
    entry_points={
        'pytest11': [
            'pytest-livetest = livetest.pytest_livetest',
        ]
    },
    install_requires=['pytest>=2.8.0,<4', 'coverage>=4'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Operating System :: POSIX',
        'Operating System :: MacOS :: MacOS X',
        'Topic :: Software Development :: Testing',
        'Topic :: Software Development :: Libraries',
        'Topic :: Utilities',
        'Programming Language :: Python', ],
)
