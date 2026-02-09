import subprocess
from rich.progress import Progress


def check_alive_hosts(subdomains, threads=50):
    """
    Uses httpx to check which subdomains are alive.
    Returns a list of alive URLs.
    """

    alive = []

    with Progress() as progress:
        task = progress.add_task(
            "🖤 Probing hosts...",
            total=len(subdomains)
        )

        for sub in subdomains:
            url = f"https://{sub}"

            cmd = [
                "httpx",
                "-silent",
                "-timeout", "3",
                "-threads", str(threads),
                "-u", url
            ]

            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True
            )

            if result.stdout.strip():
                alive.append(result.stdout.strip())

            progress.advance(task)

    return alive
