def sort_code(input_string):
    # Verifica se a entrada é uma string válida
    if not isinstance(input_string, str):
        raise ValueError("A entrada deve ser uma string.")
    
    # Ordena os caracteres da string
    return ''.join(sorted(input_string))

# Função de teste
def test_sort_code():
    try:
        # Casos de teste
        assert sort_code("pqksuvy") == "kpqsuvy", "Teste falhou: caso 1"
        assert sort_code("dcba") == "abcd", "Teste falhou: caso 2"
        assert sort_code("1234") == "1234", "Teste falhou: caso 3"
        assert sort_code("a1c2") == "12ac", "Teste falhou: caso 4"
        assert sort_code("") == "", "Teste falhou: caso 5"
        
        print("Todos os testes passaram com sucesso!")
    except AssertionError as e:
        print(f"Erro no teste: {e}")
    except ValueError as ve:
        print(f"Erro de validação: {ve}")

# Executar os testes
test_sort_code()