class Analyser:
    def get_group(self, id):
        group = 0
        while (id != 0):
            group += id % 10
            id //= 10
        return group

    def get_group_amount_of_members(self, n_customers, n_first_id=0):
        result = {}
        n_last_id = n_first_id + n_customers
        for id in range(n_first_id, n_last_id):
            group = str(self.get_group(id))
            if group in result:
                result[group] += 1
            else:
                result[group] = 1
        return result
