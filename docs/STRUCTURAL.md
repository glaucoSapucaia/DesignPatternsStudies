# Padrões Estruturais

- [Adapter](/structural/adapter/adapter_1.py)  
O padrão Adapter permite que classes com interfaces incompatíveis trabalhem juntas. Ele age como um “tradutor”, convertendo a interface de uma classe em outra esperada pelo cliente. É útil para reaproveitar código legado ou integrar sistemas com APIs diferentes de forma transparente.
![Diagram](/structural/adapter/adapter_class_diagram.png)
![Diagram](/structural/adapter/adapter_object_diagram.png)

- [Bridge](/structural/bridge/bridge_1.py)  
O padrão Bridge separa a abstração da sua implementação, permitindo que ambas evoluam independentemente. Ele desacopla classes, dividindo-as em duas hierarquias: uma para abstração e outra para implementação. É útil para evitar uma explosão de subclasses em sistemas com múltiplas variações.
![Diagram](/structural/bridge/bridge_diagram.png)

- [Composite](/structural/composite/composite_1.py)  
O padrão Composite permite tratar objetos individuais e composições de objetos de forma uniforme. Ele organiza objetos em estruturas de árvore para representar hierarquias parte-todo, onde clientes podem interagir com objetos simples e compostos da mesma maneira. É útil em sistemas com componentes recursivos.
![Diagram](/structural/composite/binary_search_tree.png)
![Diagram](/structural/composite/composite_diagram.png)

- [Decorator](/structural/decorator/decorator_1.py)  
O padrão Decorator permite adicionar funcionalidades a um objeto dinamicamente, sem alterar sua estrutura original. Ele envolve o objeto original com uma nova classe que adiciona o comportamento desejado. É útil para estender funcionalidades de forma flexível e sem herança múltipla.
![Diagram](/structural/decorator/decorator_problem.png)
![Diagram](/structural/decorator/decorator_strategy.png)
![Diagram](/structural/decorator/decorator_diagram.png)

- [Facade](/structural/facade/facade_1.py)  
O padrão Facade fornece uma interface simplificada para um conjunto complexo de classes, bibliotecas ou subsistemas. Ele oculta detalhes internos e oferece um ponto de entrada único e mais fácil de usar. É ideal para reduzir a complexidade e facilitar a interação com sistemas grandes.
![Diagram](/structural/facade/facade_diagram.png)

- [Flyweight](/structural/flyweight/flyweight_1.py)  
O padrão Flyweight reduz o uso de memória ao compartilhar instâncias comuns de objetos. Ele é útil quando há muitos objetos semelhantes, como em jogos ou editores de texto. Objetos compartilhados armazenam dados imutáveis, enquanto dados únicos são mantidos externamente, otimizando desempenho e uso de recursos.
![Diagram](/structural/flyweight/flyweight_diagram.png)

- [Proxy](/structural/proxy/proxy_1.py)  
O padrão Proxy fornece um substituto ou representante para outro objeto, controlando o acesso a ele. Pode ser usado para adicionar funcionalidades como cache, controle de acesso ou carregamento preguiçoso. Ele permite interagir com o objeto real de forma segura e eficiente, sem expor sua complexidade.
![Diagran](/structural/proxy/proxy_diagram.png)