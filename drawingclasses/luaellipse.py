#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Draw static ellipse
"""

from .luaplot import LuaGraph, LuaEllipses


class LuaEllipse(LuaGraph, LuaEllipses):
    def __init__(self, draw_area):

        LuaGraph.__init__(self, draw_area)
        LuaEllipses.__init__(self)

        self.name = "ellipse"
        self.color_name = "color"
        self.thickness_name = "thickness"

        self.dct = {
            "kind": "ellipse",
            "center": (0, 0),
            "radius": 10,
            "height": 1,
            "width": 1,
            "color": (200, 200, 200),
            "alpha": 1,
            "thickness": 8,
            "start_angle": 360,
            "end_angle": 0,
            "graduated": False,
            "number_graduation": 10,
            "angle_between_graduation": 10,
        }
