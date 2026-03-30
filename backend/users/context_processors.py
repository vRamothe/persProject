import re
import logging

from django.conf import settings

logger = logging.getLogger(__name__)


def _parse_test_report(report_path):
    """Parse test_report.html et retourne les stats (passed, failed, error, total, status)."""
    try:
        content = report_path.read_text(encoding="utf-8")
    except Exception as e:
        logger.warning("Impossible de lire le rapport de tests : %s", e)
        return None

    def _extract(class_name):
        match = re.search(
            rf'<span class="{class_name}">(\d+)\s', content
        )
        return int(match.group(1)) if match else 0

    passed = _extract("passed")
    failed = _extract("failed")
    error = _extract("error")
    total = passed + failed + error

    if failed == 0 and error == 0:
        status = "green"
    elif error > 0 or failed > 3:
        status = "red"
    else:
        status = "orange"

    return {
        "passed": passed,
        "failed": failed,
        "error": error,
        "total": total,
        "status": status,
    }


def test_report_status(request):
    """Context processor : injecte le statut du rapport de tests local pour les admins."""
    if not hasattr(request, "user") or not request.user.is_authenticated:
        return {}
    if not getattr(request.user, "is_admin", False):
        return {}

    report_path = settings.BASE_DIR / "test_report.html"
    if not report_path.exists():
        return {
            "test_report_exists": False,
            "test_report_passed": 0,
            "test_report_failed": 0,
            "test_report_error": 0,
            "test_report_total": 0,
            "test_report_status": "gray",
        }

    stats = _parse_test_report(report_path)
    if stats is None:
        return {
            "test_report_exists": False,
            "test_report_passed": 0,
            "test_report_failed": 0,
            "test_report_error": 0,
            "test_report_total": 0,
            "test_report_status": "gray",
        }

    return {
        "test_report_exists": True,
        "test_report_passed": stats["passed"],
        "test_report_failed": stats["failed"],
        "test_report_error": stats["error"],
        "test_report_total": stats["total"],
        "test_report_status": stats["status"],
    }
