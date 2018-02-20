from setuptools import setup


def readme():
    with open('README.rst') as f:
        return f.read()


setup(name='flask-api-handler',
      version='0.1',
      description='A small wrapper for flask app to ease the endpoints creation',
      keywords='Flask API REST flask-restful',
      url='https://github.com/shahar84/flask-api-handler',
      author='Shahar Polak',
      author_email='makore.shahar@gmail.com',
      license='MIT',
      packages=['flask_api_handler'],
      install_requires=[
          'flask',
      ],
      include_package_data=True,
      zip_safe=False)
