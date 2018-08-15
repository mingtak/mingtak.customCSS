# -*- coding: utf-8 -*-
from mingtak.customCSS import _
from plone.app.registry.browser.controlpanel import RegistryEditForm
from plone.app.registry.browser.controlpanel import ControlPanelFormWrapper
from zope import schema
from plone.z3cform import layout
from z3c.form import form
from plone.directives import form as Form


class ICSSControlPanel(Form.Schema):

    filePath = schema.TextLine(
        title=_(u'Fill File Path'),
        required=True,
    )


class CSSControlPanelForm(RegistryEditForm):
    form.extends(RegistryEditForm)
    schema = ICSSControlPanel

CSSControlPanelView = layout.wrap_form(CSSControlPanelForm, ControlPanelFormWrapper)
CSSControlPanelView.label = _(u"Custom CSS")

