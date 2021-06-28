# -*- coding: utf-8 -*-
"""Service to get site information."""

from cusy.restapi.info.interfaces import ICusyRestapiInfoLayer
from plone.registry.interfaces import IRegistry
from plone.restapi.interfaces import IExpandableElement
from plone.restapi.services import Service
from Products.CMFPlone.interfaces.controlpanel import ISiteSchema
from Products.CMFPlone.utils import getSiteLogo
from zope.component import adapter
from zope.component import getUtility
from zope.interface import implementer
from zope.interface import Interface

import plone.api


@implementer(IExpandableElement)
@adapter(Interface, ICusyRestapiInfoLayer)
class SiteInfo(object):
    def __init__(self, context, request):
        self.context = context
        self.request = request

    def __call__(self, expand=False):
        result = {
            "siteinfo": {
                "@id": "{}/@siteinfo".format(self.context.absolute_url()),
            }
        }
        if not expand:
            return result

        registry = getUtility(IRegistry)
        site_settings = registry.forInterface(ISiteSchema, prefix="plone", check=False)

        language_tool = plone.api.portal.get_tool(name="portal_languages")
        available_languages = language_tool.getSupportedLanguages()
        default_language = language_tool.getDefaultLanguage()

        result["siteinfo"].update(
            {
                "title": site_settings.site_title,
                "logo_url": getSiteLogo(),
                "multilingual": len(available_languages) > 1,
                "available_languages": available_languages,
                "default_language": default_language,
            }
        )
        return result


class SiteInfoGet(Service):
    def reply(self):
        site_info = SiteInfo(self.context, self.request)
        return site_info(expand=True)["siteinfo"]
