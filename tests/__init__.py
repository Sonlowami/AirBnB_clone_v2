#!/usr/bin/python3

"""
This module contain a function to clear a stream
"""


def clear(stream):
    """Clear a stream"""
    stream.seek(0)
    stream.truncate(0)
