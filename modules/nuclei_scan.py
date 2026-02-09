import subprocess
from rich import print
from rich.progress import Progress, SpinnerColumn, TextColumn


def run_nuclei_scan(alive_hosts, fast=False):
    """
    Runs nuclei vulnerability scan on alive hosts.

    fast=True:
        - only critical templates
        - low request count
        - quicker results
    """

    if not alive_hosts:
        print("[yellow][!] No alive hosts provided for nuclei scan.[/yellow]")
        return []

    print("\n[+] Running nuclei scan...")

    # Save targets temporarily
    targets_file = "output/alive.txt"
    with open(targets_file, "w") as f:
        for host in alive_hosts:
            f.write(host + "\n")

    # Output file
    output_file = "output/nuclei.txt"

    # FAST MODE SETTINGS
    if fast:
        severity = "critical"
        rate_limit = "50"
        timeout = "3"
        templates = "cves/"
        print("[bold magenta]⚡ FAST MODE: Critical CVEs only[/bold magenta]")
    else:
        severity = "high,critical"
        rate_limit = "30"
        timeout = "5"
        templates = None

    # Build nuclei command
    cmd = [
        "nuclei",
        "-l", targets_file,
        "-severity", severity,
        "-rl", rate_limit,
        "-timeout", timeout,
        "-o", output_file,
        "-silent"
    ]

    # Optional template restriction
    if templates:
        cmd += ["-t", templates]

    findings = []

    with Progress(
        SpinnerColumn(),
        TextColumn("[bold red]💀 Scanning vulnerabilities...[/bold red]"),
    ) as progress:

        task = progress.add_task("scan", total=None)

        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True
        )

        progress.stop()

    # Read results
    if result.stdout.strip():
        findings = result.stdout.strip().split("\n")

    # Save findings
    if findings:
        print(f"[bold red][!] Vulnerabilities found: {len(findings)}[/bold red]")
        for fnd in findings[:5]:
            print("   ", fnd)
    else:
        print("[bold green][✔] No vulnerabilities found.[/bold green]")

    return findings
