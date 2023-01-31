import pandas as pd
def read_file(file:str):
    """
    dosyayı okuyup içindeki değerleri elde etme.
    :param file: file name with format ex. data.csv
    :return:
    """
    data_df = pd.read_csv(f'{file}')

    mydt=pd.DataFrame(data_df, columns=(['values']))

    return mydt

def creat_column(values:'pandas.core.frame.DataFrame'):
    for i in range(len(values)):
        values.insert(f'{i+1}values',)


def main():
    file = 'data.csv'
    my_dict = read_file(file)


    creat_column(my_dict)
main()