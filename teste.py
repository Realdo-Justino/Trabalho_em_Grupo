import time
def Arma_Arco():
        print("\n\n")
        print("Dentre todas as armas, a que mais chama a atenção de Nyssa é uma besta que parece ter sido modificada múltiplas vezes para um resultado")
        print("cada vez mais especifico, ela possui uma cor opaca assemelhando-se a pura escuridão. Ao segura-la o prefeito interrompe.")
        time.sleep(15)
        print("\n")
        print("-Vejo que deseja não fazer barulho? Essa escolha será perfeita então. Essa é uma besta era usada por um grupo de assassinos de aluguel")
        print("que nunca foram vistos. Isso é até que eles vieram atrás de mim, só isso sobrou. Essa besta permite usar flechas tranquilizantes, ")
        print("não saia jogando elas para todo lado, você só tem 15 tentativas")
        time.sleep(17)
        print("\n\n")
        print("Nissa responde:")
        print("-15 hun? Será mais que o suficiente. Entrarei e sairei sem ninguém me ver. E vou ter um brinquedinho novo com 14 flechas")
        time.sleep(13)
        print("\n\n")
        print("O prefeito com um sorriso discreto olha para Nyssa, entrega-lhe um bilhete dizendo:")
        print("-Vai precisar saber onde aqueles vermes estão")
        print("\n")
        texto="1-Aceitar a localização\n2-Negar a localização\n"
        escolha=leiaint(texto)
        if(escolha==1):
                Aceitar_Localizacao()
        else:
                Negar_Localizacao()

def Aceitar_Localizacao():
        print("\n\n")
        print("Nyssa pega o papel, e o lê. Depois ela fala:")
        print("-Cavalheiro de sua parte facilitar meu trabalho não?")
        time.sleep(2)
        print("\n")
        print("-Quero apenas o trabalho feito o mais cedo possível, e assim sei que a chance de você fazer algo errado é menor")
        time.sleep(2)
        print("\n")
        print("-EU NUNCA ERRO!")
        time.sleep(2)
        print("\n")
        print("-Então me mostre, complete essa missão e isso serão início de uma bela amizade")
        time.sleep(2)
        print("\n")
        print("Com raiva, Nyssa chuta a porta e segue o caminho para o culto")
        time.sleep(2)
        print("\n\n")
        print("Ao chegar na localização Nyssa nota algo estranho, que o culto ficava dentro de uma cidade abandonada")
        print("\n")
        print("-Para eles estarem em tal lugar, eles devem ter confiança nas suas defesas, não é fácil proteger uma área tão grande")
        time.sleep(5)
        print("\n\n")
        print("Ao adentrar na cidade, Nyssa nota que uma fábrica parecia muito movimentada para ser uma conhecidencia.")
        print("Ela acredita que este seja o local em que eles guardam as máscaras.")
        time.sleep(3)
        print("\n")
        print("Olhando mais de perto há 2 guardas na porta, e mais 1 rodando a área")
        print("\n")
        texto="1-Se Esqueirar com um Distração\n2-Derrubar os Guardas com a Besta\n"
        escolha=leiaint(texto)
        if(escolha==1):
                Esqueiguar_Distracao()
        else:
                Derrubar_Guardas_Besta()

def Esqueiguar_Distracao():
        print("\n\n")
        print("Nyssa nota que a fábrica fica próxima de uma zona residencial e aproveita a oportunidade")
        print("para quebrar algumas janelas a distância usando pedras.")
        time.sleep(5)
        print("\n")
        print("O guarda de ronda na sua rota acaba notando esses sons")
        time.sleep(3)
        print("\n")
        print("Nyssa pensa:")
        print("-Isso agora vou ter menos um guarda para me preocupar")
        time.sleep(3)
        print("\n")
        print("O guarda acaba vendo que os sons vêm da zona residencial, e imediatamente retorna aos outros guardas.")
        print("Ele cochichaou algo, e depois um sino foi tocado. E com isso não muito tempo depois outros guardas")
        print("em volta de toda cidade se reúnem na fábrica, tornando impossível invadi-la")
        time.sleep(10)
        print("\n")
        print("Nyssa começa a esperar pelo momento em que o alarme seja classificado como falso. Após algumas horas os")
        print("guardas se espalham novamente como se fossem voltar ao seu posto, mas não muito tempo depois Nyssa")
        print("nota que eles estavam na verdade a cercando-a")
        print("\n")
        texto="1-Se Render\n2-Atirar em Todos\n"
        escolha=leiaint(texto)
        if(escolha==1):
                Render_Besta()
        else:
                Atirar_Besta()

def Render_Besta():
       print("\n\n")
       print("Nyssa joga o arco no chão e levanta suas mãos e diz:")
       print("-Eu me rendo não atirem")
       time.sleep(5)
       print("Do meio deles vem alguém que parece ser um dos líderes do culto, sua máscara de respiração era muito diferente")
       print("dos outros, como se fosse pintada com tinta spray. Ele fala:")
       print("-Qual é seu nome e o que quer aqui")
       time.sleep(7)
       print("\n")
       print("-Meu nome é Nyssa, sou uma mercenária, fui contratada pelo prefeito para vir roubar suas máscaras, mas não tenho fidelidade")
       print("ou ligação com aquele porco. Me deixem viva que eu direi onde podem encontrar ele, não ser difícil mata-lo com esse numero")
       time.sleep(7)
       print("\n")
       print("-Não se preocupe herege, já sei das intenções do prefeito mais ele não tem poder para vir nos confrontar, e não me importo quem")
       print("for assumir o poder. Iremos tomar-lo assim só sobra os puros e assim Deus ira absolver nossos erros, e a terra voltara a ser")
       print("como ela era antes. E essa terra não tem lugar para traidoras")
       time.sleep(10)
       print("\n")
       print("-VOCÊS SÃO LOUCOS! TODOS VOCES! E QUE HISTORIA E ESSA DE QUE DEUS VAI ARRUMAR TUDO, VOCES SÓ VÃO CAUSAR A MORTE DE TODOS!")
       time.sleep(5)
       print("\n")
       print("-Não espero que uma herege entenda isso, e nesse momento só posso esperar que se arrependa de seus pecados, mas saiba que isso não irá")
       print("te salvar, VOCÊ IRA QUEIMAR NO INFERNO!")
       time.sleep(3)
       print("\n")
       print("E assim um grupo próximo de Nyssa se aproxima e com uma chuva de balas, quase nada sobra do corpo de Nyssa")
       Game_Over()

def Atirar_Besta():
        print("\n\n")
        print("Nyssa puxa a besta e começa a derrubar um por um, porem o número deles é gigante, e após derrubar no máximo")
        print("3, Nyssa se vê não conseguindo mais se levantar e com isso sua última visão é de uma pessoa alta com uma")
        print("máscara de respiração com um olhar um tanto de dó por ela.")
        Game_Over()

def Derrubar_Guardas_Besta():
        print("tchau")

def Negar_Localizacao():
        print("\n\n")
        print("Nyssa fala com orgulho enquanto sai pela porta")
        print("-Sou uma caçadora nata, não preciso disso, só vou perder a diversão de caça-los")
        time.sleep(13)
        print("\n\n")
        print("Nyssa sai pela noite escura buscando por rastros por horas sem parar, mas quando Nyssa olha para o horizonte")
        print("novamente o sol estava nascendo, e após um tempo ela ouve um barulho não muito longe que parece estar se aproximando,")
        print("ela tenta se esconder porem a luz do dia não a ajuda. Chega um grupo de 5 pessoas, com marcas de lutas e cicatrizes")
        print("pelo seu corpo todo. Eles assim que veem a Nyssa atiram em suas pernas para que ela não pudesse fugir.")
        time.sleep(20)
        print("\n")
        print("Um homem forte com um capacete tribal, que parece ser o líder deles se aproxima e diz")
        print("-Não sei se alguém te falou, mas esse é o nosso território!\n")
        time.sleep(5)
        print("-Eu estou procurando pelo culto das máscaras de oxigênio\n")
        time.sleep(3)
        print("-Vocês ouviram rapazes ela está procurando um tal culto! ")
        print("Ouve-se risadas dos outros membros da gangue\n")
        time.sleep(5)
        print("-Olhe princesinha, nos dois sabemos que deste de que o mundo virou esse caos ninguém mais liga pra religião.")
        print("Mas olha essa arma, que linda não?")
        print("Ele agarra a besta")
        print("\n")
        texto="1-Atirar no Capitão\n2-Deixa-lo pegar a Besta\n"
        escolha=leiaint(texto)
        if(escolha==1):
                Atirar_Capitao()
        else:
                Soltar_Besta()

def Atirar_Capitao():
        print("\n\n")
        print("Com um movimento rápido Nyssa aponta a besta no peito do líder e puxa o gatilho. Mas por algum motivo a flecha não sai")
        time.sleep(3)
        print("\n")
        print("-Parece que a princesinha não sabe nem como a arma funciona não é?")
        print("\n")
        print("O líder puxa uma pistola do bolso e coloca na testa de Nyssa")
        time.sleep(3)
        print("\n")
        print("-Precisa tirar a trava de segurança primeiro")
        print("\n")
        print("E assim ele puxa o gatilho, matando Nyssa no exato momento")
        Game_Over()

def Soltar_Besta():
        print("\n\n")
        print("O líder pega a besta e joga para trás dizendo:")
        print("-Peguem isso vai valer muito no mercado")
        time.sleep(3)
        print("Ele olha novamente para Nyssa e diz")
        print("-Esse será o preço por andar no meu território, você está livre para ir,")
        print("mas com essas pernas duvido que vai ser muito longe")
        time.sleep(3)
        print("\n")
        print("Ele se levanta com um sorriso no rosto e some pelo horizonte. E assim Nyssa nunca mais.")
        print("foi encontrada com vida")
        Game_Over()

def leiaint(texto):
        try:
                try:
                        numero=int(input(texto))
                except ValueError:
                        numero=1
        except UnboundLocalError:
                numero=2
        if(numero>2):
                numero=2
        if(numero<=0):
                numero=1
        return numero

def Game_Over():
        print("\n\n")
        print("GAME OVER")
        time.sleep(3)
        print("\n\n")
        texto="1-Recomeçar\n2-Fim de Jogo\n"
        escolha=leiaint(texto)
        if(escolha==1):
               Arma_Arco()
        else:
               pass

Arma_Arco()