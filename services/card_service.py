from azure.core.credentials import AzureKeyCredential
from azure.ai.documentintelligence import DocumentIntelligenceClient
from azure.ai.documentintelligence.models import AnalyzeDocumentRequest
import os
def analyze_credit_card_image(blob_url):
    try:
       creditial = AzureKeyCredential(os.getenv('AZURE_FORM_RECOGNIZER_KEY'))
       documment_Client = DocumentIntelligenceClient(os.getenv('AZURE_FORM_RECOGNIZER_ENDPOINT'), creditial)

       result = documment_Client.begin_analyze_document_from_url("prebuilt-creditCard", AnalyzeDocumentRequest(url_source=blob_url)).result()
    
       for card in result.documents:
           card_info = {
               "card_name": card.fields.get("CardholderName").value if card.fields.get("CardholderName") else None,
               "bank_name": card.fields.get("Issuer").value if card.fields.get("Issuer") else None,
               "expiry_date": card.fields.get("ExpirationDate").value if card.fields.get("ExpirationDate") else None
           }
           return card_info
    except Exception as e:
        print(f"Erro ao analisar a imagem do cartão de crédito: {e}")
        return None