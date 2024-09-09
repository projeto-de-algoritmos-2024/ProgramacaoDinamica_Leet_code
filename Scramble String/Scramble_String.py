class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        if len(s1) != len(s2):
            return False

        if s1 == s2:
            return True

        if sorted(s1) != sorted(s2):
            return False

        n = len(s1)

        def verifica_substrings(i1, i2, tamanho):
            if s1[i1:i1 + tamanho] == s2[i2:i2 + tamanho]:
                return True

            for k in range(1, tamanho):
                if (verifica_substrings(i1, i2, k) and verifica_substrings(i1 + k, i2 + k, tamanho - k)):
                    return True
                if (verifica_substrings(i1, i2 + tamanho - k, k) and verifica_substrings(i1 + k, i2, tamanho - k)):
                    return True

            return False

        return verifica_substrings(0, 0, n)
