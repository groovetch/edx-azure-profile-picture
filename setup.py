"""
Setup file for edx_get_profile_picture_from_ms Django plugin.
"""

from __future__ import print_function

import os
import re

from setuptools import setup


def load_requirements(*requirements_paths):
    """
    Load all requirements from the specified requirements files.
    Returns a list of requirement strings.
    """
    requirements = set()
    for path in requirements_paths:
        requirements.update(
            line.split('#')[0].strip() for line in open(path).readlines()
            if is_requirement(line)
        )
    return list(requirements)


def is_requirement(line):
    """
    Return True if the requirement line is a package requirement;
    that is, it is not blank, a comment, or editable.
    """
    # Remove whitespace at the start/end of the line
    line = line.strip()

    # Skip blank lines, comments, and editable installs
    return not (
            line == '' or
            line.startswith('-r') or
            line.startswith('#') or
            line.startswith('-e') or
            line.startswith('git+') or
            line.startswith('-c')
    )


def get_version(*file_paths):
    """
    Extract the version string from the file at the given relative path fragments.
    """
    filename = os.path.join(os.path.dirname(__file__), *file_paths)
    version_file = open(filename).read()
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError('Unable to find version string.')


VERSION = get_version('edx_get_profile_picture_from_ms', '__init__.py')

setup(
    name='edx-get-profile-picture-from-ms',
    version=VERSION,
    description='edx_get_profile_picture_from_ms',
    author='eduNEXT',
    author_email='contact@edunext.co',
    packages=[
        'edx_get_profile_picture_from_ms',
    ],
    include_package_data=True,
    install_requires=load_requirements('requirements/base.in'),
    zip_safe=False,
    entry_points={
        "lms.djangoapp": [
            'edx_get_profile_picture_from_ms = edx_get_profile_picture_from_ms.apps:CustomPluginConfig',
        ],
    },
)
