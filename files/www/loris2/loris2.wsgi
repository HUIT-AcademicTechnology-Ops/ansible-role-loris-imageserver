#!/usr/bin/env python
from loris.webapp import create_app

# Uncomment and configure below if you are using virtualenv
# import site
# site.addsitedir('/path/to/my/virtualenv/lib/python2.x/site-packages')

application = create_app(config_file_path='/etc/loris2/loris2.conf')