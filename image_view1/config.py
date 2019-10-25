"""
Configure the tool
"""

from pathlib import Path


# Paths
data_path = Path("~/python/open_cv/data/").expanduser()
trash_path = Path("~/python/open_cv/data/trash/").expanduser()

# UI click styles
error_style = dict(fg="red", bold=True)
warning_style = dict(fg="yellow", bold=True)
info_style = dict(fg="green", bold=False)