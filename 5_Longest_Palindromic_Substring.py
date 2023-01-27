class Solution:
    def longestPalindrome(self, s: str) -> str:
        """Returns the longest palindromic substring in s."""
        
        if len(s) == 1:
            return s
        if len(s) == 2:
            return s if s[0] == s[1] else s[0]

        max_length = 0
        max_palindrome = ""

        for i in range(len(s)):
            for j in range(i+1, len(s)):
                sub = s[i:j+1]
                if sub[0:len(sub)//2] == sub[len(sub)-1:(len(sub)//2)-1:-1]:
                    if len(sub) > max_length:
                        max_length = max(max_length, len(sub))
                        max_palindrome = sub
                if sub[0:len(sub)//2+1] == sub[len(sub)-1:(len(sub)//2)-1:-1]:
                    if len(sub) > max_length:
                        max_length = max(max_length, len(sub))
                        max_palindrome = sub

        if max_palindrome:
            return max_palindrome
        else:
            return s[0]

text = "vnjwvalrbypfcbqnmopltjnoifmzwgvpzqzsdtvawndpjtpmpjbjionjifqtvvocpeaftvhpdgjjfafunfndztdjkcxyihtsyppendfzzjeyxlbwpdygiqmdqcdbmgyjigrmfkswcwryaydjilqqxvcnyvviesuncslvzikawwqykqwdfibggezufqihcjkebapmgkvwixywgdextafxycnipjglsndkyjoqfyfljfkkvoieksmavdlmlhhnstesibffiopqvlyuidvrawndbzonwzbsjmpeqoglmdbinkovqpzfkxihzitdopnomseqhmrrkcsvrzziphwpuhjngeotwcrebcmbtirkgeavojtmpakcewmexhxacngknokxsvtqobdgckutpexswgwqzbosjpxauyflnylfcxsucsehqvakbpvfmkelmkspsqxnutwfwacpqqvovdqafeylobneojdsgqowcbxfsvuqusdbylcgcvgrofgvzubakjmlbffjhrafvnqttwuyhokzpmhlludpbowuxzrebxsdusalljfjgjkucwzpmndqncykvfnbrxcrcaxwisjpstejjqbpwegpxyrtyafxklgralnkwxkmjpuqfixzkonznmguyizlancpxdzcfkgiotyelegprbaytdhbutbuihkxnbtuqrtezaskfqsmrznfohhlqp"
print(Solution().longestPalindrome(text))