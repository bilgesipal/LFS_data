from setuptools import setup


with open('requirements.txt') as f:
    requirements = f.read().splitlines()


setup(
    name='vect_it',
    version='0.0.0',
    author='BilgeS',
    description='sklearn vectorization wrapper',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)