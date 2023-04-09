#!/usr/bin/python3
"""This module contain a function to deploy web static to a
web server"""
from fabric.api import env


def do_deploy(archive_path):
    """Deploy from an archive path given. Servers are specified at the
    commandline with fab"""
    from os.path import isfile
    from fabric.api import run, put

    if not isfile(archive_path):
        return False
    if not put(archive_path, '/tmp/').succeeded:
        return False
    try:
        run('sudo tar -xvzf /tmp/web_static_*.tgz -C /data/web_static/releases/')
        run('sudo rm /tmp/web_static_*.tgz /data/web_static/current')
        run(
            'sudo ln -s $(ls -t /data/web_static/releases|head -n 1)\
                    /data/web_static/current')
        return True
    except Exception:
        return False


env.hosts = ['54.237.226.36', '54.87.205.95']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/intranet_server_1'
