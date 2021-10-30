from distutils.core import setup
setup(
  name = 'hcap-bypass',         # How you named your package folder (MyLib)
  packages = ['hcap-bypass'],   # Chose the same as "name"
  version = '0.1',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'A module that solves hcaptcha challenges!',   # Give a short description about your library
  author = 'Luke Cool',                   # Type in your name
  author_email = 'droidslying@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/user/reponame',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/user/reponame/archive/v_01.tar.gz',    # I explain this later on
  keywords = ['hcaptcha', 'bypass', 'hcap', 'hcap bypass', 'bypass hcaptcha'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'math',
          'base64',
          'httpx',
          'urllib',
          'hashlib',
          'json'
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.6'
  ],
)