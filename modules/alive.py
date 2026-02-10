import subprocess
from rich.console import Console
from rich.progress import track

console = Console()


def check_alive_hosts(subdomains, threads=50):
    """
    Runs httpx to check which subdomains are alive.
    Returns a list of alive URLs.
    """

    console.print("[+] Checking alive hosts with httpx...\n")

    alive_hosts = []

    # Progress bar
    for sub in track(subdomains, description="🖤 Probing hosts..."):
        try:
            cmd = [
                "httpx",
                "-silent",
                "-threads", str(threads),
                "-u", sub
            ]

            result = subprocess.run(cmd, capture_output=True, text=True)

            if result.stdout.strip():
                alive_hosts.append(result.stdout.strip())

        except Exception:
            continue

    console.print(f"\n[+] Alive hosts found: {len(alive_hosts)}")

    # Save output
    with open("output/alive.txt", "w") as f:
        f.write("\n".join(alive_hosts))

    return alive_hosts
