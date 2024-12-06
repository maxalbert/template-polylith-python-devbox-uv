from {{ pymodule_name }}.settings import settings


def test_settings():
    assert settings.logging.level == "DEBUG"
    assert settings.logging.use_colors == True
