import numpy as np
import pandas as pd

from Confidence_Intervals.Statistical_functions import get_ecdf, statistical_analysis


def test_statistical_analysis_computes_expected_summary_values():
    metrics = pd.DataFrame({"metric": [0.8, 0.9, 1.0, 0.7]})

    mean, std, sem, width, ci = statistical_analysis(metrics)

    assert mean == 0.85
    assert std == 0.129
    assert sem == 0.064
    assert width == 0.253
    assert ci == [-0.12544, 0.12544]


def test_get_ecdf_returns_sorted_values_and_cumulative_probabilities():
    x, y = get_ecdf(np.array([0.9, 0.7, 1.0, 0.8]))

    np.testing.assert_array_equal(x, np.array([0.7, 0.8, 0.9, 1.0]))
    np.testing.assert_allclose(y, np.array([0.25, 0.5, 0.75, 1.0]))
