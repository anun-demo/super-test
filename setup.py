from setuptools import setup, find_packages
setup(name='codecov',
      version='1.0',
      description='Test',
      author='Me',
      author_email='me@example.com',
      license='MIT',
      packages=find_packages(),
      install_requires=[
           "requests"
      ],
      zip_safe=False)
