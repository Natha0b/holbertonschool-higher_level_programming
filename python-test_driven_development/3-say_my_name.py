#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""function that divides all elements of a matrix."""


def say_my_name(first_name, last_name=""):
    """function that divides all elements of a matrix."""

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
