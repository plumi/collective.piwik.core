from plone.app.registry.browser.controlpanel import RegistryEditForm
from plone.app.registry.browser.controlpanel import ControlPanelFormWrapper
from collective.piwik.core.interfaces import IPiwikSettings
from plone.z3cform import layout

class PiwikControlPanelForm(RegistryEditForm):
    schema = IPiwikSettings

PiwikControlPanelView = layout.wrap_form(PiwikControlPanelForm, ControlPanelFormWrapper)

