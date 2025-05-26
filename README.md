# Princípios SOLID

Repositório com exemplos práticos em Python dos princípios de design de software SOLID. Cada arquivo demonstra um princípio específico com código comentado.

## Princípios Explicados

### 1. [Single Responsibility Principle (SRP)](SRP.py)
**Problema Resolvido:** Evita que uma classe tenha múltiplas razões para mudar, reduzindo o acoplamento e facilitando a manutenção.

**Exemplo Prático:**
- `User`: Gerencia apenas propriedades do usuário (nome, email)
- `UserRepository`: Responsável exclusivamente pela persistência

**Por Que é Um Bom Exemplo:**
A separação clara entre modelo de dados e operações de banco previne que mudanças na camada de persistência afetem a lógica de negócios. Se precisarmos mudar de SQL para NoSQL, apenas `UserRepository` será modificado.

---

### 2. [Open-Closed Principle (OCP)](OCP.py)
**Problema Resolvido:** Permite estender comportamentos sem modificar código existente, ideal para sistemas em evolução.

**Exemplo Prático:**
- Interface `Forma` com método abstrato `calcular_area()`
- Novas formas (`Retangulo`, `Circulo`) implementam a interface sem alterar `imprimir_area()`

**Por Que é Um Bom Exemplo:**
A função `imprimir_area()` trabalha com a abstração `Forma`, permitindo adicionar infinitas novas formas sem reescrever sua lógica. Isso é essencial para bibliotecas extensíveis.

---

### 4. [Interface Segregation Principle (ISP)](ISP.py)
**Problema Resolvido:** Elimina dependências forçadas em métodos não utilizados, reduzindo o impacto de mudanças.

**Exemplo Prático:**
- Interfaces especializadas (`Impressora`, `Digitalizadora`)
- `ImpressoraSimples` implementa apenas o necessário

**Por Que é Um Bom Exemplo:**
Se a interface `Digitalizadora` mudar, apenas as classes que realmente usam digitalização serão afetadas. Isso é crucial para sistemas com componentes opcionais.

---

### 5. [Dependency Inversion Principle (DIP)](DIP.py)
**Problema Resolvido:** Remove dependências diretas entre módulos de alto e baixo nível, facilitando testes e substituição de implementações.

**Exemplo Prático:**
- `ServicoRelatorio` depende da abstração `BancoDeDados`
- Implementações concretas (`MySQL`, `MongoDB`) são injetadas

**Por Que é Um Bom Exemplo:**
Para trocar o banco de dados, basta criar uma nova implementação da interface. O serviço principal permanece totalmente isolado de detalhes de infraestrutura.

---