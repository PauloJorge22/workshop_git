![Logótipo do NEIIST](https://neiist.tecnico.ulisboa.pt/static/media/neiist_logo.5b6bbd8f2f7eb5ee5200.png)
# Cenários de colaboração com Git para grupos
Este guia é constituído por vários cenários práticos para colaboração em grupos de 2-3, todos a trabalhar no mesmo fork do repositório "workshop_git". O objetivo é aplicar os conceitos e comandos de Git aprendidos durante o workshop.


## 0. Setup
- Uma pessoa do grupo faz uma cópia do repositório original para o seu Github (fork).
- Todos copiam o fork para as suas máquinas.


### 1. Desenvolver features em branches
Cada membro:
- Cria o seu branch de desenvolvimento
- Implementa uma nova operação no ficheiro "main.py".
- Salva e envia para o repositório remoto


### 2. Juntar features ao master (+ possíveis conflitos)
- Adicionem as novas features ao master
- Atualizem localmente


### 3. Resolver Conflitos
- Implementem uma operação "extra" no vosso branch e adicionem ao master.
(O mais rápido estará livre de conflitos, mas os restantes terão de resolvê-los)

ola


### 4. Voltar atrás no tempo
- O elemento que ficou livre de conflitos deverá repôr o master para a versão sem operador "extra".


### 5. Marcar versão
- Marquem o estado atual da calculadora como "Versão 1.0"


### 6. Estado da working tree
- Façam vários commits de alteração ao README no vosso branch e dêm merge com os commits agregados num só.


### 7. Colocar o desenvolvimento em standby
- Comecem a desenvolver uma nova feature, a meio do processo, mudem de branch para o master. Que comando deverão utilizar para que as alterações não sejam apagadas?


### 8. Pedido de integração com o repositório original
- Peçam a integração do vosso trabalho com o repositório original.


