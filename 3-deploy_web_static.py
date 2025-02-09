#!/usr/bin/python3
"""Fabric script that distributes an archive to your web servers"""
from fabric.api import local
from fabric.api import get
from fabric.api import put
from fabric.api import env
from fabric.api import reboot
from fabric.api import run
from fabric.api import sudo
from fabric.context_managers import cd
import time
import os.path
from datetime import datetime

env.hosts = ["54.197.92.158", "52.201.229.118"]


def do_pack():
    """create a tar file of the folder web_static"""
    da = "versions/web_static"
    now = datetime.now()
    dt_string = now.strftime("%Y%m%d%H%M%S")
    ds = "%s_%s.tgz" % (da, dt_string)
    """ds = "%s_%s.tgz" % (da, time.strftime("%Y%m%d%H%M%S", time.gmtime()))"""
    if os.path.isdir("versions") is False:
        if local("mkdir -p versions").failed is True:
            return None
    if local("tar -cvzf {} web_static".format(ds)).failed is True:
        return None
    return ds


def do_deploy(archive_path):
    """distributed the archive to my web servers"""
    if os.path.isfile(archive_path) is False:
        return False
    ds = archive_path.split("/")[-1]
    if put(archive_path, "/tmp/{}".format(ds)).failed is True:
        return False
    name = file.split(".")[0]
    if run("rm -rf /data/web_static/releases/{}/".
           format(name)).failed is True:
        return False
    if run("mkdir -p /data/web_static/releases/{}/".
           format(name)).failed is True:
        return False
    if run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/".
           format(file, name)).failed is True:
        return False
    if run("rm /tmp/{}".format(file)).failed is True:
        return False
    if run("mv /data/web_static/releases/{}/web_static/* "
           "/data/web_static/releases/{}/".format(name, name)).failed is True:
        return False
    if run("rm -rf /data/web_static/releases/{}/web_static".
           format(name)).failed is True:
        return False
    if run("rm -rf /data/web_static/current").failed is True:
        return False
    if run("ln -s /data/web_static/releases/{}/ /data/web_static/current".
           format(name)).failed is True:
        return False
    return True


def deploy():
    """distributed the archive to my web servers"""
    file = do_pack()
    if file is None:
        return False
    res = do_deploy(file)
    return res
