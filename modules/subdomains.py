import subprocess
from rich import print


def find_subdomains(domain, limit):
    """Enumera subdomínios usando subfinder"""

    print(f"[bold cyan][+] Running subfinder on {domain}...[/bold cyan]")

    cmd = ["subfinder", "-d", domain, "-silent"]

    result = subprocess.run(cmd, capture_output=True, text=True)

    subs = result.stdout.splitlines()

    if limit:
        subs = subs[:limit]

    print(f"[bold green][+] Found {len(subs)} subdomains[/bold green]")

    return subs
