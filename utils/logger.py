import os
import logging
from datetime import datetime

log_dir = "logs"
os.makedirs(log_dir, exist_ok=True)

today = datetime.now().strftime("%Y-%m-%d")
log_filename = os.path.join(log_dir, f"app_{today}.log")

logging.basicConfig(
    filename=log_filename,
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)