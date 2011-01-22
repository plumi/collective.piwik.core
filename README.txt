
Introduction
============

collective.piwik.core is the core package of the collective.piwik tools suite, that provide analytics data using Piwik!

The Piwik open source analytics system (http://piwik.org/) is used to store and retrieve the analytic data.

Works with Plone 4 sites, not tested on Plone 3.

How to get it working
=====================

 - You need to have access to a working Piwik installation. The architecture allows API calls to be sent on the Piwik server, in case authentication is needed to view the site's stats (which is the default case on Piwik). 

To use it, you have to do the following steps:

 - In case it's not already there, add the Piwik Tracking Tag to Javascript web stats support field at <SITEURL>/@@site-controlpanel (we have to use Piwik obviously!)

 - On the eggs section of your buildout.cfg, add collective.piwik.core and run ./bin/buildout -vN buildout.cfg for the product to be installed. collective.piwik.core is a dependency to the other piwik products (collective.piwik.flowplayer, collective.piwik.now, collective.piwik.pageviews) so it will be installed once any of these is installed

 - Log in as admin and go to the Add-ons configuration section (<SITEURL>/prefs_install_products_form) and activate collective.piwik.core. 

 -  Next, go to <SITEURL>/@@piwik-settings and provide the following information:
   -  the Piwik server's url with the slash on the end (example http://piwik.unweb.me/piwik/)
   - the Site id of Piwik (example 12). A piwik installation can track multiple sites, and each one has a unique site id
   - Piwik's API key, which is a token auth key (example 5f298e9c697ec59b68d080cd9be47416), or anonymous if anonymous read access is granted. 

 - After you do the above steps, you can install/activate any of the collective.piwik tools. The core package itself doesn't provide any visible data to the site.

Tweaks
======

You might use collective.piwik.core with any (or all) of the following products: 

collective.piwik.flowplayer (http://pypi.python.org/pypi/collective.piwik.flowplayer) that displays a video play counter in Plone sites that use flowplayer, 

collective.piwik.pageviews (http://pypi.python.org/pypi/collective.piwik.pageviews) that displays unique visits and pageviews, 

and collective.piwik.now (http://pypi.python.org/pypi/collective.piwik.now) that displays a portlet with the number of users currently using your Plone site.

Credits
=======

Created by `unweb.me`_ 

.. _unweb.me: https://unweb.me

Thanks to Engagemedia.org for sponsoring the development


TODO
====



Contributors
~~~~~~~~~~~~

- Markos Gogoulos, mgogoulos at unweb.me
- Dimitris Moraitis, dimo at unweb.me

