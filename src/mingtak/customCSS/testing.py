# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import mingtak.customCSS


class MingtakCustomcssLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        self.loadZCML(package=mingtak.customCSS)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'mingtak.customCSS:default')


MINGTAK_CUSTOMCSS_FIXTURE = MingtakCustomcssLayer()


MINGTAK_CUSTOMCSS_INTEGRATION_TESTING = IntegrationTesting(
    bases=(MINGTAK_CUSTOMCSS_FIXTURE,),
    name='MingtakCustomcssLayer:IntegrationTesting',
)


MINGTAK_CUSTOMCSS_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(MINGTAK_CUSTOMCSS_FIXTURE,),
    name='MingtakCustomcssLayer:FunctionalTesting',
)


MINGTAK_CUSTOMCSS_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        MINGTAK_CUSTOMCSS_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE,
    ),
    name='MingtakCustomcssLayer:AcceptanceTesting',
)
