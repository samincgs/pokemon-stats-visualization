import pytest
import pandas as pd
from project import find_best_stats_legendary, find_best_stats_non_legendary, find_most_common_types, find_dual_type


def test_find_best_stats_legendary_less_than_10():
    df = pd.DataFrame({'Name': ['test_1', 'test_2', 'test_3', 'test_4', 'test_5', 'test_6'], 
                       'Total': [10, 7, 12, 27, 3, 5]})
    
    result = find_best_stats_legendary(df)

    assert list(result['Total']) == [3, 5, 7, 10, 12, 27]
    
def test_find_best_stats_legendary_more_than_10():
    df = pd.DataFrame({'Name': [f'test_{i}' for i in range(12)], 
                       'Total': [20, 30, 10, 70, 50, 90, 100, 60, 40, 80, 25, 15]})
    
    result = find_best_stats_legendary(df)
        
    assert list(result['Total']) == [20, 25, 30, 40, 50, 60, 70, 80, 90, 100]
    
def test_find_best_stats_non_legendary_less_than_10():
    df = pd.DataFrame({'Name': ['test_1', 'test_2', 'test_3', 'test_4', 'test_5', 'test_6'], 
                       'Total': [10, 7, 12, 27, 3, 5],
                       'Legendary': [True, False, False, False, False, True]
                       })
    
    
    result = find_best_stats_non_legendary(df)
        
    assert list(result['Total']) == [3, 7, 12, 27]

def test_find_best_stats_non_legendary_more_than_10():
    df = pd.DataFrame({'Name': [f'test_{i}' for i in range(12)], 
                       'Total': [20, 30, 10, 70, 50, 90, 100, 60, 40, 80, 25, 15],
                       'Legendary': [False, False, True, False, False, False, True, True, False, False, False, False]
                       })
    
    result = find_best_stats_non_legendary(df)
        
    assert list(result['Total']) == [15, 20, 25, 30, 40, 50, 70, 80, 90]

def test_find_most_common_types_less_than_10():
    df = pd.DataFrame({'Type 1': ['Fire', 'Water', 'Fire', 'Poison', 'Dragon', 'Grass', 'Normal', 'Normal', 'Normal'], 
                       'Type 2': [None, 'Ice', 'Normal', 'Bug', None, None, None, 'Flying', 'Flying'],
                       })
    
    result = find_most_common_types(df)
    
    assert result.index[0] == 'Normal'
    assert list(result.values) == [4, 2, 2, 1, 1, 1, 1, 1, 1]

def test_find_most_common_types_more_than_10():
    df = pd.DataFrame({'Type 1': ['Grass', 'Electric', 'Normal', 'Normal', 'Fire', 'Dark', 'Poison', 'Electric', 'Fire', 'Water', 'Water', 'Ice', 'Ghost', 'Normal', 'Normal'], 
                       'Type 2': ['Poison', None, None, 'Flying', None, None, 'Psychic', None, 'Water', 'Fighting', 'Ice', 'Ice', 'Water', 'Normal', 'Normal'],
                       })
    
    result = find_most_common_types(df)
    
    assert result.index[0] == 'Normal'
    assert list(result.values) == [6, 4, 3, 2, 2, 2, 1, 1, 1, 1]
    
def test_find_dual_type_less_than_10():
    df = pd.DataFrame({
        'Name': ['test_1', 'test_2', 'test_3', 'test_4'],
        'Type 1': ['Fire', 'Water', 'Grass', 'Electric'],
        'Type 2': [None, 'Flying', None, 'Steel'],
        'Total': [50, 100, 150, 200]
    })

    result = find_dual_type(df)

    assert pytest.approx(result[True]) == 150
    assert pytest.approx(result[False]) == 100
    
def test_find_dual_type_more_than_10():
    df = pd.DataFrame({
        'Name': [f'test_{i}' for i in range(12)],
        'Type 1': ['Fire', 'Water', 'Grass', 'Electric', 'Psychic', 'Dark', 'Bug', 'Ghost', 'Normal', 'Steel', 'Ice', 'Dragon'],
        'Type 2': [None, 'Flying', None, 'Steel', None, None, 'Flying', 'Dark', None, 'Ghost', 'Water', None],
        'Total': [60, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180]
    })

    result = find_dual_type(df)

    assert pytest.approx(result[True], rel=1e-3) == 130
    assert pytest.approx(result[False], rel=1e-3) == 118.33
    
    