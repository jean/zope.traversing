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
$Id: test_skin.py,v 1.2 2002/12/25 14:13:27 jim Exp $
"""

from unittest import TestCase, TestSuite, main, makeSuite
from zope.testing.cleanup import CleanUp # Base class w registry cleanup
from zope.publisher.browser import TestRequest

class Test(CleanUp, TestCase):

    def test(self):
        from zope.app.traversing.skinnamespace import skin

        request = TestRequest()
        self.assertEqual(request.getPresentationSkin(), '')
        ob = object()
        ob2 = skin('foo', (), '++skin++foo', ob, request)
        self.assertEqual(ob, ob2)
        self.assertEqual(request.getPresentationSkin(), 'foo')

def test_suite():
    return makeSuite(Test)

if __name__=='__main__':
    main(defaultTest='test_suite')