# Python Log Analyzer

A Python-based cybersecurity project focused on analyzing log files, identifying suspicious activity, and documenting findings in a SOC-style workflow.

This project is being built as part of my hands-on cybersecurity portfolio to demonstrate practical skills in Python scripting, log analysis, detection logic, documentation, and blue-team fundamentals.

## Project Status

**Status:** In progress

This project is currently being developed as a beginner-friendly but recruiter-facing security tool. The first version will focus on reading sample log files, identifying suspicious patterns, and producing clear findings that could be used in a SOC or IT support environment.

## Project Goals

The goals of this project are to:

* Practice Python scripting for cybersecurity tasks
* Analyze log files for suspicious behavior
* Identify repeated failed login attempts
* Detect unusual IP activity
* Document findings in a clear, professional format
* Build a project that shows practical SOC and IT support readiness

## Skills Demonstrated

* Python scripting
* Log parsing
* Conditional logic
* File handling
* Pattern detection
* Security documentation
* SOC-style analysis
* Technical troubleshooting

## Planned Features

* Read log files from a sample log folder
* Detect repeated failed login attempts
* Count suspicious events by IP address
* Flag basic indicators of suspicious behavior
* Generate a simple findings summary
* Document how the tool works
* Include sample logs for testing

## Planned Project Structure

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

## Example Use Case

A SOC analyst or IT support technician may need to review authentication logs to identify suspicious behavior such as repeated failed login attempts, brute-force activity, or unusual access patterns.

This tool will simulate that workflow by analyzing sample logs and producing a clear summary of potential security concerns.

## Detection Ideas

The first version of this project will focus on simple detection logic, including:

* Multiple failed login attempts from the same IP address
* Suspicious usernames
* Repeated access attempts in a short period
* Basic indicators of brute-force behavior

## Why This Project Matters

Log analysis is a core skill for cybersecurity, SOC, NOC, and IT support roles. This project helps demonstrate the ability to review technical data, identify patterns, explain findings, and document security concerns in a professional way.

## Future Improvements

Future versions may include:

* CSV or JSON output
* More advanced detection rules
* Basic severity ratings
* Command-line arguments
* Automated findings reports
* Additional log types

## Connect With Me

* **LinkedIn:** [linkedin.com/in/cyberotto](https://www.linkedin.com/in/cyberotto)
* **GitHub:** [github.com/CyberSecRYAN](https://github.com/CyberSecRYAN)
* **Email:** [ryanmshaw@proton.me](mailto:ryanmshaw@proton.me)
