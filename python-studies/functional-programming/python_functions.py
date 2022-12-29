path = r'C:\Users\Vegh\Documents\Estudo\estudos-engenharia-dados\python-studies\pandas\hotels-dataset\hotel_data.csv'

def multiply(n1: int, n2: int) -> int:
    return n1 * n2

def read_csv(path: str, sep: str):
    import pandas as pd
    
    try:
        df = pd.read_csv(path, sep=sep)
        return df
    except Exception as e:
        print(f'Error: {e}')

df = read_csv(path=path, sep=',')
print(df)

res = multiply(1,2)
print(res)
