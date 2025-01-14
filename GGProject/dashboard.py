"""
This file was generated with the customdashboard management command, it
contains the two classes for the main dashboard and app index dashboard.
You can customize these classes as you want.

To activate your index dashboard add the following to your settings.py::
    ADMIN_TOOLS_INDEX_DASHBOARD = 'GGProject.dashboard.CustomIndexDashboard'

And to activate the app index dashboard::
    ADMIN_TOOLS_APP_INDEX_DASHBOARD = 'GGProject.dashboard.CustomAppIndexDashboard'
"""

from django.utils.translation import ugettext_lazy as _
try:
    from django.urls import reverse
except ImportError:
    from django.core.urlresolvers import reverse
from django.http import HttpResponse
from workflow.models import Employee
from admin_tools.dashboard import modules, Dashboard, AppIndexDashboard
from admin_tools.utils import get_admin_site_name


class CustomIndexDashboard(Dashboard):
    """
    Custom index dashboard for GGProject.
    """

    def init_with_context(self, context):

        site_name = get_admin_site_name(context)

        # append a link list module for "quick links"
        self.children.append(modules.LinkList(
            _('Quick links'),
            draggable=True,
            deletable=False,
            collapsible=False,
            children=[
                [_('Change password'),
                 reverse('%s:password_change' % site_name)],
                [_('Log out'), reverse('%s:logout' % site_name)],
            ]
        ))
        
        # append an app list module for "Applications"
        self.children.append(modules.AppList(
            _('Applications'),
            exclude=('django.contrib.*',),
        ))

        # append a recent actions module
        self.children.append(modules.RecentActions(_('Recent Actions'), 5))
        
        # append request another link list module for "support".
        self.children.append(modules.LinkList(
            _('Admin Options'),
            children=[
                {
                    'title': _('Update Employee Information'), #add a user from the temporary photo cache / delete photo cache
                    'url': 'tools/ad/',
                    'external': False,
                    'description': 'Add Employee from Photo Cache.'
                },
                {
                    'title': _('Change Authentication Settings'), #do you want two-factor authentication?
                    'url': 'tools/authfactor/',
                    'external': False,
                    'description': 'Get Multi-Factor Authentication Options.'
                },
            ]
        ))



class CustomAppIndexDashboard(AppIndexDashboard):
    """
    Custom app index dashboard for GGProject.
    """

    # we disable title because its redundant with the model list module
    title = ''

    def __init__(self, *args, **kwargs):
        AppIndexDashboard.__init__(self, *args, **kwargs)
        # append a model list module and a recent actions module
        self.children += [
            modules.ModelList(self.app_title, self.models),
            modules.RecentActions(
                _('Recent Actions'),
                include_list=self.get_app_content_types(),
                limit=5
            )
        ]

    def init_with_context(self, context):
        """
        Use this method if you need to access the request context.
        """

        return super(CustomAppIndexDashboard, self).init_with_context(context)
