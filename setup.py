from setuptools import setup, find_packages

setup(
    name="dsss_homework_2",                     
    version="0.1.0",                            
    packages=find_packages(),                   
    description="A math quiz game",             
    long_description=open("README.md").read(),  
    long_description_content_type="text/markdown",
    url="https://github.com/Arnavthakur26/dsss_homework_2", 
    author="Arnav Thakur",
    classifiers=[                              
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",                    
)