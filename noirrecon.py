#!/usr/bin/env python3

import argparse
from rich.console import Console

from modules.subdomains import find_subdomains
from modules.alive import check_alive_hosts
from modules.nuclei_scan import nuclei_scan
from modules.report import save_report

console = Console()


# ==========================
# MAIN FUNCTION
# ==========================
def main():
    parser = argparse.ArgumentParser(
        description="NoirRecon — Professional Recon Tool"
    )

    parser.add_argument(
        "-d", "--domain",
        required=True,
        help="Target domain (example.com)"
    )

    parser.add_argument(
        "--limit",
        type=int,
        default=200,
        help="Max number of subdomains to process (default: 200)"
    )

    parser.add_argument(
        "--threads",
        type=int,
        default=50,
        help="Threads for httpx probing (default: 50)"
    )

    parser.add_argument(
        "--fast",
        action="store_true",
        help="Fast mode (critical nuclei only)"
    )

    args = parser.parse_args()

    console.print("\n🖤 [bold white]NoirRecon Started...[/bold white]\n")

    # ==========================
    # STEP 1 — SUBDOMAIN ENUM
    # ==========================
    console.print("[bold]Step 1 — Subdomain Enumeration[/bold]")
    subdomains = find_subdomains(args.domain, args.limit)

    if not subdomains:
        console.print("[red]No subdomains found. Exiting.[/red]")
        return

    # ==========================
    # STEP 2 — ALIVE CHECK
    # ==========================
    console.print("\n[bold]Step 2 — Alive Hosts Detection[/bold]")
    alive_hosts = check_alive_hosts(subdomains, threads=args.threads)

    if not alive_hosts:
        console.print("[red]No alive hosts found. Exiting.[/red]")
        return

    # ==========================
    # STEP 3 — NUCLEI SCAN
    # ==========================
    console.print("\n[bold]Step 3 — Vulnerability Scanning[/bold]")
    results = nuclei_scan(alive_hosts, fast=args.fast)

    # ==========================
    # STEP 4 — REPORT
    # ==========================
    console.print("\n[bold]Step 4 — Saving Report[/bold]")
    save_report(args.domain, subdomains, alive_hosts, results)

    console.print("\n✅ [bold green]NoirRecon Finished Successfully![/bold green]\n")


# ==========================
# ENTRYPOINT
# ==========================
if __name__ == "__main__":
    main()
