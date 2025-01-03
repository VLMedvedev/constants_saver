from configs.constants_saver import ConstansReaderWriter


const_dict = {'TEST_VAR_INT': 5,
                  'TEST_VAR_LIST': [1, 6, 3],
                  'TEST_VAR_STR': 'test_sss',
                  'TEST_VAR_BOOL': False,
                  'TEST_VAR_DICT': {'var1': 222, 'var2': 'str_test_11', 'var3': [12, 34, 44, 33]}
                  }
crw = ConstansReaderWriter("test_config")
crw.set_constants_from_config_dict(const_dict)

