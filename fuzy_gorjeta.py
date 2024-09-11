import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import streamlit as st
import matplotlib.pyplot as plt

# Definindo as variáveis fuzzy e seus termos
servico = ctrl.Antecedent(np.arange(0, 11, 1), 'servico')
qualidade_comida = ctrl.Antecedent(np.arange(0, 11, 1), 'qualidade_comida')
gorjeta = ctrl.Consequent(np.arange(0, 21, 1), 'gorjeta')

# Definindo os termos fuzzy para cada variável
servico['ruim'] = fuzz.trimf(servico.universe, [0, 0, 5])
servico['aceitavel'] = fuzz.trimf(servico.universe, [3, 5, 7])
servico['otimo'] = fuzz.trimf(servico.universe, [5, 10, 10])

qualidade_comida['ruim'] = fuzz.trimf(qualidade_comida.universe, [0, 0, 5])
qualidade_comida['boa'] = fuzz.trimf(qualidade_comida.universe, [3, 5, 7])
qualidade_comida['saborosa'] = fuzz.trimf(qualidade_comida.universe, [5, 10, 10])

gorjeta['baixa'] = fuzz.trimf(gorjeta.universe, [0, 0, 5])
gorjeta['media'] = fuzz.trimf(gorjeta.universe, [5, 10, 15])
gorjeta['alta'] = fuzz.trimf(gorjeta.universe, [15, 20, 20])

# Definindo as regras fuzzy
regra1 = ctrl.Rule(qualidade_comida['ruim'] | servico['ruim'], gorjeta['baixa'])
regra2 = ctrl.Rule(servico['aceitavel'], gorjeta['media'])
regra3 = ctrl.Rule(servico['otimo'] & qualidade_comida['saborosa'], gorjeta['alta'])

# Criando o sistema de controle
controle = ctrl.ControlSystem([regra1, regra2, regra3])
sistema = ctrl.ControlSystemSimulation(controle)

# Interface gráfica com Streamlit
st.title("Sistema Fuzzy para Cálculo de Gorjeta")

# Slider para entrada de valores
st.sidebar.title('Valores de Entrada')
servico_value = st.sidebar.slider('Nota para o Serviço', 0, 10, 5)
qualidade_comida_value = st.sidebar.slider('Qualidade da Comida', 0, 10, 5)

# Atualizando os valores de entrada no sistema fuzzy
sistema.input['servico'] = servico_value
sistema.input['qualidade_comida'] = qualidade_comida_value

# Computando o resultado
sistema.compute()

# Obtendo o valor de saída nítido
gorjeta_value = sistema.output['gorjeta']

# Exibindo o resultado
st.markdown(f'**Gorjeta calculada: {gorjeta_value:.2f}%**')

# Visualização dos universos e funções de pertinência
st.subheader('Visualização das Funções de Pertinência')

# Função auxiliar para plotar a função de pertinência
def plot_membership_function(ax, variable, label):
    for term in variable.terms.values():
        x = variable.universe
        y = term.mf
        ax.plot(x, y, label=term.label, linewidth=1.5)
    ax.set_title(label)
    ax.legend()

# Plotando as funções de pertinência
fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(8, 12))

# Serviço
plot_membership_function(ax1, servico, 'Nota para o Serviço')

# Qualidade da Comida
plot_membership_function(ax2, qualidade_comida, 'Qualidade da Comida')

# Gorjeta
plot_membership_function(ax3, gorjeta, 'Gorjeta')

# Ajustes finais de layout
plt.tight_layout()

# Mostrando os gráficos no Streamlit
st.pyplot(fig)

# Seção de Fórmulas e Cálculos
st.subheader('Fórmulas e Cálculos')

st.markdown("""
### Cálculo do Centroide

O valor de saída para o sistema fuzzy é calculado usando o método do centroide. O centroide é o ponto médio da área sob a curva de pertinência ponderada pelas funções de pertinência.

A fórmula do centroide é dada por:

\[ \text{Centroide} = \frac{\int x \cdot \mu(x) \, dx}{\int \mu(x) \, dx} \]

Onde:
- \( x \) é o valor da variável de saída (gorjeta)
- \( \mu(x) \) é a função de pertinência da variável de saída

### Exemplo de Cálculo

Suponha que temos as funções de pertinência fuzzy para a gorjeta como segue:

- Baixa: \(\text{fuzz.trimf(gorjeta.universe, [0, 0, 5])}\)
- Média: \(\text{fuzz.trimf(gorjeta.universe, [5, 10, 15])}\)
- Alta: \(\text{fuzz.trimf(gorjeta.universe, [15, 20, 20])}\)

A área total é a soma das áreas das funções de pertinência, e o numerador é a soma de cada valor \( x \) ponderado pela sua função de pertinência.

### Implementação

No código, o cálculo do centroide é feito automaticamente pelo método `compute` do `ControlSystemSimulation` do `skfuzzy`, que realiza a integração das funções de pertinência para calcular a saída.

""")
