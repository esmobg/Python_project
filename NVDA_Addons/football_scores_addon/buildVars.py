# -*- coding: UTF-8 -*-

import os

# Build customizations
# Change this file instead of sconstruct or manifest files, 
# since these will be overwritten in updated/reinstalled builds.

# Add-on information variables
addon_info = {
    # Add-on Name, internal for nvda
    "addon_name": "footballScores",
    # Add-on summary, usually the user visible name of the addon.
    # Translatable titles/descriptions for user visible strings 
    # should be defined in buildVars.py. This allows the strings
    # to be translated without having to modify the addon source code.
    "addon_summary": "Football Scores Announcer",
    # Add-on description
    # TRANSLATORS: Summary for this add-on 
    # to be shown on installation and add-on information.
    "addon_description": _("""Announces the latest football scores"""),
    # Version
    "addon_version": "1.0",
    # Author(s)
    "addon_author": "EsmoBG <contact@ismailov.website>",
    # URL for the add-on documentation support
    "addon_url": None,
    # Documentation file name
    "addon_docFileName": "docHandler.py",
    # Minimum NVDA version supported (e.g. "2018.3.0", minor version is optional)
    "addon_minimumNVDAVersion": None,
    # Last NVDA version supported/allowed (e.g. "2019.1.0", ideally more recent than minimum version)
    "addon_lastTestedNVDAVersion": None,
    # Add-on update channel (default is None, denoting stable releases,
    # and for independence of add-on updater)
    "addon_updateChannel": None,
}

# Define the python files that are the sources of your add-on.
# You can either use download files (.py), or use MERGED comprehensive compiled (.pyo, .pyc)
pythonSources = [os.path.join("globalPlugins", "football_scores_announcer.py")]

# Add file(s) to be removed on addon uninstall
# IMPORTANT: path must be within the NVDA documentation directory site_scons
# and with forward slashes "/":
addon_uninstallFiles = []