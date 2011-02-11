"""Event subscribers"""
import logging
from zope.component import adapter
from plone.registry.interfaces import IRecordModifiedEvent
from collective.piwik.core.interfaces import IPiwikSettings
from Products.CMFCore.utils import getToolByName
from zope.component import getUtility
from plone.registry.interfaces import IRegistry
from Products.CMFPlone.utils import safe_unicode

log = logging.getLogger('collective.piwik.core')

PIWIK_CODE = """
<script type="text/javascript">
var pkBaseURL = (("https:" == document.location.protocol) ? "%s" : "%s");
document.write(unescape("%%3Cscript src='" + pkBaseURL + "piwik.js' type='text/javascript'%%3E%%3C/script%%3E"));
</script><script type="text/javascript">
try {
var piwikTracker = Piwik.getTracker(pkBaseURL + "piwik.php", %s);
piwikTracker.trackPageView();
piwikTracker.enableLinkTracking();
} catch( err ) {}
</script><noscript><p><img src="%spiwik.php?idsite=%s" style="border:0" alt="" /></p></noscript>
"""


@adapter(IPiwikSettings, IRecordModifiedEvent)
def updateTrackingCode(obj, event):
    ptool = getToolByName(obj, "portal_properties")
    registry = getUtility(IRegistry)
    settings = registry.forInterface(IPiwikSettings)
    if not settings.piwik_server.endswith('/'):
        settings.piwik_server+='/'
    ptool.site_properties.webstats_js = (PIWIK_CODE % (settings.piwik_server.encode('utf-8').replace('http://','https://'),
                                                       settings.piwik_server.encode('utf-8'),                                                       
                                                       settings.piwik_siteid.encode('utf-8'),
                                                       settings.piwik_server.encode('utf-8'),
                                                       settings.piwik_siteid.encode('utf-8'),                                                       
                                                       )
                                        )
    log.info('webstats_js code updated')
