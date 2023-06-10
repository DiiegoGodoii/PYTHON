import streamlit as st
import pickle

def carregar_produtos():
    try:
        with open("produtos.pkl", "rb") as file:
            return pickle.load(file)
    except FileNotFoundError:
        return {}

def salvar_produtos(produtos):
    with open("produtos.pkl", "wb") as file:
        pickle.dump(produtos, file)

def adicionar_produto(nome, preco):
    if nome not in produtos:
        produtos[nome] = preco
        salvar_produtos(produtos)
        return True
    else:
        return False

def atualizar_preco(nome, novo_preco):
    if nome in produtos:
        produtos[nome] = novo_preco
        salvar_produtos(produtos)
        return True
    else:
        return False

def excluir_produto(nome):
    if nome in produtos:
        del produtos[nome]
        salvar_produtos(produtos)
        return True
    else:
        return False

def mostrar_produtos():
    st.write("## Lista de Produtos")
    if produtos:
        for nome, preco in produtos.items():
            st.write(f"- {nome}: R${preco:.2f}")
    else:
        st.write("Nenhum produto cadastrado.")

# Carrega os produtos ao iniciar o aplicativo
produtos = carregar_produtos()

def main():
    st.title("Aplicativo CRUD de Produtos")
    
    opcoes = ["Adicionar Produto", "Atualizar Preço", "Excluir Produto", "Mostrar Produtos"]
    escolha = st.sidebar.selectbox("Selecione uma opção", opcoes)
    
    if escolha == "Adicionar Produto":
        st.header("Adicionar Produto")
        nome = st.text_input("Nome do Produto")
        preco = st.number_input("Preço do Produto", step=0.01, format="%.2f")
        
        if st.button("Adicionar"):
            if adicionar_produto(nome, preco):
                st.success("Produto adicionado com sucesso!")
            else:
                st.error("Produto já existe na lista!")

    elif escolha == "Atualizar Preço":
        st.header("Atualizar Preço")
        nome = st.selectbox("Selecione um produto", list(produtos.keys()))
        novo_preco = st.number_input("Novo Preço", step=0.01, format="%.2f")
        
        if st.button("Atualizar"):
            if atualizar_preco(nome, novo_preco):
                st.success("Preço atualizado com sucesso!")
            else:
                st.error("Produto não encontrado!")

    elif escolha == "Excluir Produto":
        st.header("Excluir Produto")
        nome = st.selectbox("Selecione um produto", list(produtos.keys()))
        
        if st.button("Excluir"):
            if excluir_produto(nome):
                st.success("Produto excluído com sucesso!")
            else:
                st.error("Produto não encontrado!")

    elif escolha == "Mostrar Produtos":
        mostrar_produtos()

if __name__ == "__main__":
    main()
