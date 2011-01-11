from z3c.form import interfaces

from zope import schema
from zope.interface import Interface

from zope.i18nmessageid import MessageFactory

_ = MessageFactory('collective.piwik.core')


class IPiwikSettings(Interface):
    """Piwik settings."""

    piwik_key = schema.TextLine(title=_(u"Piwik API key"),
                                required=True,
                                default = u'',
                                )

