import subprocess
from rich import print


def run_nuclei(hosts):
    """Roda nuclei para detectar vulnerabilidades high/critical"""

    if not hosts:
        print("[bold yellow][!] No alive hosts found. Skipping nuclei.[/bold yellow]")
        return []

    print("[bold cyan][+] Running nuclei scan (high/critical)...[/bold cyan]")

    input_data = "\n".join(hosts)

    cmd = [
        "nuclei",
        "-severity", "high,critical",
        "-silent"
    ]

    result = subprocess.run(
        cmd,
        input=input_data,
        capture_output=True,
        text=True
    )

    findings = result.stdout.splitlines()

    print(f"[bold red][+] Vulnerabilities found: {len(findings)}[/bold red]")

    return findings
