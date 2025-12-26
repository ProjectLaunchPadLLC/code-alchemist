'''
ATOMIC JUSTIFICATION: This file defines a single data class, AggregatedMetric, responsible for encapsulating aggregated metric data.
FUNCTION: Represents the aggregation of metric values with associated metadata.
USAGE: Used to store aggregated metrics calculated from raw metric data within the MetricsUtils library.
'''

from typing import Dict, Optional, Union

class AggregatedMetric:
    """
    Represents an aggregated metric.

    :param name: The name of the metric.
    :param value: The aggregated value of the metric.
    :param tags: Optional tags associated with the metric.
    :param metadata: Optional metadata associated with the metric.
    """

    def __init__(
        self,
        name: str,
        value: Union[int, float],
        tags: Optional[Dict[str, str]] = None,
        metadata: Optional[Dict[str, str]] = None,
    ):
        self.name = name
        self.value = value
        self.tags = tags or {}
        self.metadata = metadata or {}
