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
        dest_path = archive_path.split(".")[0]
        dest = dest_path.split("/")[-1]
        run('mkdir -p /data/web_static/releases/{}'.format(dest))
        run('sudo tar -xvzf /tmp/web_static_*.tgz -C\
            /data/web_static/releases/{}'.format(dest))
        run('sudo rm /tmp/web_static_*.tgz /data/web_static/current')
        run('sudo ln -s /data/web_static/releases/{} /data/web_static/current'
            .format(dest))
        return True
    except Exception:
        return False


env.hosts = ['54.237.226.36', '54.87.205.95']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/intranet_server_1'
