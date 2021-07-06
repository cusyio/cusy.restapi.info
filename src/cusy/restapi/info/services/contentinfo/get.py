# -*- coding: utf-8 -*-
"""Service to get content information."""

from cusy.restapi.info.interfaces import ICusyRestapiInfoLayer
from plone.app.layout.navigation.root import getNavigationRootObject
from plone.restapi.interfaces import IExpandableElement
from plone.restapi.services import Service
from zope.component import adapter
from zope.interface import implementer
from zope.interface import Interface

import plone.api


@implementer(IExpandableElement)
@adapter(Interface, ICusyRestapiInfoLayer)
class ContentInfo(object):
    def __init__(self, context, request):
        self.context = context
        self.request = request

    def __call__(self, expand=False):
        result = {
            "contentinfo": {
                "@id": "{}/@contentinfo".format(self.context.absolute_url()),
            }
        }
        if not expand:
            return result

        default_page = self.context.getDefaultPage()
        default_page_url = None
        if default_page is not None:
            default_page_url = self.context.absolute_url() + "/" + default_page

        layout = self.context.getLayout()
        if layout == "view":
            layout = "{0}{1}".format(
                self.context.getPortalTypeName(),
                "View",
            )

        portal = plone.api.portal.get()
        navigation_root = getNavigationRootObject(self.context, portal)
        result["contentinfo"].update(
            {
                "default_page": default_page_url,
                "layout": layout,
                "navigation_root": navigation_root.absolute_url(),
                "current_language": plone.api.portal.get_current_language(
                    context=self.context
                ),
            }
        )

        return result


class ContentInfoGet(Service):
    def reply(self):
        info = ContentInfo(self.context, self.request)
        return info(expand=True)["contentinfo"]
