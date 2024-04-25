import importlib.metadata

# to save yourself having to manually update the module version, you can use importlib to get it from the pyproject.toml!
try:
    __version__ = importlib.metadata.version("psychopy-plugin-template")
except importlib.metadata.PackageNotFoundError:
    # if you're running direct as a local module, you'll get a PackageNotFoundError, so in such instance let's just set the version to "0.dev"
    __version__ = "0.dev"
