import subprocess
from rich import print


def check_alive(subdomains, threads):
    """Verifica quais subdomínios estão vivos usando httpx"""

    print("[bold cyan][+] Checking alive hosts with httpx...[/bold cyan]")

    if not subdomains:
        return []

    input_data = "\n".join(subdomains)

    cmd = ["httpx", "-silent", "-threads", str(threads)]

    result = subprocess.run(
        cmd,
        input=input_data,
        capture_output=True,
        text=True
    )

    alive_hosts = result.stdout.splitlines()

    print(f"[bold green][+] Alive hosts: {len(alive_hosts)}[/bold green]")

    return alive_hosts
