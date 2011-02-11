from z3c.form import interfaces

from zope import schema
from zope.interface import Interface

from zope.i18nmessageid import MessageFactory

_ = MessageFactory('collective.piwik.core')


class IPiwikSettings(Interface):
    """Piwik settings."""

    piwik_server = schema.TextLine(title=_(u"Piwik server URL"), 
                                description=u'Where is your piwik located? e.g. http://demo.piwik.org ',
                                required=True,
                                default = u'',
                                )
    
    piwik_siteid = schema.TextLine(title=_(u"Piwik site id"),
                                description=u'integer siteId',
                                required=True,
                                default = u'',
                                )

    piwik_key = schema.TextLine(title=_(u"Piwik API key"),
                                description=u'piwik API token auth key, or anonymous if no auth',
                                required=True,
                                default = u'anonymous',
                                )

