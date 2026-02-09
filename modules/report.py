import os
from rich import print


def save_report(domain, subdomains, alive_hosts, nuclei_results):
    """
    Saves a full recon report inside output/report.txt
    """

    os.makedirs("output", exist_ok=True)

    report_path = "output/report.txt"

    with open(report_path, "w") as f:
        f.write("🖤 NoirRecon Report\n")
        f.write("=" * 50 + "\n\n")

        f.write(f"Target Domain: {domain}\n\n")

        # Subdomains
        f.write("[+] Subdomains Found:\n")
        for sub in subdomains:
            f.write(f"  - {sub}\n")

        f.write("\n")

        # Alive Hosts
        f.write("[+] Alive Hosts:\n")
        for host in alive_hosts:
            f.write(f"  - {host}\n")

        f.write("\n")

        # Nuclei Findings
        f.write("[+] Nuclei Findings:\n")
        if nuclei_results:
            for finding in nuclei_results:
                f.write(f"  - {finding}\n")
        else:
            f.write("  No vulnerabilities found.\n")

    print(f"[bold green]✔ Report saved at {report_path}[/bold green]")
