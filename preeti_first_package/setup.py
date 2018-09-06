import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
     name='preeti',
     version='0.1',
     scripts=['preeti'] ,
     author="Preeti Duhan",
     author_email="prtduhan@gmail.com",
     description="hello world",
     long_description=long_description,
     long_description_content_type="text/markdown",
     packages=setuptools.find_packages(),
     url="https://github.com/preetiduhan/preeti",
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
)