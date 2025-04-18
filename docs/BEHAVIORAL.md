# Padrões Comportamentais

- [Chain](./behavioral/chain/chain_of_responsibility.py)  
O padrão Chain of Responsibility permite que múltiplos objetos tratem uma requisição, passando-a ao longo de uma cadeia até que um deles a processe. Ele desacopla o remetente do receptor, tornando o sistema flexível e facilitando a adição ou reorganização de manipuladores sem alterar o código cliente.
![Diagram](/behavioral/chain/chain_responsibility_diagram.png)

- [Command](/behavioral/command/command_1.py)  
O padrão Command encapsula uma solicitação como um objeto, permitindo parametrizar ações, enfileirar comandos e suportar operações como desfazer/refazer. Ele desacopla o emissor da ação do seu executor, promovendo flexibilidade na execução de tarefas e no controle de comandos em sistemas complexos.
![Diagram](/behavioral/command/command_diagram.png)

- [Iterator](/behavioral/iterator/iterator_1.py)  
O padrão Iterator fornece uma maneira de acessar os elementos de um objeto agregado (como uma lista ou conjunto) sequencialmente, sem expor sua estrutura interna. Ele permite percorrer os elementos de forma uniforme e independente da implementação da coleção, facilitando a navegação em diferentes tipos de coleções.
![Diagram](/behavioral/iterator/iterator_diagram.png)

- [Mediator](/behavioral/mediator/mediator_1.py)  
O padrão Mediator centraliza a comunicação entre objetos, evitando dependências diretas entre eles. Em vez de interagir diretamente, os objetos se comunicam com um mediador, que gerencia as interações. Isso reduz o acoplamento e melhora a manutenção, tornando o sistema mais flexível e organizado.
![Diagram](/behavioral/mediator/mediator_problem.png)
![Diagram](/behavioral/mediator/mediator_diagram.png)

- [Memento](/behavioral/memento/memento_1.py)  
O padrão Memento captura e armazena o estado interno de um objeto sem expor sua estrutura. Ele permite restaurar o objeto a um estado anterior sem violar o encapsulamento. É útil para implementar funcionalidades como desfazer/refazer em sistemas, mantendo a integridade do objeto original.
![Diagram](/behavioral/memento/memento_diagram.png)

- [Observer](/behavioral/observer/observer_1.py)  
O padrão Observer define uma dependência um-para-muitos entre objetos, de modo que quando um objeto (sujeito) muda de estado, todos os seus dependentes (observadores) são notificados e atualizados automaticamente. É útil em sistemas onde múltiplos componentes precisam reagir a mudanças em outro componente sem acoplamento direto.
![Diagram](/behavioral/observer/observer_diagram.png)

- [State](/behavioral/state/state_1.py)  
O padrão State permite que um objeto altere seu comportamento quando seu estado interno muda. Ele encapsula os estados em classes distintas, permitindo que o objeto mude de estado sem alterar seu código. Isso melhora a flexibilidade e facilita a manutenção, especialmente em sistemas com comportamentos variados e complexos.
![Diagram](/behavioral/state/state_problem_diagram.png)
![Diagram](/behavioral/state/state_diagram.png)

- [Strategy](/behavioral/strategy/strategy_1.py)  
O padrão Strategy define uma família de algoritmos, encapsula cada um deles e os torna intercambiáveis. Ele permite que o comportamento de um objeto seja alterado em tempo de execução, sem modificar seu código. É útil quando há várias maneiras de realizar uma tarefa e a escolha da estratégia deve ser flexível.
![Diagram](/behavioral/strategy/strategy_diagram.png)

- [Template Method](/behavioral/template_method/template_method_1.py)  
O padrão Template Method define o esqueleto de um algoritmo em um método, permitindo que subclasses implementem passos específicos. A estrutura do algoritmo é mantida, enquanto a variação de comportamento é delegada para métodos concretos nas subclasses. Isso facilita a reutilização de código e promove a consistência.
![Diagram](/behavioral/template_method/template_method_diagram.png)