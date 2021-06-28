# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from cusy.restapi.info.testing import INTEGRATION_TESTING  # noqa: E501,
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID

import unittest


try:
    from Products.CMFPlone.utils import get_installer
except ImportError:
    get_installer = None


class TestSetup(unittest.TestCase):
    """Test that cusy.restapi.info is properly installed."""

    layer = INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer["portal"]
        if get_installer:
            self.installer = get_installer(self.portal, self.layer["request"])
        else:
            self.installer = api.portal.get_tool("portal_quickinstaller")

    def test_product_installed(self):
        """Test if cusy.restapi.info is installed."""
        self.assertTrue(self.installer.isProductInstalled("cusy.restapi.info"))

    def test_browserlayer(self):
        """Test that ICusyRestapiInfoLayer is registered."""
        from cusy.restapi.info.interfaces import ICusyRestapiInfoLayer
        from plone.browserlayer import utils

        self.assertIn(ICusyRestapiInfoLayer, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer["portal"]
        if get_installer:
            self.installer = get_installer(self.portal, self.layer["request"])
        else:
            self.installer = api.portal.get_tool("portal_quickinstaller")
        roles_before = api.user.get_roles(TEST_USER_ID)
        setRoles(self.portal, TEST_USER_ID, ["Manager"])
        self.installer.uninstallProducts(["cusy.restapi.info"])
        setRoles(self.portal, TEST_USER_ID, roles_before)

    def test_product_uninstalled(self):
        """Test if cusy.restapi.info is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled("cusy.restapi.info"))

    def test_browserlayer_removed(self):
        """Test that ICusyRestapiInfoLayer is removed."""
        from cusy.restapi.info.interfaces import ICusyRestapiInfoLayer
        from plone.browserlayer import utils

        self.assertNotIn(ICusyRestapiInfoLayer, utils.registered_layers())
