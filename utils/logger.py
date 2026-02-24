import logging
import os


def get_logger():
    os.makedirs("reports", exist_ok=True)

    logging.basicConfig(
        filename="reports/test.log",
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )

    return logging.getLogger()