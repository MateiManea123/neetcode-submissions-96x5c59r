class Solution:

    def encode(self, strs: List[str]) -> str:
        sol = ""
        for string in strs:
            sol+=str(len(string))
            sol+="#"
            sol+=string
        print(sol)
        return sol
    def decode(self, s: str) -> List[str]:
        char_nr = ""
        sol=[]
        i=0
        while i < len(s):
            if s[i]=="#":
                print(char_nr)
                sol.append(s[i+1:i+int(char_nr)+1])
                i+=int(char_nr)
                char_nr=""
            else:
                char_nr+=s[i]
            i+=1
        return sol
        

        
