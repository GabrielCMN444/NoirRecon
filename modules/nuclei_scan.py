import subprocess


def nuclei_scan(targets, fast=False):
    """
    Runs nuclei vulnerability scan.

    Parameters:
        targets (list): Alive URLs
        fast (bool): If True, runs only critical templates

    Returns:
        list: Findings output
    """

    print("[+] Running nuclei scan...")

    # Save targets into temp file
    targets_file = "output/alive.txt"

    with open(targets_file, "w") as f:
        for t in targets:
            f.write(t + "\n")

    # Fast mode = only critical
    if fast:
        severity = "critical"
        print("[+] Fast mode enabled (critical only)")
    else:
        severity = "high,critical"

    cmd = [
        "nuclei",
        "-l", targets_file,
        "-severity", severity,
        "-silent"
    ]

    try:
        result = subprocess.run(cmd, capture_output=True, text=True)

        output = result.stdout.strip().splitlines()

        if output:
            print(f"[+] Nuclei found {len(output)} issues!")
        else:
            print("[+] No vulnerabilities found.")

        return output

    except Exception as e:
        print("[-] Error running nuclei:", e)
        return []
