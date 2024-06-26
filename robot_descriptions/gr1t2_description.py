#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""GR1T2 description."""

from os import getenv as _getenv
from os import path as _path

from ._cache import clone_to_cache as _clone_to_cache

REPOSITORY_PATH: str = _clone_to_cache(
    "gr1_description",
    commit=_getenv("ROBOT_DESCRIPTION_COMMIT", None),
)

PACKAGE_PATH: str = _path.join(REPOSITORY_PATH, "src", "robots", "gr1t2_description")


URDF_PATH: str = _path.join(PACKAGE_PATH, "urdf", "GR1T2.urdf")
