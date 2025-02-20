from typing import List, Dict
from datetime import datetime

def filter_by_state(operations: List[Dict], state: str = 'EXECUTED') -> List[Dict]:
    """
     Фильтрует список операционных словарей по заданному состоянию.

        operations (List[Dict]): Список операционных словарей.
        state (str): Государство, по которому будет отфильтровываться. По умолчанию - EXECUTED.
        List[Dict]: Фильтрованный список операционных словарей.
    """
    return [op for op in operations if op.get('state') == state]

def sort_by_date(operations: List[Dict], descending: bool = True) -> List[Dict]:
    """
    Сортирует список операционных словарей по дате.

        operations (List[Dict]): Список операционных словарей.
        descending (bool): порядок сортировки. По умолчанию - True (descending).

        List[Dict]: Сортированный список операционных словарей.
    """
    return sorted(operations, key=lambda x: datetime.fromisoformat(x['date']), reverse=descending)


