from structlog.testing import capture_logs

from {{ pymodule_name }}.logging import structlog_logger


def test_structlog_logger():
    expected_output = [{"answer": 42, "event": "Hello, world!", "log_level": "info"}]

    with capture_logs() as cap_logs:
        structlog_logger.info("Hello, %s!", "world", answer=42)
        assert cap_logs == expected_output


def test_structlog_logger_v2(capsys):
    structlog_logger.info("Hello, %s!", "world", answer=42)
    captured = capsys.readouterr()
    output = captured.out.strip()
    assert output.endswith("[info     ] Hello, world!                  answer=42")
