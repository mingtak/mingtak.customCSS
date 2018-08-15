# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from mingtak.customCSS.testing import MINGTAK_CUSTOMCSS_INTEGRATION_TESTING  # noqa

import unittest


class TestSetup(unittest.TestCase):
    """Test that mingtak.customCSS is properly installed."""

    layer = MINGTAK_CUSTOMCSS_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if mingtak.customCSS is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'mingtak.customCSS'))

    def test_browserlayer(self):
        """Test that IMingtakCustomcssLayer is registered."""
        from mingtak.customCSS.interfaces import (
            IMingtakCustomcssLayer)
        from plone.browserlayer import utils
        self.assertIn(
            IMingtakCustomcssLayer,
            utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = MINGTAK_CUSTOMCSS_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        roles_before = api.user.get_roles(TEST_USER_ID)
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.installer.uninstallProducts(['mingtak.customCSS'])
        setRoles(self.portal, TEST_USER_ID, roles_before)

    def test_product_uninstalled(self):
        """Test if mingtak.customCSS is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'mingtak.customCSS'))

    def test_browserlayer_removed(self):
        """Test that IMingtakCustomcssLayer is removed."""
        from mingtak.customCSS.interfaces import \
            IMingtakCustomcssLayer
        from plone.browserlayer import utils
        self.assertNotIn(
            IMingtakCustomcssLayer,
            utils.registered_layers())
