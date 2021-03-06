#!/usr/bin/python
# -*- coding: utf-8 -*-

""" This file is part of B{Domogik} project (U{http://www.domogik.org}).

License
=======

B{Domogik} is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

B{Domogik} is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with Domogik. If not, see U{http://www.gnu.org/licenses}.

Module purpose
==============



Implements
==========


@author: Domogik project
@copyright: (C) 2007-2009 Domogik project
@license: GPL(v3)
@organization: Domogik
"""

from django.conf.urls.defaults import *


urlpatterns = patterns('domoweb.view.views',
    url(r'^$', 'page', name="page_view"),
    url(r'^(?P<id>\d+)$', 'page', name="page_view"),
    url(r'^configuration/(?P<id>\d+)$', 'page_configuration', name="page_configuration_view"),
    url(r'^elements/(?P<id>\d+)$', 'page_elements', name="page_elements_view"),
    url(r'^elements/widgetparams/(?P<instanceid>n\d+)/(?P<featureid>\d+)/(?P<featuretype>[a-z.]+)$', 'page_elements_widgetparams', name="page_elements_widgetparams_view"),
)
