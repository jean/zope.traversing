##############################################################################
#
# Copyright (c) 2001, 2002 Zope Corporation and Contributors.
# All Rights Reserved.
# 
# This software is subject to the provisions of the Zope Public License,
# Version 2.0 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE
# 
##############################################################################
"""

Revision information:
$Id: ObjectName.py,v 1.1 2002/06/15 20:38:17 stevea Exp $
"""
from Zope.Proxy.ContextWrapper import getWrapperData

from Interface import Interface

class IObjectName(Interface):

    def __str__():
        """Get a human-readable string representation
        """

    def __repr__():
        """Get a string representation
        """
        
    def __call__():
        """Get a string representation
        """

class ObjectName(object):

    __implements__ = IObjectName
    
    def __init__(self, context):
        self.context = context

    def __str__(self):
        dict = getWrapperData(self.context)
        name = dict and dict.get('name') or None
        if name is None:
            raise TypeError, \
                  'Not enough context information to get an object name'
        return name

    __call__ = __str__


class SiteObjectName(object):

    __implements__ = IObjectName
    
    def __init__(self, context):
        pass
        
    def __str__(self):
        return ''

    __call__ = __str__