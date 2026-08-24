"""Small reusable helpers for the Day 1 Python-for-AI assignment."""


def normalise(values, minimum=None, maximum=None):
    """Scale a list of numbers into the 0-1 range.

    Args:
        values: list of numbers to scale.
        minimum: value to treat as the lower bound. Defaults to min(values).
        maximum: value to treat as the upper bound. Defaults to max(values).

    Returns:
        A list of floats in [0, 1], same length as `values`. If every value
        is identical (or minimum == maximum), returns 0.0 for every element
        instead of dividing by zero.
    """
    if minimum is None:
        minimum = min(values)
    if maximum is None:
        maximum = max(values)

    span = maximum - minimum
    if span == 0:
        return [0.0 for _ in values]

    return [(v - minimum) / span for v in values]


def summarise_scores(scores):
    """Summarise a list of numeric scores.

    Args:
        scores: list of numbers (e.g. accuracy scores in [0, 1]).

    Returns:
        A dict with keys: count, mean, minimum, maximum, above_threshold
        (count of scores >= 0.8). For an empty list, count and
        above_threshold are 0, and mean/minimum/maximum are None (there is
        no sensible number to report for an empty collection).
    """
    if not scores:
        return {
            "count": 0,
            "mean": None,
            "minimum": None,
            "maximum": None,
            "above_threshold": 0,
        }

    return {
        "count": len(scores),
        "mean": sum(scores) / len(scores),
        "minimum": min(scores),
        "maximum": max(scores),
        "above_threshold": sum(1 for s in scores if s >= 0.8),
    }


def safe_divide(numerator, denominator, default=0.0):
    """Divide two numbers, falling back to a default on bad input.

    Args:
        numerator: the dividend.
        denominator: the divisor.
        default: value to return if the denominator is zero or either
            input is not numeric. Defaults to 0.0.

    Returns:
        numerator / denominator, or `default` if that division is unsafe.
    """
    try:
        return numerator / denominator
    except (ZeroDivisionError, TypeError):
        return default


def train(*args, **kwargs):
    """Stretch example: print whatever positional/keyword args it receives.

    Args:
        *args: any positional arguments.
        **kwargs: any keyword arguments (e.g. learning_rate=0.01).

    Returns:
        None. This function only prints, mirroring the train() demo from
        class where the point is showing how *args/**kwargs collect input.
    """
    print("positional args:", args)
    print("keyword args:", kwargs)
