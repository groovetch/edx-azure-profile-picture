"""
App configuration for edx_azure_profile_picture.
"""

from __future__ import unicode_literals

from django.apps import AppConfig


class CustomPluginConfig(AppConfig):
    """
    edx_azure_profile_picture configuration.
    """
    name = 'edx_azure_profile_picture'
    verbose_name = 'edx_azure_profile_picture'

    plugin_app = {
        'settings_config': {
            'lms.djangoapp': {
                'common': {'relative_path': 'settings.common'},
                'test': {'relative_path': 'settings.test'},
                'aws': {'relative_path': 'settings.aws'},
                'production': {'relative_path': 'settings.production'},
                'devstack': {'relative_path': 'settings.devstack_docker'}
            }
        }
    }
