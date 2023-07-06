#!/usr/bin/python3
"""abric script that generates a .tgz archive from the
   contents of the web_static folder of your AirBnB Clone repository"""
from fabric.api import local
from fabric.api import get
from fabric.api import put
from fabric.api import reboot
from fabric.api import run
from fabric.api import sudo
from fabric.context_managers import cd
import time
import os.path


def do_pack():
    """create a tar file of the folder web_static"""
    da = "versions/web_static"
    ds = "%s_%s.tgz" % (da, time.strftime("%Y%m%d%H%M%S", time.gmtime()))
    if os.path.isdir("versions") is False:
        if local("mkdir -p versions").failed is True:
            return None
    if local("tar -cvzf {} web_static".format(ds)).failed is True:
        return None
    return ds
