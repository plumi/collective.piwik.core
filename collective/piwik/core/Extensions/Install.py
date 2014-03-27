from Products.CMFCore.utils import getToolByName


def install(portal):
    setup_tool = getToolByName(portal, 'portal_setup')
    setup_tool.runAllImportStepsFromProfile(
        'profile-collective.piwik.core:default')
    return "Ran all import steps."


def uninstall(portal):
    setup_tool = getToolByName(portal, 'portal_setup')
    setup_tool.runAllImportStepsFromProfile(
        'profile-collective.piwik.core:uninstall')
    return "Ran all uninstall steps."
