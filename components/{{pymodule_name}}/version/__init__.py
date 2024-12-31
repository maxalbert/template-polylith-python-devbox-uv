# Source: https://github.com/maresb/hatch-vcs-footgun-example/

__all__ = ["__version__"]


# Define the variable '__version__':
try:
    # If setuptools_scm is installed (e.g. in a development environment with
    # an editable install), then use it to determine the version dynamically.
    import setuptools_scm

    # This will fail with LookupError if the package is not installed in
    # editable mode or if Git is not installed.
    __version__ = setuptools_scm.get_version(root="../../..", relative_to=__file__)
except (ImportError, LookupError):  # pragma: no cover
    # As a fallback, use the version that is hard-coded in the file.
    try:
        from {{ pymodule_name }}.version._version import __version__  # noqa: F401
    except ModuleNotFoundError:
        # The user is probably trying to run this without having installed
        # the package, so complain.
        raise RuntimeError(
            "{{ pymodule_name }} is not correctly installed. Could not determine version."
        )
