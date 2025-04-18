# Padrões Criacionais

- [Abstract Factory](/creational/abstract_factory/vehicle_1.py)  
O padrão Abstract Factory oferece uma interface para criar famílias de objetos relacionados sem especificar suas classes concretas. Ele permite que o código seja independente da criação de objetos, facilitando a substituição de famílias de produtos, promovendo a flexibilidade e a extensibilidade no sistema.
![Diagram](/creational/abstract_factory/abstract_factory_diagram.png)

- [Builder](/creational/builder/builder_1.py)  
O padrão Builder separa a construção de um objeto complexo da sua representação. Ele permite criar objetos passo a passo, garantindo que o processo de construção seja flexível e reutilizável. É útil quando o objeto possui muitas partes opcionais ou a construção precisa ser feita de formas diferentes.
![Diagram](/creational/builder/builder_diagram.png)

- [Factory Method](/creational/factory_method/vehicle_1.py)  
O padrão Factory Method define uma interface para criar um objeto, mas permite que as subclasses decidam qual classe instanciar. Ele delega a responsabilidade de criação de objetos para subclasses, promovendo flexibilidade e desacoplamento no código, evitando a dependência direta de classes concretas.
![Diagram](/creational/factory_method/factory_method_diagram.png)

- [MonoState (Borg)](/creational/monostate_borg/monostate_1.py)  
O padrão MonoState (ou Borg) assegura que todas as instâncias de uma classe compartilhem o mesmo estado. Em vez de ter um único objeto, todas as instâncias armazenam dados no mesmo lugar, permitindo que elas se comportem como se fossem uma única instância, facilitando o gerenciamento de estado em sistemas com múltiplos objetos.

- [Prototype](/creational/prototype/prototype_1.py)  
O padrão Prototype permite criar novos objetos copiando um protótipo existente. Ele é útil quando a criação de objetos é complexa ou cara, permitindo duplicar instâncias de maneira eficiente. Com isso, evita-se a necessidade de reconstruir objetos do zero, promovendo flexibilidade e performance no sistema.
![Diagram](/creational/prototype/prototype_diagram.png)

- [Simple Factory](/creational/simple_factory/vehicle_1.py)  
O padrão Simple Factory fornece uma classe responsável pela criação de objetos, delegando a lógica de instância a um único ponto. Ele simplifica a criação de instâncias, ocultando a complexidade da criação de objetos em uma única classe, facilitando o gerenciamento e a escalabilidade do código.
![Diagram](/creational/simple_factory/simple_factory_diagram.png)

- [Singleton](/creational/singleton/singleton_1.py)  
O padrão Singleton garante que uma classe tenha apenas uma instância e fornece um ponto global de acesso a ela. É usado quando é necessário controlar o acesso a recursos compartilhados, como conexões com banco de dados ou arquivos de configuração, evitando múltiplas instâncias no sistema.
![Diagram](/creational/singleton/singleton_diagram.png)