import streamlit as st

# Título da página
st.title("Comparação de Algoritmos: Natureza vs Heurística")

# Seção: Algoritmos Inspirados na Natureza
st.header("Algoritmos Inspirados na Natureza")

st.subheader("Características Gerais")
st.write("""
- **Base Biológica**: Inspirados em comportamentos naturais e sociais de organismos como formigas, abelhas e até mesmo a evolução das espécies.
- **População de Soluções**: Trabalham com uma população de soluções simultaneamente, e não com uma única solução.
- **Exploração e Exploração**: Combinam a exploração de novas áreas e a exploração local das melhores soluções encontradas.
- **Memória e Atualização**: Utilizam mecanismos de memória (como feromônio em ACO ou informações de qualidade de soluções em Bees Algorithm) para guiar a busca.
""")

st.subheader("Exemplos")
st.write("""
- **Bees Algorithm**: Usa abelhas empregadas e exploradoras para buscar soluções locais e globais.
- **ACO (Algoritmo de Colônia de Formigas)**: Baseado em feromônio deixado por formigas para guiar a busca.
- **GA (Algoritmo Genético)**: Usa operações de cruzamento e mutação em uma população de soluções.
""")

# Seção: Algoritmos de Busca Heurística
st.header("Algoritmos de Busca Heurística")

st.subheader("Características Gerais")
st.write("""
- **Busca em Espaço de Estados**: Projetados para explorar o espaço de estados de um problema, geralmente focando na busca de um caminho ótimo ou solução.
- **Estado Único ou Sequencial**: Trabalham com uma única solução ou um caminho em um dado momento, em vez de uma população de soluções.
- **Heurísticas**: Usam heurísticas para avaliar e priorizar estados ou caminhos, com o objetivo de encontrar a melhor solução possível.
""")

st.subheader("Exemplos")
st.write("""
- **Busca A***:
  - **Estratégia**: Combina a busca em largura e profundidade com heurísticas para encontrar o caminho mais curto ou a solução ótima.
  - **Funcionamento**: Usa uma função de custo que combina o custo do caminho atual com uma estimativa heurística do custo restante para atingir o objetivo.
  - **Heurística**: A função heurística deve ser admissível e, de preferência, consistente, para garantir a optimalidade.

- **Busca Gulosa**:
  - **Estratégia**: Sempre escolhe a opção que parece ser a melhor localmente, sem considerar as consequências a longo prazo.
  - **Funcionamento**: Utiliza uma função heurística para decidir qual caminho seguir, priorizando o que parece ser mais promissor em cada etapa.
  - **Heurística**: Pode não garantir a solução ótima, pois pode ficar preso em ótimos locais.
""")

# Seção: Comparação
st.header("Comparação")

st.subheader("Abordagem de Busca")
st.write("""
- **Algoritmos Inspirados na Natureza**: Trabalham com uma população de soluções, aplicando mecanismos de adaptação e evolução inspirados na biologia.
- **Algoritmos Heurísticos**: Focam em encontrar uma solução a partir de um estado inicial, muitas vezes explorando um caminho ou uma sequência de estados.
""")

st.subheader("Exploração e Exploração")
st.write("""
- **Algoritmos Inspirados na Natureza**: Utilizam métodos combinados de exploração local e global, muitas vezes utilizando memória para guiar a busca.
- **Algoritmos Heurísticos**: Normalmente exploram localmente, seguindo a heurística para tomar decisões sobre qual caminho seguir.
""")

st.subheader("Memória e Atualização")
st.write("""
- **Algoritmos Inspirados na Natureza**: Usam memória implícita ou explícita para guiar a busca, como feromônio em ACO ou qualidade de soluções em Bees Algorithm.
- **Algoritmos Heurísticos**: Geralmente, não têm memória de soluções anteriores, focando em expandir o caminho atual com base na heurística.
""")

st.subheader("Solucionamento de Problemas")
st.write("""
- **Algoritmos Inspirados na Natureza**: São usados para problemas complexos onde a busca global é importante e a solução pode ser muito grande ou multidimensional.
- **Algoritmos Heurísticos**: São eficazes em problemas onde uma boa heurística pode guiar a busca de forma eficiente, muitas vezes em problemas de menor escala ou onde a solução é mais bem definida.
""")

st.write("""
**Conclusão**: 
Os algoritmos inspirados na natureza e os algoritmos heurísticos são abordagens distintas para a resolução de problemas. Enquanto os algoritmos inspirados na natureza utilizam princípios biológicos para explorar e adaptar soluções, os algoritmos heurísticos aplicam métodos de avaliação e seleção baseados em heurísticas para encontrar soluções de maneira mais direta. Ambos têm seus próprios conjuntos de vantagens e desvantagens, dependendo do tipo e complexidade do problema a ser resolvido.
""")
