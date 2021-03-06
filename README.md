Bright Fabric
=============

**Bright Interactive's Fabric Utilities.**

**Author:** [Bright Interactive][1].

Overview
========

Useful Fabric commands to include in your projects

### Commands

#### fab pylint

Validates the code layout for all python files in configured paths using flake8

##### Configuration

 * pylint_ignore_errors: Set codes to ignore in a list (eg ['E500', 'E501'])
 * pylint_dirs: Set dirs to search for python files in (defaults to current dir)
 * pylint_exclude_dirs: Set dirs exclude when searching for python files to lint

Development
===========

Create a virtualenv and activate it:

    virtualenv /path/to/env
    . /path/to/env/bin/activate
    
Then install requirements for the app and for tests

    pip install -e .
    pip install -r requirements.txt


Testing
=======

Run test using the command
    
    python -m unittest discover
    

Publishing releases to PyPI
===========================

Only Bright Interactive employees can publish a release. Ensure you have a .pypirc file in your home directory configured to publish to the bright PyPI account (real password has been redacted).

```
[pypirc]
servers = pypi

[server-login]
username:bright
password:******
```

To publish a new version of your app to PyPI, set the `__version__` string in
your package's `__init__.py`, then run:

	# Publish to PyPI
    ./setup.py publish
	# Tag (change 1.0.0 to the version you are publishing!)
	git tag -a v1.0.0 -m 'Version 1.0.0'
	git push --tags


Changelog
=========

0.1.0
-----

bright_fabric.fabfile and bright_fabric.fab have been deprecated and will be
removed in version 1.0.0.

Use bright_fabric.tasks and bright_fabric.util instead

No flake8 errors are ignored by default. To return to the existing behaviour you
have to add this line to your fabfile.py

    env.pylint_ignore_errors = ['E501']

All python files in the current folder are included by default in pylint. If you 
want to return to a behaviour similar to the previous one use:
    
    env.pylint_dirs = ['project', 'apps', 'apps_test']


No folders are excluded from pylint by default. To configure a similar behaviour
to the previous one, use:

    env.pylint_exclude_dirs = ['migrations', 'settings']

0.0.1
-----

* First release that actually contained any code!

0.0.0
-----

* Initial empty release


License
=======

Copyright (c) Bright Interactive Limited.
Started with django-reusable-app Copyright (c) DabApps.

All rights reserved.

Redistribution and use in source and binary forms, with or without 
modification, are permitted provided that the following conditions are met:

Redistributions of source code must retain the above copyright notice, this 
list of conditions and the following disclaimer.
Redistributions in binary form must reproduce the above copyright notice, this 
list of conditions and the following disclaimer in the documentation and/or 
other materials provided with the distribution.
THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND 
ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED 
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE 
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE 
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL 
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR 
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER 
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, 
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE 
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

[1]: http://www.bright-interactive.com/
