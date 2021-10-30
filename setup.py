from distutils.core import setup
setup(
  name = 'hcap-bypass',
  packages = ['hcap-bypass'],
  version = '0.1',
  license='MIT',        
  description = 'A module that solves hcaptcha challenges!',
  author = '7gh',  
  author_email = 'droidslying@gmail.com',
  url = 'https://github.com/7gh/hcap-bypass',
  keywords = ['hcaptcha', 'bypass', 'hcap', 'hcap bypass', 'bypass hcaptcha'],
  install_requires=[        
          'math',
          'base64',
          'httpx',
          'urllib',
          'hashlib',
          'json'
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers', 
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.6'
  ],
)
