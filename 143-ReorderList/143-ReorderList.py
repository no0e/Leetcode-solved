# Last updated: 04/08/2026 11:37:36
class Solution(object):
    def reorderList(self, head):
        if not head or not head.next:
            return
        
        
        tortue = head
        lievre = head.next 
        
        while lievre and lievre.next:
            tortue = tortue.next
            lievre = lievre.next.next
            
       
        debut_seconde_moitie = tortue.next
        tortue.next = None 

        
        precedent = None
        current = debut_seconde_moitie
        
        while current is not None:
            next_temp = current.next  
            current.next = precedent    
            precedent = current          
            current = next_temp
        
       
        bon_sens = head
        sens_inverse = precedent 
        
        while bon_sens and sens_inverse:
            # Sauvegarder
            tmp1 = bon_sens.next
            tmp2 = sens_inverse.next
            
            # Recâbler
            bon_sens.next = sens_inverse
            sens_inverse.next = tmp1
            
            # Avancer
            bon_sens = tmp1
            sens_inverse = tmp2

         
