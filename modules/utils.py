import os
import logging


def setup_logging(output_dir):
    os.makedirs(output_dir, exist_ok=True)

    log_file = os.path.join(output_dir, "noirrecon.log")

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(message)s",
        handlers=[
            logging.FileHandler(log_file),
            logging.StreamHandler()
        ]
    )

    logging.info("Logging started...")
