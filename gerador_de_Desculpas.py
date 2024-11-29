import random 
import time


motivos = ["o cachorro comeu o notebook", "tive que esfriar o sol um pouco porque tava calor deamis"
           , "descrobri um bug na matrix e precisei reiniciar o universo",
           "meu vizinho resolveu fazer um churrasco", "meu vizinho resolveu fazer um churrasco e me sequestrou"
           , "o sol estava na posicção errada e desestabilizou o meu foco"]

consequencias = ["passei horas tentando resolver isso", "acabei me distraindo com a situação",
                 "não deu tempo de terminar", " me perdi no caos", "tive que adiar para evitar o pior"]

promessas = ["vou compensar isso amanhã", "semana que vem tudo estará em ordem",
             "prometo que isso nunca mais acontece(talvez)", "vou resolver isso assim que possivel"
             , "vou aprender com essa experiência e melhorar"]
def carregando(texto="Gerando desculpa"):
   for i in range (3):
      print(f"{texto}{'.'*(i+1)}")
      time.sleep(0.5)

def gerar_desculpa ():
    motivo = random.choice(motivos)
    consequencia = random.choice(consequencias)
    promessa = random.choice(promessas)
    return f"eu não consegui porque {motivo}, daí {consequencia}, mas {promessa}. "

if __name__ == "__main__":
    print (" ===Bem-vinda ao Gerador de Desculpas ===")
    print (" Especialmente feito para você! \n")
    input ("pressione ENTER para começar... ")
    carregando()
    desculpa = gerar_desculpa()
    print (desculpa)