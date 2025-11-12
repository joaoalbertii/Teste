import streamlit as st
st.title("Verificador de Idade")
Nome = st.text_input("Digite seu nome completo:")
idade_str = st.text_input("Digite sua idade (apenas números):")
if Nome and idade_str:
    if idade_str.isdigit():
        Idade = int(idade_str)
        if Idade < 0:
            st.write("Idade inválida")
        elif Idade <= 12:
            st.write(f"{Nome}, você ainda é uma crinçinha, que fofura.")
        elif Idade <= 17:
            st.write(f"{Nome}, você já está grande, começando a ter responsabilidade. Essa fase de adolescente é muito boa.")
        elif Idade <= 59:
            st.write(f"É {Nome}, tá ficando com dor nas costas já né!? Difícil ser adulto.")
        else:
            st.write(f"Já se aposentou {Nome}? kkkk ser idoso tem suas vantagens.")
    else:
        st.write("Digite apenas números inteiros para a idade!")
