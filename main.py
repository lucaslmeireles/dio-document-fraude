import streamlit as st
from services.blob_service import upload_image_to_blob
from services.card_service import analyze_credit_card_image

def configure_interface():
    st.title("Validação de Cartão de Crédito")
    st.write("Faça upload de uma imagem do seu cartão de crédito para validar as informações.")
    uploaded_file = st.file_uploader("Escolha uma imagem do cartão de crédito", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        fileName = uploaded_file.name

        blob_url = upload_image_to_blob(uploaded_file, fileName)
        if blob_url:
            st.write("Imagem enviada com sucesso!")
            credit_card_info = analyze_credit_card_image(blob_url)
            show_image_and_validation(blob_url, credit_card_info)
        else:
            st.write("Erro ao enviar a imagem. Por favor, tente novamente.")
            credit_card_info = None

def show_image_and_validation(blob_url, credit_card_info):
    st.image(blob_url, caption="Imagem enviada", use_column_width=True)
    st.write("Informações do cartão de crédito:")
    if credit_card_info and credit_card_info["card_name"]:
        st.markdown(f"<h1 style='color: green;'> Cartão Valido </h1>", unsafe_allow_html=True)
        st.write(f"Nome do titular: {credit_card_info['card_name']}")
        st.write(f"Nome do emissor: {credit_card_info['bank_name']}")
        st.write(f"Validade: {credit_card_info['expiry_date']}")
    else:
        st.markdown(f"<h1 style='color: red;'> Cartão Invalido </h1>", unsafe_allow_html=True)
        st.write("Não foi possível extrair as informações do cartão de crédito. Por favor, tente novamente com uma imagem mais clara ou diferente.")
if __name__ == "__main__":
    main()
