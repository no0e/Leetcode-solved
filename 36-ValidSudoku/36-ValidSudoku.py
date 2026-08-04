# Last updated: 04/08/2026 11:38:01
class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        #ligne
        for i in range(9):
            ligne = [x for x in board[i] if x != '.']
            if len(ligne) != len(set(ligne)):#ligne
                return False
            colonne = [ligne[i] for ligne in board if ligne[i] != '.'] #colonnes
            if len(colonne) != len(set(colonne)):
                return False
        #carré
        for k in [0,3,6]:
            for h in [0,3,6]:
                carre = []
                for x in range(3):        
                    for y in range(3):
                        val = board[x+k][y+h]
                        if val != '.':
                            carre.append(board[x+k][y+h])
                if len(carre) != len(set(carre)):
                    return False
        
        return True

    
 