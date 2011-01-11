from z3c.form import interfaces

from zope import schema
from zope.interface import Interface

from zope.i18nmessageid import MessageFactory

_ = MessageFactory('collective.piwik.core')


class IPiwikSettings(Interface):
    """Global settings. 
    """

    piwik_key = schema.TextLine(title=_(u"Piwik auth token key"),
                                  description=_(u"insert the auth key so that we can communicate with the Piwik server API"),
                                  required=True,
                                  default = u'1771d99931264d538e75eeb19da7d6a0',
                               )


