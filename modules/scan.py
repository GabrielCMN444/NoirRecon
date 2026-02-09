from rich import print
from modules.subdomains import find_subdomains
from modules.alive import check_alive
from modules.nuclei_scan import run_nuclei
from modules.report import generate_report


def run_scan(domain, limit, threads, fast, rate, timeout, no_nuclei):
    print("\n[bold cyan]Step 1 — Subdomain Enumeration[/bold cyan]")

    subdomains = find_subdomains(domain, limit)

    if not subdomains:
        print("[yellow]No subdomains found. Stopping scan.[/yellow]")
        return

    print("\n[bold cyan]Step 2 — Alive Hosts Detection[/bold cyan]")

    alive_hosts = check_alive(subdomains, threads)

    if not alive_hosts:
        print("[yellow]No alive hosts detected. Stopping scan.[/yellow]")
        return

    if no_nuclei:
        print("\n[yellow]Skipping nuclei scan (--no-nuclei)[/yellow]")
        generate_report(domain)
        return

    print("\n[bold cyan]Step 3 — Vulnerability Scanning[/bold cyan]")

    severity = "critical" if fast else "high,critical"

    run_nuclei(alive_hosts, severity, rate, timeout)

    print("\n[bold cyan]Step 4 — Report Generation[/bold cyan]")

    generate_report(domain)

    print("\n[bold green]NoirRecon Finished Successfully 🖤[/bold green]\n")
