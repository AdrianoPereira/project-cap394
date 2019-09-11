from functions import load_dataset


if __name__ == "__main__":
    PATH = '../../data/full/exp'

    df = load_dataset(PATH)

    print(df)