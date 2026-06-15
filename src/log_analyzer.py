from pathlib import Path
from collections import Counter, defaultdict
import re


FAILED_LOGIN_PATTERN = re.compile(
    r"Failed password for (?:invalid user )?(?P<username>\S+) from (?P<ip>\d{1,3}(?:\.\d{1,3}){3})"
)

ACCEPTED_LOGIN_PATTERN = re.compile(
    r"Accepted password for (?P<username>\S+) from (?P<ip>\d{1,3}(?:\.\d{1,3}){3})"
)


def analyze_log_file(log_file_path):
    """
    Analyze an authentication log file and identify failed login patterns.
    """

    failed_login_counts = Counter()
    accepted_login_counts = Counter()
    usernames_by_ip = defaultdict(set)
    failed_events = []
    accepted_events = []

    with open(log_file_path, "r", encoding="utf-8") as log_file:
        for line in log_file:
            failed_match = FAILED_LOGIN_PATTERN.search(line)
            accepted_match = ACCEPTED_LOGIN_PATTERN.search(line)

            if failed_match:
                username = failed_match.group("username")
                ip_address = failed_match.group("ip")

                failed_login_counts[ip_address] += 1
                usernames_by_ip[ip_address].add(username)
                failed_events.append(line.strip())

            elif accepted_match:
                username = accepted_match.group("username")
                ip_address = accepted_match.group("ip")

                accepted_login_counts[ip_address] += 1
                accepted_events.append(line.strip())

    return failed_login_counts, accepted_login_counts, usernames_by_ip, failed_events, accepted_events


def create_findings_report(
    failed_login_counts,
    accepted_login_counts,
    usernames_by_ip,
    failed_events,
    accepted_events,
    suspicious_threshold=3,
):
    """
    Create a SOC-style findings report based on analyzed log activity.
    """

    suspicious_ips = {
        ip: count
        for ip, count in failed_login_counts.items()
        if count >= suspicious_threshold
    }

    report_lines = [
        "# Python Log Analyzer Findings Summary",
        "",
        "## Executive Summary",
        "",
        "This report summarizes authentication log activity reviewed by the Python Log Analyzer.",
        "The tool identifies failed login attempts, successful logins, and IP addresses that may require further investigation.",
        "",
        "## Log Analysis Results",
        "",
        f"- Total failed login events: {len(failed_events)}",
        f"- Total accepted login events: {len(accepted_events)}",
        f"- Unique IPs with failed logins: {len(failed_login_counts)}",
        f"- Suspicious IPs flagged: {len(suspicious_ips)}",
        "",
        "## Suspicious IP Activity",
        "",
    ]

    if suspicious_ips:
        for ip_address, count in suspicious_ips.items():
            usernames = ", ".join(sorted(usernames_by_ip[ip_address]))
            report_lines.extend(
                [
                    f"### {ip_address}",
                    "",
                    f"- Failed login attempts: {count}",
                    f"- Usernames attempted: {usernames}",
                    "- Finding: This IP address met or exceeded the failed login threshold and should be reviewed.",
                    "",
                ]
            )
    else:
        report_lines.append("No IP addresses met the suspicious activity threshold.")
        report_lines.append("")

    report_lines.extend(
        [
            "## Successful Login Activity",
            "",
        ]
    )

    if accepted_login_counts:
        for ip_address, count in accepted_login_counts.items():
            report_lines.append(f"- {ip_address}: {count} successful login event(s)")
    else:
        report_lines.append("No successful login events were identified.")

    report_lines.extend(
        [
            "",
            "## Analyst Notes",
            "",
            "Repeated failed login attempts may indicate brute-force activity, password guessing, or unauthorized access attempts.",
            "Additional investigation would include reviewing timestamps, validating IP reputation, checking account lockouts, and correlating activity with other security logs.",
            "",
            "## Recommended Next Steps",
            "",
            "- Review suspicious IP addresses for reputation and geolocation",
            "- Confirm whether targeted accounts are valid business users",
            "- Check for related alerts in SIEM or endpoint tools",
            "- Validate MFA and password policy enforcement",
            "- Document findings and escalate if activity appears malicious",
        ]
    )

    return "\n".join(report_lines)


def main():
    base_directory = Path(__file__).resolve().parent.parent
    log_file_path = base_directory / "sample_logs" / "sample_auth.log"
    findings_directory = base_directory / "findings"
    findings_file_path = findings_directory / "findings_summary.md"

    if not log_file_path.exists():
        print(f"Log file not found: {log_file_path}")
        return

    findings_directory.mkdir(exist_ok=True)

    (
        failed_login_counts,
        accepted_login_counts,
        usernames_by_ip,
        failed_events,
        accepted_events,
    ) = analyze_log_file(log_file_path)

    report = create_findings_report(
        failed_login_counts,
        accepted_login_counts,
        usernames_by_ip,
        failed_events,
        accepted_events,
    )

    findings_file_path.write_text(report, encoding="utf-8")

    print(report)
    print()
    print(f"Findings report saved to: {findings_file_path}")


if __name__ == "__main__":
    main()
