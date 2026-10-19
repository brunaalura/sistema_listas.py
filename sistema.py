"""
Sistema de Listas em página web (Streamlit)
Os alunos podem: cadastrar, editar e excluir itens de uma lista.

Para rodar:
    pip install streamlit
    streamlit run sistema_listas_web.py
"""

import streamlit as st

st.set_page_config(page_title="Sistema de Listas", page_icon="📝")
st.title("📝 Sistema de Listas")

# O Streamlit executa o código de novo a cada clique.
# Por isso a lista fica guardada no session_state, para não ser apagada.
if "itens" not in st.session_state:
    st.session_state.itens = []

itens = st.session_state.itens


# ----- Cadastrar -----
with st.form("form_adicionar", clear_on_submit=True):
    novo = st.text_input("Novo item")
    enviado = st.form_submit_button("Adicionar")

if enviado:
    if novo.strip() == "":
        st.warning("Digite algo antes de adicionar.")
    else:
        itens.append(novo.strip())
        st.success(f"'{novo.strip()}' foi adicionado!")


# ----- Mostrar a lista -----
st.subheader("Sua lista")

if len(itens) == 0:
    st.info("A lista está vazia.")
else:
    for posicao, item in enumerate(itens, start=1):
        st.write(f"{posicao}. {item}")

    # ----- Editar ou excluir -----
    st.divider()
    st.subheader("Editar ou excluir")

    indice = st.selectbox(
        "Escolha o item",
        range(len(itens)),
        format_func=lambda i: f"{i + 1}. {itens[i]}",
    )

    novo_texto = st.text_input(
        "Texto do item",
        value=itens[indice],
        key=f"edit_{indice}_{itens[indice]}",
    )

    col1, col2 = st.columns(2)

    if col1.button("Salvar edição"):
        if novo_texto.strip() == "":
            st.warning("O item não pode ficar vazio.")
        else:
            itens[indice] = novo_texto.strip()
            st.rerun()

    if col2.button("Excluir"):
        itens.pop(indice)
        st.rerun()