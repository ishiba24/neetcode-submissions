class UF:
    def __init__(self, size):
        self.rep = [i for i in range(size)]
        self.size = [1] * size
    def find_representative(self, x):
        if x == self.rep[x]:
            return x
        self.rep[x] = self.find_representative(self.rep[x])
        return self.rep[x]
    def union(self, a, b):
        repA = self.find_representative(a)
        repB = self.find_representative(b)
        if repA == repB:
            return
        if self.size[repA] >= self.size[repB]:
            self.size[repA] += self.size[repB]
            self.rep[repB] = repA
        else:
            self.size[repB] += self.size[repA]
            self.rep[repA] = repB
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        #union find to connect emails to the root, aka the name? 
        n = len(accounts)
        dsu = UF(n)
        emailGroup = {}
        for i, account in enumerate(accounts):
            for email in account[1:]:
                if email not in emailGroup:
                    emailGroup[email] = i
                else:
                    dsu.union(i, emailGroup[email])
        components = {}
        for email, group in emailGroup.items():
            root = dsu.find_representative(group)
            components.setdefault(root, []).append(email)
        mergedAccounts = []
        for root, emails in components.items():
            name = accounts[root][0]
            mergedAccounts.append([name] + sorted(emails))
        return mergedAccounts