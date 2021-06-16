class DictCompare:
    @staticmethod
    def dict_in_dict(dict1, dict2):
        """ This fuction ensure that all the keys in dict 1 are present in dict 2
            and are of the same type.

            If the type of any value is a dict, it recursively checks those dicts 
        """
        for i in dict1.keys():
            if i in dict2.keys():
                if type(dict1[i]) == type(dict2[i]):
                    pass
                else:
                    return False
                if type(dict1[i]) == dict:
                    return DictCompare.dict_in_dict(dict1[i], dict2[i])
                elif type(dict1[i]) == list:
                    return DictCompare.list_in_list(dict1[i], dict2[i])
            else:
                return False
        return True

    @staticmethod
    def list_in_list(list1, list2):
        for i in list1:
            if i in list2:
                index = list2.index(i)
                if type(i) == type(list2[index]):
                    pass
                else:
                    return False
                if type(i) == dict:
                    DictCompare.dict_in_dict(i, list2[index])
                elif type(i) == list:
                    DictCompare.list_in_list(i, list2[index])
            else:
                return False