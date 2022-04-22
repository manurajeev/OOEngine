from collections import Counter


class Database:
    def insert(self, movies_data_list, movies_kw_data):
        self.MOVIES_DATA = movies_data_list
        self.MOVIES_KW_DATA = movies_kw_data

    def get_data(self, query):

        for operator in ["AND", "OR", "NOT"]:
            if operator in query:
                query1, query2 = query.split(operator)
                res1, res2 = self.__fetch(query1), self.__fetch(query2)
                break

        if "AND" in query:
            res_indices = list(set(res1) & set(res2))
            res_indices.sort(key=Counter(res1 + res2).get, reverse=True)
        elif "OR" in query:
            res_indices = list(set(res1 + res2))
            res_indices.sort(key=Counter(res1 + res2).get, reverse=True)
        elif "NOT" in query:
            res_indices = list(set(res1) - set(res2))
            res_indices.sort(key=Counter(res1).get, reverse=True)
        else:
            temp = self.__fetch(query)
            res_indices = list(set(temp))
            res_indices.sort(key=Counter(temp).get, reverse=True)

        res = []
        for index in res_indices:
            res.append(self.MOVIES_DATA[index])
        return res

    def __fetch(self, query):
        query = query.split()
        res_indices = []

        for word in query:
            if word in self.MOVIES_KW_DATA:
                res_indices += self.MOVIES_KW_DATA[word]

        return res_indices
