from typing import Any, Iterable, List

YELLOW = "\033[93m"
GREEN = "\033[92m"
RED = "\033[91m"
BLUE = "\033[94m"
NC = "\033[0m"  # No Color


STORAGE_MODES: List[str] = [
    "task1.1",
    "task1.2",
    "task2.1",
    "task2.2",
    # "raid1",
    # "erasure_coding_rs",
    # "erasure_coding_rlnc",
    # "fake-hdfs",
]


TOPIC_HEARTBEAT = "heartbeat"

PORT_HEARTBEAT = 5555

TOTAL_NUMBER_OF_STORAGE_NODES: int = 4