#!/usr/bin/env python3

import argparse
import os
from rich import print
from rich.panel import Panel

from modules.subdomains import find_subdomains
from modules.alive import check_alive_hosts
from modules.nuclei_scan import run_nuclei_scan
from modules.report import save_report


# ----------------------------
# NoirRecon Banner
# ----------------------------
def banner():
    print(
        Panel.fit(
            "[bold magenta]🖤 NoirRecon — Safe Recon Tool[/bold magenta]\n"
            "[white]Subdomain Enum • Alive Check • Optional Nuclei Scan[/white]\n\n"
            "[yellow]⚠ Only use on domains you own or have permission to test.[/yellow]",
            border_style="magenta",
        )
    )


# ----------------------------
# Main Logic
# ----------------------------
def main():
    banner()

    parser = argparse.ArgumentParser(
        description="NoirRecon — Professional Safe Recon Tool"
    )

    parser.add_argument(
        "-d",
        "--domain",
        required=True,
        help="Target domain (example.com)",
    )

    parser.add_argument(
        "--limit",
        type=int,
        default=200,
        help="Max number of subdomains to process",
    )

    parser.add_argument(
        "--threads",
        type=int,
        default=50,
        help="Threads for httpx probing",
    )

    parser.add_argument(
        "--fast",
        action="store_true",
        help="Fast mode (critical-only nuclei templates)",
    )

    parser.add_argument(
        "--nuclei",
        action="store_true",
        help="Enable nuclei vulnerability scanning (optional)",
    )

    args = parser.parse_args()

    os.makedirs("output", exist_ok=True)

    # ----------------------------
    # Step 1 — Subdomain Enum
    # ----------------------------
    print("\n[bold cyan]Step 1 — Subdomain Enumeration[/bold cyan]")
    subdomains = find_subdomains(args.domain, args.limit)

    if not subdomains:
        print("[red][!] No subdomains found. Exiting.[/red]")
        return

    # ----------------------------
    # Step 2 — Alive Hosts
    # ----------------------------
    print("\n[bold cyan]Step 2 — Alive Hosts Detection[/bold cyan]")
    alive_hosts = check_alive_hosts(subdomains, threads=args.threads)

    if not alive_hosts:
        print("[yellow][!] No alive hosts found.[/yellow]")
        print("[yellow]→ This is normal for many domains.[/yellow]")
        save_report(args.domain, subdomains, [], [])
        return

    print(f"[bold green][+] Alive hosts found: {len(alive_hosts)}[/bold green]")

    # ----------------------------
    # Step 3 — Optional Nuclei
    # ----------------------------
    nuclei_results = []

    if args.nuclei:
        print("\n[bold cyan]Step 3 — Vulnerability Scan (Nuclei)[/bold cyan]")
        nuclei_results = run_nuclei_scan(alive_hosts, fast=args.fast)
    else:
        print(
            "\n[yellow]Step 3 skipped — Nuclei scan disabled.[/yellow]\n"
            "[white]Run with:[/white] [bold]--nuclei[/bold] to enable."
        )

    # ----------------------------
    # Step 4 — Report
    # ----------------------------
    print("\n[bold cyan]Step 4 — Saving Report[/bold cyan]")
    save_report(args.domain, subdomains, alive_hosts, nuclei_results)

    print(
        "\n[bold magenta]🖤 Recon Completed! Check the output/ folder.[/bold magenta]"
    )


# ----------------------------
if __name__ == "__main__":
    main()
