# Herança múltipla: quando uma classe-filha herda de várias classes-pai

class Animal:
    def __init__(self, nmr_patas):
        self.nmr_patas = nmr_patas

    def __str__(self):
        return f'{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}'

class Mamifero(Animal):
    def __init__(self, cor_pelo, **kw):
        super().__init__(**kw)
        self.cor_pelo = cor_pelo
       
class Ave(Animal):
     def __init__(self, cor_bico, **kw):
        super().__init__(**kw)
        self.cor_bico = cor_bico
        
class Cachorro(Mamifero):
    pass

class Gato(Mamifero):
    pass

class Leao(Mamifero):
    pass

class Ornitorrinco(Mamifero, Ave):
    def __init__(self, cor_pelo, cor_bico, nmr_patas):
        print(Ornitorrinco.__mro__) # ou mro()

        super().__init__(cor_pelo=cor_pelo, cor_bico=cor_bico, nmr_patas=nmr_patas)

leao = Leao(nmr_patas=4, cor_pelo='marrom-avermelhado')
print(leao)

ornitorrinco = Ornitorrinco(nmr_patas=4, cor_pelo='marrom-esverdiado', cor_bico='laranja')
print(ornitorrinco)