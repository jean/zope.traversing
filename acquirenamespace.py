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
# FOR A PARTICULAR PURPOSE.
#
##############################################################################
"""

$Id: acquirenamespace.py,v 1.2 2002/12/25 14:13:26 jim Exp $
"""

from zope.app.traversing.namespaces import provideNamespaceHandler
from zope.app.traversing.exceptions import UnexpectedParameters
from zope.exceptions import NotFoundError
from zope.component import queryAdapter
from zope.proxy.context import ContextWrapper, getWrapperContext
from zope.app.interfaces.traversing.traversable import ITraversable

class ExcessiveWrapping(NotFoundError):
    """Too many levels of acquisition wrapping. We don't believe them."""

def acquire(name, parameters, pname, ob, request):
    if parameters:
        raise UnexpectedParameters(parameters)

    i = 0
    origOb = ob
    while i < 200:
        i += 1
        traversable = queryAdapter(ob, ITraversable, None)
        if traversable is not None:

            try:
                # XXX what do we do if the path gets bigger?
                path = []
                next = traversable.traverse(name, parameters, pname, path)
                if path: continue
            except NotFoundError:
                pass
            else:
                return ContextWrapper(next, ob, name=name)

        ob = getWrapperContext(ob)
        if ob is None:
            raise NotFoundError(origOb, pname)

    raise ExcessiveWrapping(origOb, pname)
