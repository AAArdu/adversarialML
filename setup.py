from setuptools import setup
from setuptools import find_packages

install_requires = [
    'numpy',
    'setuptools'
]

setup(
    name="advML",
    version='0.1.0',
    description="This lib includes some functions related to attack and defense methods in adversarial machine learning",
    long_description='',
    # classifiers=[
    #     "Development Status :: 3 - Alpha",
    #     "Intended Audience :: Developers",
    #     "Intended Audience :: Science/Research",
    #     "License :: OSI Approved :: MIT License",
    #     "Programming Language :: Python :: 2.7",
    #     "Programming Language :: Python :: 3",
    #     "Programming Language :: Python :: 3.5",
    #     "Programming Language :: Python :: 3.6",
    #     "Topic :: Scientific/Engineering :: Artificial Intelligence",
    # ],
    keywords="",
    author="Zhengjie Du",
    author_email="dz1833006@smail.nju.edu.cn",
    url="https://github.com/AAArdu/advML",
    license="MIT",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=install_requires,
    # extras_require={
    #     'testing': tests_require,
    #     ':python_version == "2.7"': ['future', 'futures'],
    # },
)