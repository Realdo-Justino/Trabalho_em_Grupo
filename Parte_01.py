import time
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

def leiaint2(texto):
        try:
                try:
                        numero=int(input(texto))
                except ValueError:
                        numero=1
        except UnboundLocalError:
                numero=2
        if(numero>3):
                numero=3
        if(numero<=0):
                numero=1
        return numero

print("\n")


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
        print("\n\n")
        print("Nyssa puxa a besta e começa a mirrar nos guardas, e com 3 tiros consecutivos")
        print("certeiros os guardas caem no chão desacordados.")
        time.sleep(3)
        print("\n")
        print("Nyssa aproveitando a oportunidade entra na fabrica")
        time.sleep(2)
        print("\n")
        print("Ao entra Nyssa nota que há muitos guardas rodando o interior constantemente, e")
        print("parece que eles estão mais focados em uma porta no fundo da sala, que parece bem reforçada")
        print("\n")
        texto="1-Derrubar um guarda e se Disfarçar\n2-Correr para Porta\n"
        escolha=leiaint(texto)
        if(escolha==1):
                Derrubar_Disfarcar()
        else:
                Correr_Porta()

def Derrubar_Disfarcar():
        print("\n\n")
        print("Nyssa se esconde num canto escuro esperando pelo momento perfeito, após alguns minutos a")
        print("oportunidade aparece e Nyssa o perfura com uma fecha da besta, ele desmaiou na mesma hora")
        print("sem quaisquer barulhos. Nyssa aproveita e esconde o corpo atrás de umas caixas próximas e")
        print("coloca a roupa do guarda e sua máscara.")
        time.sleep(10)
        print("\n")
        print("Nyssa torna sua atenção para porta e se dirige a ela, ao chegar lá alguns guardas a param e dizem:")
        print("-Alto, o que procuras a aqui irmã?")
        time.sleep(3)
        print("\n")
        print("-Ninguém pode entrar na sala do tesouro sagrado")
        time.sleep(2)
        print("\n")
        print("-Nosso querido líder comandou-me entrar para fazer a contagem e análise, ele teme que alguém tenha")
        print("desobedecido suas ordens e possa ter danificado ou ainda roubado parte do tesouro sagrado")
        time.sleep(2)
        print("\n")
        print("-Nos perdoe irmã, por favor prossiga, mas antes entregue a chave para que possamos abrir")
        time.sleep(2)
        print("\n")
        print("-Me perdoe, mas não foi me dado nenhuma chave, acredito que ele possa ter esquecido de me dar")
        time.sleep(2)
        print("\n")
        print("-Espera, você não possui a chave?")
        time.sleep(2)
        print("\n")
        print("-Não isso não seria um problema não é verdade, você poderia abrir sem ela não?")
        time.sleep(2)
        print("\n")
        print("Ambos os guardas apontam suas armas para Nyssa")
        print("-Se você possui uma chave do paraíso, não é uma de nós!")
        time.sleep(4)
        print("\n")
        print("E ambos os guardas abrem fogo, matando Nyssa")
        Game_Over()

def Correr_Porta():
        print("\n\n")
        print("-É a agora ou nunca não?")
        print("\n")
        print("Nyssa puxa a besta e começa a correr pela porta.")
        time.sleep(3)
        print("\n")
        print("A surpresa permite com que ela evite com que muitos acertem na, ao se aproximar da porta")
        print("ela nota que não será tão sortuda com eles. Ela pega acerta 2 tiros em movimento nos guardas")
        print("e abre a porta o mais rápido possível. ")
        time.sleep(5)
        print("\n")
        print("Ao tornar sua atenção para sala, ela nota que não há nenhuma mascara a vista, mas sim um monte")
        print("de veículos, gasolina e agua. Nyssa nota que ela agora tem que fazer uma decisão difícil.")
        print("\n")
        texto="1-Procurar uma Maneira de Voltar e achar as Mascaras\n2-Pegar tudo que Poder e Fugir\n"
        escolha=leiaint(texto)
        if(escolha==1):
                Final_Neutro()
        else:
                Voltar_Procurar()

def Final_Neutro():
        print("\n\n")
        print("Nyssa pensa nas consequências e as aceitas ela pega um carro, enche ele de suprimentos pega")
        print("o carro e vai de frente para a parede mais fina que uma vez já foi uma porta de garagem")
        time.sleep(3)
        print("\n")
        print("Ela sai correndo a toda velocidade para fora da cidade, atropelando alguns fieis ao longo do caminho")
        time.sleep(2)
        print("\n")
        print("Saindo da cidade ela tem uma conversa consigo")
        print("-Eu ferrei com tudo! Não posso voltar para casa por que aquele porco maldito sabe onde moro, e não")
        print("posso ficar na região próxima daqui. Aquele culto é grande demais para eles planejarem algo pequeno.")
        print(" Eles são uma bomba relógio e eu não vou estar aqui para ver. Com toda essa gasolina e suprimentos que")
        print("eu peguei eu vou pra muito longe, vou trocar meu nome e ter outra vida. Quem sabe essa possa ser um pouco")
        print("melhor que essa última, e tomara que eu possa achar algumas drogas, o resto do meu estoque está em casa e")
        print("eu não sei quanto tempo eu duro sem elas.")
        time.sleep(10)
        print("\n")
        print("E assim Nyssa a mercenária desapareceu do mundo")
        time.sleep(2)
        print("\n\n")
        print("Fim de Jogo")
        print("\n")
        print("FINAL NEUTRO")

def Voltar_Procurar():
        print("\n\n")
        print("Nyssa começa a procurar por qualquer saída que leve para fora dessa sala para procurar as máscaras,")
        print(" ela acaba achando um duto de ventilação abandonado. Ela decide adentrar e esperar a poeira baixar")
        print(" para voltar a busca.")
        time.sleeo(5)
        print("\n")
        print("Os guardas após um tempo conseguem invadir a sala, eles procuram por Nyssa em todo canto, mas não conseguem a achar.")
        time.sleep(3)
        print("\n")
        print("Nyssa ouve uma conversa")
        print("-Uma invasora no terreno sagrado?")
        time.sleep(2)
        print("\n")
        print("-ME PERDOE PAI, EU ERREI E DEIXEI ELA ENTRAR!")
        time.sleep(2)
        print("\n")
        print("-Se acalme, eu quero que você arrume um time e traga a cabeça dela, também verifique o tesouro sagrado se nada foi")
        print("perdido, pensarei no seu castigo depois")
        time.sleep(3)
        print("\n")
        print("-MUITO OBRIGADO ME GENEROSO PAI!")
        time.sleep(2)
        print("\n")
        print("Durante a procura Nyssa fica quieta esperando o momento certo, mas após alguns minutos ela nota que esses tuneis não")
        print("estavam abandonados por nada, mas sim por que era ali que uma família de ratos vivia, e ela só notou quando era tarde")
        print("demais, eles estavam sobre todo seu corpo a devorando.")
        time.sleep(5)
        print("\n")
        print("Ela não podia fazer barulho, ela tinha que aguentar a dor até a impressão acaba-se. Porem ela se estendeu por horas.")
        print(" E Nyssa só foi descoberta uma semana depois por causa que muitos fieis reclamaram de sangue saindo dos dutos abandonados.")
        print("Ela morreu e o seu cadáver parecia ter perdido várias partes para os ratos")
        Game_Over()
        
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
        print("\n")
        print("Ele olha novamente para Nyssa e diz")
        print("-Esse será o preço por andar no meu território, você está livre para ir,")
        print("mas com essas pernas duvido que vai ser muito longe")
        time.sleep(3)
        print("\n")
        print("Ele se levanta com um sorriso no rosto e some pelo horizonte. E assim Nyssa nunca mais.")
        print("foi encontrada com vida")
        Game_Over()

def Game_Over():
        print("\n\n")
        print("GAME OVER")
        time.sleep(3)
        print("\n\n")
        texto="1-Recomeçar\n2-Fim de Jogo\n"
        escolha=leiaint(texto)
        if(escolha==1):
               Inicio()
        else:
               pass

def Aceitar_Proposta1():
        print("Nyssa não pôde se conter, a ansiedade tomava seu corpo e alma.")
        time.sleep(5)
        print("Ao anoitecer, preparou-se com suas botas de couro e suas características pistolas que já tanto lhe ajudaram. ")
        time.sleep(8)
        print("Caminhou rumo ao endereço informado na carta, pensando em tudo que poderia lhe acontecer,")
        time.sleep(5)
        print("mas sua força de vontade era maior que qualquer medo. ")
        time.sleep(4)
        print("Ao chegar ao local marcado, deparou-se com uma casa velha que cheirava a mofo e terra molhada")
        time.sleep(5)
        print("e conforme se aproximava só piorava.")
        time.sleep(2)
        print("Ao adentrar a casa, dois capangas estavam na parte de dentro da porta,")
        time.sleep(5)
        print("um de cada lado. ")
        time.sleep(2)
        print("A mercenária foi levada pelos braços até uma sala iluminada por velas,")
        time.sleep(4)
        print("e ao chegar lá, encontrou seu possível empregador sentado atrás de uma mesa.")
        time.sleep(5)


        print("- Sente-se! – apontou para a cadeira a sua frente.")
        time.sleep(4)
        print("Os capangas a deixaram e mantiveram-se entre o homem misterioso e a mercenária, protegendo-o, obviamente.")
        time.sleep(5)
        print("- Recebi sua proposta. – Disse Nyssa olhando-o fixamente.")
        time.sleep(5)
        print("- Então agora podemos falar de negócios. – o homem sorriu de forma maldosa, contrastando a figura simpática que demonstrara na carta.")
        time.sleep(7)
        print("– Como pode perceber, - apontou para seus capangas- meus homens recebem muito bem para me obedecer. ") 
        time.sleep(6)
        print("E claro, não só de armas se vive alguém. – riu maliciosamente.")
        time.sleep(4)
        print("– Posso te oferecer tudo, drogas, galões de água, mantimentos...")
        time.sleep(5)
        print("- Podemos ir direto ao ponto? – Nyssa indagou impacientemente. ")
        time.sleep(5)
        print("– As propostas parecem boas demais para um serviço pequeno, eu diria.")
        time.sleep(5)
        print("- Vejo que você é sagaz. Bom, já que insiste lhe direi então! Minha proposta se trata de um grande trabalho, ")
        time.sleep(5)
        print("algo que pode beneficiar a todos, e principalmente, a mim, que preciso me reeleger. ")
        time.sleep(5)
        print("Esses pobres vermes rastejam em minha direção, implorando que eu conserte seus problemas e lhes ofereça oportunidades.")
        time.sleep(7)
        print("Mas é claro, isso não é tão fácil assim, ser um prefeito é um trabalho difícil, e é por isso que preciso de seu auxílio. ")
        time.sleep(8)
        print("Há alguns dias recebi rumores de um grande culto, que dentro de sua sede armazenam cilindros e máscaras de oxigênio, ")
        time.sleep(8)
        print("pode imaginar o que eu poderia conseguir se eu os possuísse? ")
        time.sleep(4)
        print("Preciso que os roube para mim, e se sobreviver, ganhará tudo que lhe foi prometido e muito mais!")
        time.sleep(5)
        print("! Eu cumpro com minha palavra, senhorita Nyssa. Sendo assim, posso contar com a sua? ? – o homem sorriu para ela lhe estendendo a mão. ")
        time.sleep(9)
        print("\n")
        texto = "1- Aceita a proposta \n 2- Recusar Proposta \n "
        escolha=leiaint(texto)
        if(escolha==1):
                Aceitar_Proposta2 ()   
        else:
                Negar_Proposta2()

def Aceitar_Proposta2():
        print("Sua proposta é realmente interessante, senhor prefeito. Mas, uma coisa me intriga.")
        time.sleep(5)   
        print("- O que seria senhorita? – disse o homem com um olhar curioso.")
        time.sleep(5)
        print("- Se estou indo para uma guerra, onde estão as armas?")
        time.sleep(5)
        print("- Então estamos chegando a algum lugar, veja! – apontou para a parede atrás dele. – Tenho algumas opções para você.")
        time.sleep(5)
        texto="Arma1\nBesta\nArma3"
        escolha=leiaint2(texto)
        if(escolha==1):
                print("oi")
        elif(escolha==2):
                Arma_Arco
        else:
                print("tchau")

def Negar_Proposta2():
        print("- A forma como você enxerga seu povo me enoja! Obrigada, senhor prefeito, mas prefiro recusar. – Nyssa levantou-se rindo.")
        time.sleep(5)
        print("- Você é um verme assim como eles, tentei te fazer como aliada, Nyssa, mas você não me dá outra escolha. ")
        time.sleep(5)
        print("– novamente riu, de forma irônica, irritante, mas sua risada fora abafada pelo som árduo do disparo das armas de seus homens.")
        time.sleep(5)
        print(" Olhou para o corpo ao chão e continuou - Lembre-se disso, não se recusa uma oferta irrecusável.")
        Game_Over()

def Negar_Proposta1():
        print("Nyssa olha e decide ignorar o pedaço de papel deixado para ela e sai para procurar mantimentos, ")
        time.sleep(5)
        print("mas ao voltar para sua casa a encontra em cinzas, completamente destruída. ")
        time.sleep(5)
        print("Porém, uma única coisa encontrava-se intacta, um bilhete colado em um tronco de árvore seco ao lado de sua casa,")
        time.sleep(5)
        print("nele estava escrito:")
        time.sleep(2)
        print("“Olá novamente, Nyssa! Eu bem lhe avisei que minha oferta era irrecusável.”")
        Game_Over

def Inicio():
    
    print("Nyssa acorda pela manhã com o barulho de três batidas na porta e uma carta passando por debaixo dela,")
    time.sleep(6)

    print("e ainda meio sonolenta ela se abaixa e pega a carta deixada em sua casa para ela,")
    time.sleep(6)

    print(" sem remente, apenas seu nome como destinatário")

    time.sleep(5)
    print("abrir o pedaço de papel, se depara com uma proposta:")
    print("\n")
    time.sleep(5)

    print(" “Saudações, Nyssa! Ouvi belíssimos rumores sobre sua última missão, sem dúvidas um sucesso")
    print("magnífico! E considerando seu grande êxito, tenho uma missão irrecusável para você, ")
    print("sei que seu preço não é barato, porém, ofereço água, drogas e munição. ")
    print("Encontre-me nessa localização para mais detalhes, venha sozinha!”")
    time.sleep(16)
    print("\n")

    texto ="1- para ir até a local \n 2- recusar proposta \n"
    escolha=leiaint(texto)
    if(escolha==1):
        Aceitar_Proposta1()   
    else:
        Negar_Proposta1()

Inicio()