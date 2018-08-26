# -*- coding: utf-8 -*-
from mingtak.customCSS import _
from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone import api
from plone.protect.interfaces import IDisableCSRFProtection
from zope.interface import alsoProvides
import logging

import os

logger = logging.getLogger("mustomCSS")


class CustomCSS(BrowserView):
    """ custom.css """

    template = ViewPageTemplateFile("custom_css.pt")

    def __call__(self):
        portal = api.portal.get()
        context = self.context
        request = self.request

        alsoProvides(request, IDisableCSRFProtection)

        self.theming = request.form.get('theming')
        if self.theming == 'frontend':
            filePath = api.portal.get_registry_record('mingtak.customCSS.browser.configlet.ICSSControlPanel.filePath')
        elif self.theming == 'backend':
            filePath = api.portal.get_registry_record('mingtak.customCSS.browser.configlet.ICSSControlPanel.backendCSS')
        else:
            return request.response.redirect(portal.absolute_url())

        css = request.form.get('css')
        if css:
            with open(filePath, 'w') as file:
                file.write(css)
                api.portal.show_message('Override css file finish.', request=request, type='info')
                request.response.redirect('%s/@@custom_css?theming=%s' % (portal.absolute_url(), self.theming))
                return
        else:
            os.system('touch %s' % filePath)
            with open(filePath) as file:
                self.css = file.read()
                return self.template()
