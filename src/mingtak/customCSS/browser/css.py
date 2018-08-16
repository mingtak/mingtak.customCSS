# -*- coding: utf-8 -*-
from mingtak.customCSS import _
from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone import api
from plone.protect.interfaces import IDisableCSRFProtection
from zope.interface import alsoProvides
import logging

logger = logging.getLogger("mustomCSS")


class CustomCSS(BrowserView):
    """ custom.css """

    template = ViewPageTemplateFile("custom_css.pt")


    def __call__(self):
        portal = api.portal.get()
        context = self.context
        request = self.request

        alsoProvides(request, IDisableCSRFProtection)

        filePath = api.portal.get_registry_record('mingtak.customCSS.browser.configlet.ICSSControlPanel.filePath')
        css = request.form.get('css')
        if css:
            with open(filePath, 'w') as file:
                file.write(css)
                api.portal.show_message('Override css file finish.', request=request, type='info')
                request.response.redirect('%s/@@custom_css' % portal.absolute_url())

                return
        else:
            with open(filePath) as file:
                self.css = file.read()
                return self.template()

