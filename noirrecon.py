import argparse
from rich import print

from modules.subdomains import find_subdomains
from modules.alive import check_alive
from modules.nuclei_scan import run_nuclei
from modules.utils import create_output_folder, save_list


def main():
    parser = argparse.ArgumentParser(
        description="NoirRecon  — Professional Recon Tool"
    )

    parser.add_argument(
        "-d", "--domain",
        required=True,
        help="Target domain (example.com)"
    )

    parser.add_argument(
        "--limit",
        type=int,
        default=300,
        help="Max number of subdomains to process"
    )

    parser.add_argument(
        "--threads",
        type=int,
        default=50,
        help="Number of threads for httpx"
    )

    args = parser.parse_args()

    domain = args.domain
    limit = args.limit
    threads = args.threads

    print("\n[bold magenta]🖤 NoirRecon Started...[/bold magenta]\n")

    # Create output folder
    create_output_folder()

    # Step 1 — Subdomain Enumeration
    subs = find_subdomains(domain, limit)
    save_list("output/subdomains.txt", subs)

    # Step 2 — Alive Host Check
    alive_hosts = check_alive(subs, threads)
    save_list("output/alive.txt", alive_hosts)

    # Step 3 — Nuclei Vulnerability Scan
    findings = run_nuclei(alive_hosts)
    save_list("output/nuclei.txt", findings)

    # Final Report
    print("\n[bold green]========= FINAL REPORT =========[/bold green]")
    print(f"[+] Subdomains found: {len(subs)}")
    print(f"[+] Alive hosts:      {len(alive_hosts)}")
    print(f"[+] Vulns detected:   {len(findings)}")
    print("[bold cyan]Output saved inside /output folder[/bold cyan]\n")


if __name__ == "__main__":
    main()
