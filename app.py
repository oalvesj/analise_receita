import gradio as gr
import joblib
import pandas as pd

modelo = joblib.load("modelo_receita.pkl")

def prever_receita(tempo_de_experiencia, numero_de_vendas, fator_sazonal):
    entrada = pd.DataFrame({
        "tempo_de_experiencia": [tempo_de_experiencia],
        "numero_de_vendas": [numero_de_vendas],
        "fator_sazonal": [fator_sazonal],
    })
    previsao = modelo.predict(entrada)[0]
    return f"R$ {previsao:,.2f}"

demo = gr.Interface(
    fn=prever_receita,
    inputs=[
        gr.Number(label="Tempo de experiencia (meses)", value=60),
        gr.Number(label="Número de vendas", value=50),
        gr.Number(label="Fator sazonal (1 a 10)", value=5),
    ],
    outputs=gr.Textbox(label="Receita prevista"),
    title="Previsão de Receita de Vendas",
    description="Informe os dados do vendedor para estimar a receita gerada.",
)

if __name__ == "__main__":
    demo.launch()

