import pandas as pd


class SimulateID:
    """SimulateID.assign_sim_id assigns for each non-missing 'col'
    a new unique integer.


    Debug:
    # -%%
    start = 1
    col = 'A_ID'
    mapping = (
        full
        [col]
        .drop_duplicates()
        .dropna()
        .sort_values()
        .to_frame()
        .assign(**{f"{col}_SIM": lambda x: range(start, start + len(x))}))
    mapping

    # -%%
    full[col].to_frame().merge(mapping, how='left', on=col)
    """

    def __init__(self, df: pd.DataFrame):
        self.df = df

    def get_mapping(
        self, col: str, start: int = 1
    ) -> pd.DataFrame:  # index = subset of self.df, columns = [col, f"{col}_SIM"]
        mapping = (
            self.df[col]
            .drop_duplicates()
            .dropna()  # if there is no A_ID or C_ID there should be no mapping
            .sort_values()
            .to_frame()
            .assign(**{f"{col}_SIM": lambda x: range(start, start + len(x))})
        )
        return mapping

    def assign_sim_id(self, col: str, start: int = 1) -> pd.Series:
        self.df = self.df.copy()
        mapping = self.get_mapping(col, start)
        shape = self.df.shape
        self.df = self.df.reset_index().merge(
            mapping, how="left", on=col
        )  # I have to do a merge here
        assert self.df.shape[0] == shape[0]
        self.df = self.df.set_index("index")
        # self.df = self.df.join(mapping[f"{col}_SIM"])
        return self


def analyze_sim_kpi(df: pd.DataFrame, col: str, round_: int = 1, sample_n: int = 10000):
    col_sim = f"{col}_SIM"
    assert col_sim in df.columns
    abs_diff = df[col] - df[col_sim]
    abs_diff.name = "abs_diff"
    rel_diff = (abs_diff / df[col]) * 100
    rel_diff.name = "rel_diff"
    df = df.assign(abs_diff=abs_diff, rel_diff=rel_diff)
    ls = []
    for k in [col, col_sim, "abs_diff", "rel_diff"]:
        ls.append(df[k].describe().round(round_))
    out = pd.concat(ls, axis=1)
    df.sample(sample_n).plot.scatter(col, col_sim)
    return out
