# Last updated: 06/08/2026 10:54:43
1class Solution(object):
2    def smallestNumber(self, n, t):
3        """
4        :type n: int
5        :type t: int
6        :rtype: int
7        """ 
8        def produit_des_chiffres(num):
9            chaine = str(abs(num))
10            produit = 1
11            for caractere in chaine:
12                produit *= int(caractere)
13            return produit
14
15        
16        i = n
17        while True:
18            if produit_des_chiffres(i) % t == 0:
19                return i
20            i += 1
21            
22           
23    
24            