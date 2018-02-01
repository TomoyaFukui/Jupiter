# coding: utf-8
import xml.etree.ElementTree as ET
import pandas as pd
import numpy as np

class ReadXML():
    '''
    Geniusで作成された効用ドメインファイルを読み込む
    '''
    def __init__(self):
        self.__all_records = []
        self.__size = 0

    #tag_name属性の子要素までをdictionaryで追加する
    #{tag_name + index:{child's neme + index :value_name}}
    def __set_dictionary(self, parent, tag_name, value_name):
        for nodes in list(parent):
            if nodes.tag == tag_name:
                records_value_name = {}
                records_value = {}
                for node in list(nodes):
                    records_value_name[node.get("index")] = node.get(value_name)
                    records_value[node.get("index")] = node.get('value')
                self.__all_records.append({"index":nodes.get("index"),
                                            tag_name:records_value_name,
                                            "name":nodes.get("name"),
                                            nodes.get("name"):records_value})
            else:
                self.__set_dictionary(nodes, tag_name, value_name)

    #tag_name属性の要素をdictionaryで追加する
    #{tag_name + index:value}
    def __set_element(self, parent, tag_name):
        for nodes in list(parent):
            #tag_names = nodes.findall(tag_name)
            if(nodes.tag == tag_name):
                #self.all_records.append(nodes.get("value"))
                if nodes.get("index") is None:
                    self.__all_records.append({tag_name:nodes.get("value")})
                else:
                    self.__all_records.append({"index":nodes.get("index"), tag_name:nodes.get("value")})
            # 処理の軽量化のためのif
            if nodes.tag != 'issue':
                self.__set_element(nodes, tag_name)

    def __count_size(self, parent, tag_name):
        for nodes in list(parent):
            if nodes.tag == tag_name:
                self.size += 1
            else:
                self.__count_size(nodes, tag_name)

    def __set_size(self, parent, tag_name):
        self.size = 0
        self.__count_size(parent, tag_name)
        self.__all_records.append(self.size)

    #未実装
    #weightやissueをindexの順番でソートする
    def __sort(self):
        weight_index_list = [0] * self.__all_records[2]
        for i in range(self.__all_records[2]):
            weight_index_list[i] = (int)(self.__all_records[i+3]["index"])
        sort_range = self.__all_records[2]
        #print(sorted(self._all_records[3, sort_range],key=lambda x: (x["index"])))
        print(sorted(self.__all_records[3, sort_range+2],key=lambda x: int(x["index"])))
        #print(weight_index_list)
        #for in self.all_records:


    def create_utility(self, file_name):
        '''
        効用ドメインファイルを読み込んで，内容をリストで返す

        :param str file_name: 読み込みたいファイルのパス
        :rtype: List
        :return: 読み込んだ情報のリスト
        '''
        self.__all_records = []
        try:
            tree = ET.parse(file_name)
        except:
            print('cannnot serch for ', file_name)
            return
        root = tree.getroot()
        self.__set_element(root, 'discount_factor')
        if len(self.__all_records) == 0:
            self.__all_records.append({"discount_factor": 1})
        # print(len(self.__all_records))
        self.__set_element(root, 'reservation')
        if len(self.__all_records) == 1:
            self.__all_records.append({"reservation": 0})
        self.__set_size(root, 'issue')
        self.__set_element(root, 'weight')
        self.__set_dictionary(root, 'issue', 'evaluation')
        #print(self.__all_records)
        #self._sort()
        #return pd.DataFrame(read_domain.all_records)
        return self.__all_records

    def __print_all_records(self):
        print(self.__all_records)

# if __name__ == '__main__':
#     read_domain = ReadXML()
#     #read_domain.create_utility('Domain2/Domain2_util1.xml')
#     read_domain.create_utility('Jobs/Jobs_util1.xml')
#     read_domain.__print_all_records()
