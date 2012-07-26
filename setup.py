from setuptools import setup

requires = open('requirements.txt').readlines()

setup(
    name='confuzzle',
    author='Jamie Matthews',
    author_email='jamie.matthews@gmail.com',
    version='0.1.0',
    url='http://github.com/j4mie/confuzzle',
    py_modules=['confuzzle'],
    description='A tiny tool for generating templated config files',
    license='Public Domain',
    install_requires=requires,
    entry_points={
        'console_scripts': [
            'confuzzle = confuzzle:main'
        ]
    },
    classifiers=[
        'Programming Language :: Python',
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: Public Domain',
    ],
)
