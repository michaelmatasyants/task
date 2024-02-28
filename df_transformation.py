"""Transforming version_test.csv"""
import pandas as pd


def main():
    """Main function"""
    df = pd.read_csv("version_test.csv", encoding="cp1251")
    df_2 = pd.DataFrame({"x1": ["x1 1"], "new_columns": "ok"})

    df_column_names = {
        name: name.strip()
        for name in df.columns.tolist()
    }
    df = df.drop_duplicates().dropna().iloc[:,  1:]
    df.rename(columns=df_column_names, inplace=True)
    df["Корень"] = df["Корень"].apply(lambda x: x.replace(",", "."))  \
                               .astype("float")
    df = df.groupby(["x1", "x2", "x3",
                     "y1", "y2", "y3",
                     "z1", "z2", "z3", "values"])  \
           .sum().reset_index()

    df = df.merge(df_2, how="left", on=["x1"])

    # Save new csv file in project directory as result.csv
    df.to_csv("result.csv", index=False)

    # Check the df
    print(df)


if __name__ == "__main__":
    main()
