from plone.app.registry.browser import controlpanel

from collective.piwik.core.interfaces import IPiwikSettings, _


class IPiwikSettingsEditForm(controlpanel.RegistryEditForm):

    schema = IPiwikSettings

    def updateFields(self):
        super(IPiwikSettingsEditForm, self).updateFields()

    def updateWidgets(self):
        super(IPiwikSettingsEditForm, self).updateWidgets()

class PiwikSettingsControlPanel(controlpanel.ControlPanelFormWrapper):
    form = IPiwikSettingsEditForm
~                                                              
