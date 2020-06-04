"""
App configuration for edx_get_profile_picture_from_ms.
"""

from __future__ import unicode_literals

from django.apps import AppConfig


class CustomPluginConfig(AppConfig):
    """
    edx_get_profile_picture_from_ms configuration.
    """
    name = 'edx_get_profile_picture_from_ms'
    verbose_name = 'edx_get_profile_picture_from_ms'

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
