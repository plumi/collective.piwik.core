from z3c.form import interfaces

from zope import schema
from zope.interface import Interface

from zope.i18nmessageid import MessageFactory

_ = MessageFactory('collective.piwik.core')


class IPiwikSettings(Interface):
    """Piwik settings."""

    piwik_server = schema.TextLine(title=_(u"Piwik server URL"), 
                                description=u'url+piwik location. example http://piwik.unweb.me/piwik/ Please include the slash on the end',
                                required=True,
                                default = u'http://piwik.unweb.me/piwik/',
                                )
    piwik_siteid = schema.TextLine(title=_(u"Piwik Site id"),
                                description=u'site id, example 12',
                                required=True,
                                default = u'12',
                                )

    piwik_key = schema.TextLine(title=_(u"Piwik API key"),
                                description=u'piwik API token auth key, or anonymous if no auth',
                                required=True,
                                default = u'anonymous',
                                )

