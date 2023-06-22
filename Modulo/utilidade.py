def comparaS(s1,s2):
    # funcao que compara strings
    # letras iguais, maiuscula e minuscula, contam como diferentes 

    t1=len(s1)
    t2=len(s2)

    if (t1!=t2):
        return False

    for i in range(0,len(s1)):      
        if(s1[i]!=s2[i]):
            return False

    return True



#Teste ---- comparaS
''' 
r=comparaS('Pedro','Pedro')
print(r)
'''