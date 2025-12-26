'''
ATOMIC JUSTIFICATION: This file defines a single data class, Metric, responsible for encapsulating raw metric data.
FUNCTION: Represents a single metric value with associated metadata and timestamp.
USAGE: Used to store raw metric data before aggregation within the MetricsUtils library.
'''

from typing import Dict, Optional, Union

class Metric:
    """
    Represents a single metric.

    :param name: The name of the metric.
    :param value: The value of the metric.
    :param timestamp: The timestamp of the metric.
    :param tags: Optional tags associated with the metric.
    :param metadata: Optional metadata associated with the metric.
    """

    def __init__(
        self,
        name: str,
        value: Union[int, float],
        timestamp: float,
        tags: Optional[Dict[str, str]] = None,
        metadata: Optional[Dict[str, str]] = None,
    ):
        self.name = name
        self.value = value
        self.timestamp = timestamp
        self.tags = tags or {}
        self.metadata = metadata or {}
