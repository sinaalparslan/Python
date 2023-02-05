import pandas


def calculate_average_value(rolling_average_value: int, df: list):
    '''
    values sütunundaki değerleri birer,ikişer,üçer.... şekilde toplayıp ortlamasını alıp yeni sütununda gerekli
    konumunda yazıyor.

    :param rolling_average_value: int value of rolling average value
    :param df: pandas dataFrame
    :return: updated pandas dataFrame
    '''
    b = []
    for i in range(len(df)):

        if i <= rolling_average_value:
            b.append(None)
        else:
            sub_df = df['values'][i - 1 - rolling_average_value: i + 1]
            sum_df = sum(sub_df)
            len_df = len(sub_df)
            res = sum_df / len_df
            b.append(res)

    df[f"avg_{rolling_average_value + 2}"] = b


def rolling_average_value(df: list):
    '''
    yeni oluşturacağımız sütun sayısınca işlemleri döndürmek için
    :param df: pandas dataFrame
    :return:
    '''
    for i in range(100):
        calculate_average_value(i, df)
    write_file(df)


def read_file():
    '''
    csv verisini dataFrame şekline okuyabilmek için
    :return: pandas dataFrame
    '''
    values = pandas.read_csv('data.csv')
    return values


def write_file(df):
    '''
    güncellenmiş pandas dataFrame i csv formatında oluşturmak için
    :param df: pandas dataFrame
    :return: .csv file
    '''
    df.to_csv("result.csv")


def main():
    data = read_file()

    rolling_average_value(data)


main()
