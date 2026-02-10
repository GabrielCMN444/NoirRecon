import subprocess
from rich.console import Console

console = Console()


def find_subdomains(domain, limit=200):
    """
    Runs subfinder and returns a list of subdomains.
    """

    console.print(f"[+] Running subfinder on {domain}...")

    try:
        cmd = [
            "subfinder",
            "-d", domain,
            "-silent"
        ]

        result = subprocess.run(cmd, capture_output=True, text=True)

        if result.returncode != 0:
            console.print("[red]Subfinder failed.[/red]")
            console.print(result.stderr)
            return []

        subdomains = result.stdout.splitlines()

        # Apply limit
        subdomains = subdomains[:limit]

        console.print(f"[+] Found {len(subdomains)} subdomains (limit={limit})")

        # Save correctly into output/
        with open("output/subdomains.txt", "w") as f:
            f.write("\n".join(subdomains))

        return subdomains

    except Exception as e:
        console.print(f"[red]Subdomain scan failed: {e}[/red]")
        return []
