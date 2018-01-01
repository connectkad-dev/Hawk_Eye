# -*- coding: utf-8 -*-
"""
/***************************************************************************
 Hawk_Eye
                                 A QGIS plugin
 Telecom site mapper and Planner
                             -------------------
        begin                : 2017-12-27
        copyright            : (C) 2017 by Joyjeet Chowdhury
        email                : joyjeetchowdhury@gmail.com
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load Hawk_Eye class from file Hawk_Eye.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .Hawk_Eye import Hawk_Eye
    return Hawk_Eye(iface)
