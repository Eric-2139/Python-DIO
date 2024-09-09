# Polimorfismo: o mesmo nome de função sendo usado com diferentes comportamentos

class Passaro:
    def voar(self):
        print('Voando...')

class Pardal(Passaro):
    def voar(self):
        return super().voar()
    
class Avestruz(Passaro):
    def voar(self):
        print('Avestruz não pode voar')

# FIXME: exemplo ruim para o caso
class Aviao(Passaro):
    def voar(self):
        print('Avião está decolando')

def plano_voo(obj):
    obj.voar()

plano_voo(Pardal())
plano_voo(Avestruz())
plano_voo(Aviao())