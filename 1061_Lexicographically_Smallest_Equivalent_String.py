class Solution:
    def group_initial(self, s1: str, s2: str) -> dict:
        grp_0 = list(set([s1[0], s2[0]]))
        grps = {
            "grp_0": grp_0,
        }
        return grps


    def group_rest(self, s1: str, s2: str, grps: dict) -> dict:
        grp_num = 1
        for i in range(1, len(s1)):
            found = False
            for j in range(len(grps)):
                if s1[i] in grps["grp_"+str(j)] or s2[i] in grps["grp_"+str(j)]:
                    grps["grp_"+str(j)].append(s1[i])
                    grps["grp_"+str(j)].append(s2[i])
                    grps["grp_"+str(j)] = list(set(grps["grp_"+str(j)]))
                    found = True
                    break

            if not found:
                grps["grp_"+str(grp_num)] = list(set([s1[i], s2[i]]))
                grp_num += 1
        return grps


    def group_merge(self, grps: dict) -> list:
        for i in range(len(grps)):
            for j in range(i+1, len(grps)):
                if any(x in grps["grp_"+str(i)] for x in grps["grp_"+str(j)]):
                    grps["grp_"+str(i)] += grps["grp_"+str(j)]
                    grps["grp_"+str(i)] = list(set(grps["grp_"+str(i)]))
        return grps


    def group_sort(self, grps: dict) -> None:
        for grp in grps:
            grps[grp].sort()
        return


    def convert_string(self, grps: dict, baseStr: str) -> str:
        result = []
        for char in baseStr:
            found = False
            for i in range(len(grps)):
                if char in grps["grp_"+str(i)]:
                    result.append(grps["grp_"+str(i)][0])
                    found = True
                    break
            if not found:
                result.append(char)
        result = "".join(result)
        return result


    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        grps = self.group_initial(s1, s2)
        grps = self.group_rest(s1, s2, grps)
        grps = self.group_merge(grps)
        self.group_sort(grps)
        result = self.convert_string(grps, baseStr)

        return result


solution = Solution()
print(solution.smallestEquivalentString("akppbligjsmjmagpjorgerfqdoflslfnjqbheiprceafcrjjesigrmdnoois","jfqloksallnorrpoqjrrmkoepkiojgqpqjchadmlfiqbnsdsafabkloiakis","whpqehdlsoqqmnjolqfpcpaboewcmijvoxralwyliggpeyqnjmnzghkfxkou"))