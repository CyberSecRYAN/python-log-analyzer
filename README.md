# Python Log Analyzer

A Python-based cybersecurity project focused on analyzing authentication logs, identifying suspicious login activity, and documenting findings in a SOC-style workflow.

This project was built as part of my hands-on cybersecurity portfolio to demonstrate practical skills in Python scripting, log analysis, detection logic, documentation, and blue-team fundamentals.

## Project Status

**Status:** Version 1 complete

Version 1 analyzes a sample authentication log file, identifies repeated failed login attempts, flags suspicious IP addresses, and generates a SOC-style findings summary.

## Project Goals

The goals of this project are to:

* Practice Python scripting for cybersecurity tasks
* Analyze authentication logs for suspicious behavior
* Identify repeated failed login attempts
* Detect unusual IP activity
* Document findings in a clear, professional format
* Build a project that shows practical SOC and IT support readiness

## Skills Demonstrated

* Python scripting
* Log parsing
* Regular expressions
* File handling
* Conditional logic
* Pattern detection
* Security documentation
* SOC-style analysis
* Technical troubleshooting

## Current Features

* Reads a sample authentication log file
* Detects failed login attempts
* Detects successful login activity
* Counts failed login attempts by IP address
* Flags IP addresses that meet or exceed a suspicious activity threshold
* Tracks usernames attempted by suspicious IPs
* Generates a markdown findings report
* Prints analysis results to the terminal

## Repository Structure

```text
python-log-analyzer/
├── README.md
├── src/
│   └── log_analyzer.py
├── sample_logs/
│   └── sample_auth.log
├── findings/
│   └── findings_summary.md
├── .gitignore
└── LICENSE
```

## Files

* `src/log_analyzer.py` contains the Python script used to analyze the log file.
* `sample_logs/sample_auth.log` contains sample authentication log data.
* `findings/findings_summary.md` contains the SOC-style findings report generated from the sample log analysis.

## How to Run

From the root of the repository, run:

```bash
python src/log_analyzer.py
```

The script will analyze the sample authentication log and create or update:

```text
findings/findings_summary.md
```

## Example Use Case

A SOC analyst or IT support technician may need to review authentication logs to identify suspicious behavior such as repeated failed login attempts, brute-force activity, or unusual access patterns.

This tool simulates that workflow by analyzing sample logs and producing a clear summary of potential security concerns.

## Detection Logic

Version 1 focuses on simple detection logic, including:

* Multiple failed login attempts from the same IP address
* Suspicious username attempts
* Repeated authentication failures
* Basic indicators of brute-force behavior

The current suspicious activity threshold is set to **3 or more failed login attempts from the same IP address**.

## Findings Summary

The sample log analysis identified:

* 10 failed login events
* 2 accepted login events
* 3 unique IP addresses with failed logins
* 3 suspicious IP addresses flagged for review

The findings report includes analyst notes and recommended next steps.

## Why This Project Matters

Log analysis is a core skill for cybersecurity, SOC, NOC, and IT support roles. This project demonstrates the ability to review technical data, identify patterns, explain findings, and document security concerns in a professional way.

## Future Improvements

Future versions may include:

* CSV or JSON output
* More advanced detection rules
* Basic severity ratings
* Command-line arguments
* Additional log types
* Timestamp-based analysis
* Automated reporting improvements

## Connect With Me

* **LinkedIn:** [linkedin.com/in/cyberotto](https://www.linkedin.com/in/cyberotto)
* **GitHub:** [github.com/CyberSecRYAN](https://github.com/CyberSecRYAN)
* **Email:** [ryanmshaw@proton.me](mailto:ryanmshaw@proton.me)
