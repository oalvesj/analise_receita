# Previsão de Receita de Vendas

Projeto de análise e previsão da receita gerada por vendedores a partir do tempo de experiência, número de vendas e fator sazonal. O trabalho compara diferentes modelos de regressão para identificar o mais eficiente e disponibiliza o modelo treinado em um app interativo com Gradio.

## Estrutura

- `analise_receita.ipynb` — notebook com a análise exploratória, comparação de modelos (Regressão Linear, Regressão Polinomial e Random Forest) e salvamento do melhor modelo.
- `app.py` — aplicação Gradio que carrega o modelo e prevê a receita a partir dos dados informados.
- `modelo_receita.pkl` — melhor modelo treinado, salvo para uso no app.
- `sales_data.csv` — base de dados utilizada.

## Resultados e conclusão

As três variáveis têm correlação muito baixa com a receita (todas próximas de zero), então nenhum modelo consegue prever a receita com boa precisão. Entre os testados, a **Regressão Polinomial** foi a mais eficiente (maior R² e menor erro), sendo escolhida como modelo final. A conclusão principal é que, com os dados disponíveis, essas variáveis não explicam bem a receita gerada: para um modelo realmente útil seriam necessárias outras informações.

## Tecnologias

- Python 3
- Pandas, NumPy, Matplotlib
- scikit-learn
- joblib
- Gradio

## Como rodar

1. Instale as dependências:

```bash
pip install -r requirements.txt
```

2. Execute o notebook `analise_receita.ipynb` para gerar o `modelo_receita.pkl`.

3. Rode o app de previsão:

```bash
python app.py
```

O Gradio abre uma página no navegador com os campos de entrada e a receita prevista.
