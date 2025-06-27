import pytest
import pandas as pd
from project import find_best_stats_legendary, find_best_stats_non_legendary, find_most_common_types, find_dual_type


def test_find_best_stats_legendary_less():
    df = pd.DataFrame({'Name': ['test_1', 'test_2', 'test_3', 'test_4', 'test_5', 'test_6'], 
                       'Total': [10, 7, 12, 27, 3, 5]})
    
    result = find_best_stats_legendary(df)
    
    top_10_totals = sorted(df['Total'], reverse=True)[:10]
    expected_values = sorted(top_10_totals)
        
    assert list(result['Total']) == expected_values
    
def test_find_best_stats_legendary_extra():
    df = pd.DataFrame({'Name': [f'test_{i}' for i in range(12)], 
                       'Total': [20, 30, 10, 70, 50, 90, 100, 60, 40, 80, 25, 15]})
    
    result = find_best_stats_legendary(df)
        
    assert list(result['Total']) == [20, 25, 30, 40, 50, 60, 70, 80, 90, 100]
    assert list(result.columns) == ['Name', 'Total']
    assert len(result) == 10
    
def test_find_best_stats_non_legendary():
    df = pd.DataFrame({'Name': ['test_1', 'test_2', 'test_3', 'test_4', 'test_5', 'test_6'], 
                       'Total': [10, 7, 12, 27, 3, 5],
                       'Legendary': [True, False, False, False, False, True]
                       })
    
    
    result = find_best_stats_non_legendary(df)
        
    assert list(result['Total']) == [3, 7, 12, 27]

def test_find_best_stats_non_legendary_extra():
    df = pd.DataFrame({'Name': [f'test_{i}' for i in range(12)], 
                       'Total': [20, 30, 10, 70, 50, 90, 100, 60, 40, 80, 25, 15],
                       'Legendary': [False, False, True, False, False, False, True, True, False, False, False, False]
                       })
    
    result = find_best_stats_non_legendary(df)
        
    assert list(result['Total']) == [15, 20, 25, 30, 40, 50, 70, 80, 90]
    assert list(result.columns) == ['Name', 'Total']
    assert len(result) == 9