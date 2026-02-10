#!/usr/bin/env python3

import argparse
import os

from modules.subdomains import find_subdomains
from modules.alive import check_alive_hosts
from modules.nuclei_scan import nuclei_scan
from modules.report import save_report


def banner():
    print("\n🖤 NoirRecon Started...\n")


def main():
    banner()

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
        help="Max number of subdomains to process"
    )

    parser.add_argument(
        "--threads",
        type=int,
        default=50,
        help="Number of threads for httpx"
    )

    parser.add_argument(
        "--fast",
        action="store_true",
        help="Fast mode (only critical nuclei templates)"
    )

    args = parser.parse_args()

    output_dir = "output"
    os.makedirs(output_dir, exist_ok=True)

    # -----------------------------
    # Step 1 — Subdomain Enumeration
    # -----------------------------
    print("\nStep 1 — Subdomain Enumeration")
    subdomains = find_subdomains(args.domain, args.limit)

    if not subdomains:
        print("[-] No subdomains found.")
        return

    # -----------------------------
    # Step 2 — Alive Hosts Detection
    # -----------------------------
    print("\nStep 2 — Alive Hosts Detection")
    alive_hosts = check_alive_hosts(subdomains, args.threads)

    if not alive_hosts:
        print("[-] No alive hosts found.")
        return

    # -----------------------------
    # Step 3 — Vulnerability Scanning
    # -----------------------------
    print("\nStep 3 — Vulnerability Scanning")
    nuclei_results = nuclei_scan(alive_hosts, fast=args.fast)

    # -----------------------------
    # Step 4 — Report Generation
    # -----------------------------
    print("\nStep 4 — Saving Report")
    save_report(args.domain, subdomains, alive_hosts, nuclei_results)

    print("\n✅ NoirRecon Finished Successfully!\n")


if __name__ == "__main__":
    main()
