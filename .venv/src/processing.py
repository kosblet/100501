from typing import List, Dict
from datetime import datetime

def filter_by_state(operations: List[Dict], state: str = 'EXECUTED') -> List[Dict]:
    """
    Filters the list of operations dictionaries by the given state.

    Args:
        operations (List[Dict]): List of operation dictionaries.
        state (str): The state to filter by. Default is 'EXECUTED'.

    Returns:
        List[Dict]: Filtered list of operation dictionaries.
    """
    return [op for op in operations if op.get('state') == state]

def sort_by_date(operations: List[Dict], descending: bool = True) -> List[Dict]:
    """
    Sorts the list of operations dictionaries by the date.

    Args:
        operations (List[Dict]): List of operation dictionaries.
        descending (bool): Sort order. Default is True (descending).

    Returns:
        List[Dict]: Sorted list of operation dictionaries.
    """
    return sorted(operations, key=lambda x: datetime.fromisoformat(x['date']), reverse=descending)