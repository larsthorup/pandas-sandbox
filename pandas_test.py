from pandas.testing import assert_frame_equal, assert_index_equal, assert_series_equal
import pandas as pd

def test_assert_frame_equal():
    df = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]})
    assert_frame_equal(df, pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]}))

def test_pandas_columns():
    df = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]})
    actual = df.columns
    assert_index_equal(actual, pd.Index(["A", "B"]))

def test_pandas_index():
    df = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]})
    actual = df.index
    assert_index_equal(actual, pd.Index([0, 1, 2]))

def test_pandas_iloc_column():
    df = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]})
    actual = df.iloc[:, 1]
    assert_series_equal(actual, pd.Series([4, 5, 6], name="B"))

def test_pandas_iloc_row():
    df = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]})
    actual = df.iloc[1]
    assert_series_equal(actual, pd.Series({"A": 2, "B": 5}, index=["A", "B"], name=1))

def test_pandas_iloc_cell():
    df = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]})
    actual = df.iloc[1, 1]
    assert actual == 5

def test_pandas_loc_column():
    df = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]})
    actual = df.loc[:, "B"]
    print(type(actual))
    assert_series_equal(actual, pd.Series([4, 5, 6], name="B"))

def test_pandas_loc_row():
    df = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]})
    actual = df.loc[1]
    assert_series_equal(actual, pd.Series({"A": 2, "B": 5}, index=["A", "B"], name=1))

def test_pandas_loc_cell():
    df = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]})
    actual = df.loc[1, "B"]
    assert actual == 5

def test_pandas_merge():
    people_df = pd.DataFrame({"Id": ["Lars", "Jerry"], "Age": [57, 2]})
    cats_df = pd.DataFrame({"Owner": ["Lars", "Lars", "Jerry"], "Cat": ["Ciao", "Mono", "Tom"]})
    actual = pd.merge(people_df, cats_df, left_on="Id", right_on="Owner")
    assert_frame_equal(actual, pd.DataFrame({
        "Id": ["Lars", "Lars", "Jerry"], 
        "Age": [57, 57, 2], 
        "Owner": ["Lars", "Lars", "Jerry"], 
        "Cat": ["Ciao", "Mono", "Tom"],
    }))

def test_pandas_sum():
    df = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]})
    actual = df["A"].sum()
    assert actual == 6
