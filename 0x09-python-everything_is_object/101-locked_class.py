#!/usr/bin/python3
"""Defines a locked class."""


class LockedClass:
    """
    Prevent the user from instantiating new LockedClass att
    for anything but att 'first_name'.
    """

    __slots__ = ["first_name"]
