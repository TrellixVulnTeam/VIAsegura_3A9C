from setuptools import setup, find_packages

VERSION = '0.0.1.22' 
DESCRIPTION = 'A python package to interact with Inter-American Development Bank machine learning modelsto automatic label elements for iRAP certification'
LONG_DESCRIPTION = 'Test for package that executes iRAP label module'

setup(
       # the name must match the folder name 'verysimplemodule'
        name="viasegura_test", 
        version=VERSION,
        author="Jose Maria Marquez Blanco",
        author_email="jose.marquez.blanco@gmail.com",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=['tensorflow-gpu==2.3.0','numpy==1.18.5', 'tqdm', 'opencv-contrib-python==4.2.0.34','boto3==1.14.37'],        
        keywords=['Machine Learning', 'safe road'],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Programming Language :: Python :: 3",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: Microsoft :: Windows",
        ],
        include_package_data=True
)