## Simulated Log Source Onboarding (MSSP-style)

This is a minimal Python-based project that simulates onboarding a log source to a central collector

## What It Does

- Simulates a Linux host sending JSON logs over UDP
- Collects and displays the logs in a central listener ("mock SIEM")
- No VMs, WSL, or root access required — just Python

## Files

| File            | Purpose                            |
|-----------------|------------------------------------|
| `log_source.py` | Simulates a log-emitting host      |
| `collector.py`  | Receives logs like a SIEM would    |

## How to Run

1. **Open terminal 1** and run the collector:

python3 collector.py

2. **Open terminal 2** and run the log source:

python3 logsource.py


This is far from ideal as a log source onboarding project but I wanted to try my hand at this.
