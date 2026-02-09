from datetime import datetime


def generate_report(domain, subdomains, alive):
    """
    Generates a Markdown report.
    """

    now = datetime.now().strftime("%Y-%m-%d %H:%M")

    report = f"""# ShadowRecon Report 🦇

Target: **{domain}**  
Date: {now}

---

## Subdomains Found ({len(subdomains)})

"""

    for s in subdomains:
        report += f"- {s}\n"

    report += f"""

---

## Alive Hosts ({len(alive)})

"""

    for h in alive:
        report += f"- {h}\n"

    with open("output/report.md", "w") as f:
        f.write(report)
