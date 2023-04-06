#!/usr/bin/python3
"""This script contains a function to archieve the webstatic folder"""


def do_pack():
    """Pack all html directories into a tar.gz file"""
    from fabric.api import local
    from datetime import datetime
    now = datetime.now()
    local('mkdir -p versions')
    pth = 'versions/web_static_{}{}{}{}{}{}'.format(now.year, now.month,
                                                    now.day, now.hour,
                                                    now.minute, now.second)
    result = local('tar -czvf {}.tgz web_static/'.format(pth))
    if result.succeeded:
        return pth
