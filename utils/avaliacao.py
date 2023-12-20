from sklearn.metrics import classification_report

def avaliar_classificacao(y_true, y_pred):
    # Avaliação da classificação
    relatorio_classificacao = classification_report(y_true, y_pred)
    return relatorio_classificacao
