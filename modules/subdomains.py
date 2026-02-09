import subprocess
from rich import print
from rich.console import Console
from rich.spinner import Spinner


def find_subdomains(domain, limit):
    console = Console()

    print(f"[+] Running subfinder on {domain}...")

    cmd = ["subfinder", "-d", domain, "-silent"]

    with console.status("🕵️ Enumerating subdomains...", spinner="dots"):
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True
        )

    subs = result.stdout.splitlines()
    subs = subs[:limit]

    print(f"[+] Found {len(subs)} subdomains (limit={limit})")

    with open("output/subdomains.txt", "w") as f:
        for s in subs:
            f.write(s + "\n")

    return subs
