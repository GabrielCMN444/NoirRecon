import subprocess
from rich import print


def scan_ports(hosts):
    """
    Runs nmap fast scan on alive hosts.
    """

    print("[cyan][+] Running Nmap scan...[/cyan]")

    with open("output/nmap_results.txt", "w") as f:
        for host in hosts:
            print(f"[yellow]Scanning {host}[/yellow]")

            result = subprocess.run(
                f"nmap -F {host}",
                shell=True,
                capture_output=True,
                text=True
            )

            f.write(result.stdout + "\n")

    print("[green][+] Nmap results saved in output/nmap_results.txt[/green]")
