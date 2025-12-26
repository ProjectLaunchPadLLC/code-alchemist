'''
ATOMIC JUSTIFICATION: This file defines the MetricsAggregator class responsible for aggregating raw Metric objects into AggregatedMetric objects.
FUNCTION: Provides methods for calculating various aggregates (sum, average, etc.) from a stream of Metric objects.
USAGE:  Used to process raw metric data and generate summarized metric reports.  Depends on Metric and AggregatedMetric classes.
'''

from typing import List, Dict
from .Metric import Metric
from .AggregatedMetric import AggregatedMetric

class MetricsAggregator:
    """
    Aggregates metrics.

    :param metrics: A list of Metric objects.
    """

    def __init__(self, metrics: List[Metric]):
        self.metrics = metrics

    def sum(self) -> Dict[str, AggregatedMetric]:
        """
        Calculates the sum of each metric.

        :return: A dictionary of aggregated metrics, where the key is the metric name.
        """

        aggregated_metrics: Dict[str, AggregatedMetric] = {}
        for metric in self.metrics:
            if metric.name not in aggregated_metrics:
                aggregated_metrics[metric.name] = AggregatedMetric(
                    name=metric.name,
                    value=metric.value,
                    tags=metric.tags,
                    metadata=metric.metadata,
                )
            else:
                aggregated_metrics[metric.name].value += metric.value

        return aggregated_metrics

    def average(self) -> Dict[str, AggregatedMetric]:
        """
        Calculates the average of each metric.

        :return: A dictionary of aggregated metrics, where the key is the metric name.
        """

        aggregated_metrics = self.sum()
        for metric_name, aggregated_metric in aggregated_metrics.items():
            count = len([m for m in self.metrics if m.name == metric_name])
            aggregated_metric.value /= count

        return aggregated_metrics
