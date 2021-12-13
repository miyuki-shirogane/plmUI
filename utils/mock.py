import string
import random


class Mock:
    def mock_data(self,data_name:str):
        ran_str = '_' + ''.join(random.sample(string.ascii_letters + string.digits, 6))
        res = data_name + ran_str
        return res


if __name__ == "__main__":
    mock = Mock()
    print(mock.mock_data("test"))