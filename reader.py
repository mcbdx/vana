import pandas as pd 


def csv_reader(csv):
    try:
        df = pd.read_csv(csv)
        return df 
    except Exception as e:
        print(e)



if __name__ == "__main__":
    df = csv_reader("demo.csv")
    print(df.head())
