import streamlit as st
import pandas as pd
import numpy as np
from itertools import combinations


# Função para calcular o suporte de um itemset
def calculate_support(itemset, transactions):
    return np.mean([set(itemset).issubset(set(transaction)) for transaction in transactions])


# Função para gerar combinações de k-itemsets
def generate_candidates(itemsets, k):
    return [set(x) for x in combinations(set().union(*itemsets), k)]


# Função para calcular o Lift de uma regra
def calculate_lift(antecedent, consequent, support_data):
    antecedent_support = support_data.get(frozenset(antecedent), 0)
    consequent_support = support_data.get(frozenset(consequent), 0)
    itemset_support = support_data.get(frozenset(antecedent) | frozenset(consequent), 0)

    if antecedent_support > 0 and consequent_support > 0:
        lift = itemset_support / (antecedent_support * consequent_support)
    else:
        lift = 0

    return lift


# Algoritmo Apriori
def apriori(transactions, min_support, min_confidence):
    itemsets = [{item} for transaction in transactions for item in transaction]
    itemsets = [set(item) for item in set(frozenset(item) for item in itemsets)]
    large_itemsets = []
    k = 1
    support_data = {}

    while itemsets:
        # Calcula o suporte de cada itemset
        itemsets_with_support = [(itemset, calculate_support(itemset, transactions)) for itemset in itemsets]
        # Filtra os itemsets que atendem ao suporte mínimo
        itemsets = [itemset for itemset, support in itemsets_with_support if support >= min_support]
        for itemset in itemsets:
            support_data[frozenset(itemset)] = calculate_support(itemset, transactions)
        large_itemsets.extend(itemsets)
        k += 1
        itemsets = generate_candidates(itemsets, k)

    # Regras de associação
    rules = []
    for itemset in large_itemsets:
        if len(itemset) > 1:
            for antecedent in combinations(itemset, len(itemset) - 1):
                antecedent = set(antecedent)
                consequent = itemset - antecedent
                antecedent_support = support_data.get(frozenset(antecedent), 0)
                itemset_support = support_data.get(frozenset(itemset), 0)
                confidence = itemset_support / antecedent_support if antecedent_support > 0 else 0
                lift = calculate_lift(antecedent, consequent, support_data)

                if confidence >= min_confidence:
                    rules.append({
                        'antecedent': antecedent,
                        'consequent': consequent,
                        'support': itemset_support,
                        'confidence': confidence,
                        'lift': lift
                    })

    return large_itemsets, rules


# Função para exibir os resultados no Streamlit
def show_apriori():
    st.title("Algoritmo Apriori para Regras de Associação")

    # Introdução ao Algoritmo Apriori
    st.header("Introdução ao Algoritmo Apriori")
    st.write("""
    O **algoritmo Apriori** é utilizado para a descoberta de **regras de associação** em grandes conjuntos de dados, como transações de compras. Ele utiliza três métricas principais:

    - **Suporte (Support)**: A frequência com que um item ou conjunto de itens aparece nas transações.
    - **Confiança (Confidence)**: A probabilidade condicional de que o consequente de uma regra de associação ocorra dado o antecedente.
    - **Lift**: Medida que indica o aumento da probabilidade de ocorrência do consequente devido à presença do antecedente, comparado com a probabilidade de ocorrência do consequente de forma independente.

    A ideia principal é identificar **itemsets frequentes** que satisfaçam um suporte mínimo e depois gerar regras de associação que atendam a uma confiança mínima.
    """)

    # Fórmulas de Suporte, Confiança e Lift
    st.subheader("Fórmulas Utilizadas")
    st.latex(r'Support(A) = \frac{\text{Número de transações contendo } A}{\text{Número total de transações}}')
    st.latex(r'Confidence(A \Rightarrow B) = \frac{\text{Support}(A \cup B)}{\text{Support}(A)}')
    st.latex(r'Lift(A \Rightarrow B) = \frac{\text{Support}(A \cup B)}{\text{Support}(A) \cdot \text{Support}(B)}')

    st.write("""
    Onde:
    - \( A \) é o antecedente da regra.
    - \( B \) é o consequente da regra.
    """)

    # Seção de características dos algoritmos de regras de associação
    st.header("Características dos Algoritmos de Regras de Associação")
    st.write("""
    Os algoritmos de regras de associação, como o Apriori, são utilizados para descobrir padrões e relações ocultas em grandes bases de dados transacionais. Algumas de suas principais características incluem:

    - **Descoberta de Padrões Frequentes**: Identifica subconjuntos frequentes de itens em transações.
    - **Geração de Regras**: Cria regras que descrevem associações significativas entre os itens.
    - **Escalabilidade**: Algoritmos como Apriori podem ser aplicados em grandes volumes de dados, embora possam enfrentar desafios de desempenho à medida que o número de itens cresce.
    - **Suporte, Confiança e Lift**: As regras geradas dependem de três parâmetros principais: suporte, confiança e lift, para garantir que apenas padrões relevantes sejam identificados.
    """)

    # Seção de vantagens
    st.header("Vantagens do Algoritmo Apriori")
    st.write("""
    O algoritmo Apriori possui diversas vantagens:

    - **Simplicidade**: É relativamente fácil de entender e implementar.
    - **Controle de Parâmetros**: O uso de suporte, confiança e lift permite ao usuário controlar a quantidade e a relevância das regras geradas.
    - **Identificação de Relações**: Capaz de encontrar associações úteis e compreensíveis em bases de dados transacionais.
    - **Aplicações em Diversas Áreas**: Pode ser aplicado em diferentes setores, como varejo (cestas de compras), marketing, saúde, entre outros.
    """)

    # Seção de desvantagens
    st.header("Desvantagens do Algoritmo Apriori")
    st.write("""
    No entanto, o Apriori também apresenta algumas desvantagens:

    - **Alta Complexidade Computacional**: O número de combinações de itens pode crescer exponencialmente à medida que o número de itens aumenta, resultando em custos computacionais elevados.
    - **Número Exagerado de Regras**: Pode gerar um grande número de regras, muitas das quais podem ser triviais ou não interessantes.
    - **Necessidade de Suporte Mínimo Alto**: Para evitar explosão combinatória, o suporte mínimo muitas vezes precisa ser ajustado para valores mais altos, o que pode levar à perda de padrões raros.
    - **Inflexível para Dados Complexos**: Pode não ser adequado para conjuntos de dados que não são transacionais ou que possuem estruturas complexas.
    """)

    # Conclusão
    st.header("Conclusão")
    st.write("""
    O **algoritmo Apriori** é uma poderosa ferramenta para descobrir padrões de associação em grandes volumes de dados, sendo particularmente útil em ambientes como análise de cestas de compras no varejo. Embora apresente limitações em termos de desempenho e possa gerar um número elevado de regras triviais, seus benefícios superam esses desafios quando bem aplicado. Algoritmos mais avançados, como FP-Growth, podem ser utilizados em cenários em que o desempenho do Apriori não seja satisfatório.
    """)

    # Exemplo prático com conjunto de transações
    st.header("Exemplo Prático: Análise de Regras de Associação com Apriori")

    # Exemplo de transações
    transactions = [
        ['leite', 'pão', 'manteiga'],
        ['leite', 'pão'],
        ['pão', 'manteiga'],
        ['leite', 'manteiga'],
        ['pão', 'manteiga', 'queijo'],
        ['leite', 'pão', 'manteiga', 'queijo']
    ]

    st.subheader("Transações de Exemplo")
    df = pd.DataFrame(transactions, columns=["Item 1", "Item 2", "Item 3", "Item 4"])
    st.write(df.fillna(""))

    # Parâmetros de suporte e confiança
    min_support = st.slider("Suporte Mínimo", 0.1, 1.0, 0.5)
    min_confidence = st.slider("Confiança Mínima", 0.1, 1.0, 0.7)

    # Executar o algoritmo Apriori
    large_itemsets, rules = apriori(transactions, min_support, min_confidence)

    # Exibir os itemsets frequentes
    st.subheader("Itemsets Frequentes")
    st.write(large_itemsets)

    # Exibir as regras geradas
    st.subheader("Regras de Associação Geradas")
    if rules:
        for rule in rules:
            st.write(f"{rule['antecedent']} -> {rule['consequent']}")
            st.write(f"Suporte: {rule['support']:.2f}, Confiança: {rule['confidence']:.2f}, Lift: {rule['lift']:.2f}")
    else:
        st.write("Nenhuma regra gerada com os parâmetros selecionados.")


# Execução do código no Streamlit
if __name__ == "__main__":
    show_apriori()
