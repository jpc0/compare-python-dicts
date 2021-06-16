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
            for j in list2:
                if type(i) == type(j):
                    pass
                else:
                    return False
            if type(i) == dict:
                for k in list2:
                    if DictCompare.dict_in_dict(i, k):
                        break
                else:
                    return False
            elif type(i) == list:
                if i in list[2]:
                    for l in list2:
                        if DictCompare.list_in_list(i, l):
                            break
                    else:
                        return False
                else:
                    pass
        return True

if __name__ == "__main__":
    a = {"a": "", "b":[{"a":""}, {"b":""}]}
    b = {"a": ""}
    c = {"b": [{}]}
    d = {"b": []}
    e = {}
    f = {"b": [{"a":""}, {"b":""}]}
    assert DictCompare.dict_in_dict(b, a)
    assert DictCompare.dict_in_dict(c, a)
    assert DictCompare.dict_in_dict(d, a)
    assert DictCompare.dict_in_dict(e, a)
    assert DictCompare.dict_in_dict(f, a)