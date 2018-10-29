# Restaurant_Selector3_18
def main():
    
    vegeterian=str(input('Is any one in your party a vegetarian? '))
    vegan=str(input('Is anyone in your party a vegan? '))
    gluten_free=str(input('Is anyone in your party gluten_free? '))

    rstrnt1="Joe's Gourmet Burgers"
    # veget=no, vegan=no, glu=no
    rstrnt2="Main Street Pizza Company"
    # veget=yes, vegan=no ,glu=yes
    rstrnt3="Corner Cafe"
    #  veget=yes, vegan=yes, glu=yes
    rstrnt4="Mama's Fine Italian"
    #  veget=yes, vegan=no, glu=no 
    rstrnt5="The Chef's Kitchen"
    #veget=yes, vegan=yes, glu=yes
    
    print('Here are your restaraunt choice: ')


    if vegeterian=='yes' and vegan=='yes' and gluten_free=='yes':
        print(rstrnt3,'\n',rstrnt5)                                      
  
    if vegeterian=='yes' and vegan=='yes' and gluten_free=='no':
        print(rstrnt3,'\n',rstrnt5)                                     
    
    if vegeterian=='yes' and vegan=='no' and gluten_free=='yes':
        print(rstrnt2,'\n',rstrnt3,'\n',rstrnt5)                          
    
    if vegeterian=='no' and vegan=='yes' and gluten_free=='yes':
        print(rstrnt3,'\n',rstrnt3)                                      
  
    if vegeterian=='no' and vegan=='yes' and gluten_free=='no':
        print(rstrnt3,'\n',rstrnt5)                                      
  
    if vegeterian=='no' and vegan=='no' and gluten_free=='yes':
        print(rstrnt2,'\n',rstrnt3,'\n',rstrnt5)                           
  
    if vegeterian=='yes' and vegan=='no' and gluten_free=='no':
        print(rstrnt2,'\n',rstrnt3,'\n',rstrnt4,'\n',rstrnt5)                
  
    if vegeterian=='no' and vegan=='no' and glute_freen=='no':
        print(rstrnt1,'\n',rstrnt2,'\n',rstrnt3,'\n',rstrnt4,'\n',rstrnt5)     

main()
