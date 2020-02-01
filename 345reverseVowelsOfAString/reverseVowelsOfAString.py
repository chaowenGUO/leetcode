class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = [group[0] for group in re.finditer('[aeiou]', s, re.I)]
        return re.sub('[aeiou]', lambda group: vowels.pop(), s, 0, re.I)
