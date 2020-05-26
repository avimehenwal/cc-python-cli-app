from setuptools import setup, find_packages
import src

setup(
    name='{{cookiecutter.project_slug}}',
    version='{{cookiecutter.version}}',
    author='{{cookiecutter.author}}',
    author_email='{{cookiecutter.email}}',
    license='MIT',
    description='{{cookiecutter.project_description}}',
    long_description=open('README.md').read(),
    project_urls={
        'Documentation': 'https://github.com/avimehenwal/swissarmyknife',
        'Source': 'https://github.com/avimehenwal/swissarmyknife',
        'Tracker': 'https://github.com/avimehenwal/swissarmyknife/issues',
    },

    packages=find_packages(),
    python_requires='>=3.4',
    install_requires=[
        'doit',
        'click',
        'pylint',
        'coloredlogs',
    ],

    keywords='python cli cookiecutter template',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'License :: OSI Approved :: BSD License'
    ],
    tests_require=[
        'pytest',
        'pytest-cov',
        'pytest-flake8',
        'pytest-watch',
    ],

    extras_require={
        ':sys.platform == "darwin"': ['macfsevents'],
        ':sys.platform == "linux"': ['pyinotify'],
    },
    entry_points={
        'console_scripts': [
            'sak = src.__main__:main',
            # 'snake = src.snake:main',
        ]
    },
)
