from rich.console import Console
import os
import json

console = Console()

def save_report(domain, subdomains, alive_hosts, results, output_dir="output"):
    """
    Saves the recon report in TXT and JSON formats.
    """

    os.makedirs(output_dir, exist_ok=True)

    txt_file = os.path.join(output_dir, f"{domain}_report.txt")
    json_file = os.path.join(output_dir, f"{domain}_report.json")

    # --- TXT report ---
    with open(txt_file, "w") as f:
        f.write(f"NoirRecon Report for {domain}\n\n")
        f.write("Subdomains Found:\n")
        for sub in subdomains:
            f.write(f"- {sub}\n")

        f.write("\nAlive Hosts:\n")
        for host in alive_hosts:
            f.write(f"- {host}\n")

        f.write("\nVulnerabilities Found:\n")
        for vuln in results:
            f.write(f"- {vuln}\n")

    # --- JSON report ---
    report = {
        "domain": domain,
        "subdomains": subdomains,
        "alive_hosts": alive_hosts,
        "vulnerabilities": results
    }

    with open(json_file, "w") as f:
        json.dump(report, f, indent=4)

    console.print(f"\n[+] Report saved in {txt_file} and {json_file}")
