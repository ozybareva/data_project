import pandas


class FileProcess:

    def __init__(self):
        self.file_name = '../razb_uch.xlsx'
        self.data = pandas.read_excel(self.file_name)
        self.data_info = self.data.dtypes

    def create_model(self):
        with open('data_model.py', 'a') as f:
            for col_name, data_type in self.data_info.items():
                f.write(f'    {col_name} = {self.define_type(str(col_name), str(data_type))}\n')
            f.write('\n    class Meta:\n        table = "data_table"\n')

    def define_type(self, col_name: str, df_data_type: str):
        if df_data_type == 'object':
            return f'CharField(max_length={self.data[col_name].map(len).max()})'
        if df_data_type == 'int64':
            return 'IntField()'
        if df_data_type == 'float64':
            return 'FloatField()'
