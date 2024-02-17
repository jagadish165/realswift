import setuptools

setuptools.setup(
	name="realswift",
	version="3.0.2",
	author="Jagadish Dabbiru",
	author_email="jagadish.dabbiru@gmail.com",
	packages=["realswift"],
	description="AI automation tool leverages a cognitive approach inspired by the human brain's intuitive understanding of web interfaces",
	long_description="This project performs user interactions with OpenCV2 by integrating the PyAutoGUI library alongside custom utility functions. The script offers a range of functionalities, including simulating user actions like typing, clicking, scrolling, and hovering. These actions are executed within a defined window or specific area, enhancing the automation of user interactions",
	long_description_content_type="text/markdown",
	url="https://github.com/jagadish165/realswift",
	license='BSD-2-Clause',
classifiers=[
        "Topic :: Software Development :: Testing",
        "Topic :: Internet :: WWW/HTTP :: Browsers",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
    ],
	python_requires='>=3.8',
	install_requires=[
		'easyocr==1.7.1',
		'numpy==1.26.4',
		'opencv_python_headless==4.8.1.78',
		'Pillow==10.2.0',
		'psutil==5.9.5',
		'PyAutoGUI==0.9.54',
		'PyGetWindow==0.0.9',
		'setuptools==65.5.0',
		'wand==0.6.13'
	]
)
