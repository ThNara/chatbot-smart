def chatbot_smart():
    print("Olá! Vou te ajudar a definir uma meta usando o método SMART.")
    
    # S - Específica
    meta = input("\nQual é sua meta principal? ")
    especifica = input("O que exatamente você quer alcançar? Seja o mais específico possível: ")
    
    # M - Mensurável
    mensuravel = input("Como você saberá que atingiu essa meta? (ex.: um número, um prazo, um resultado específico) ")
    
    # A - Atingível
    atingivel = input("Essa meta é realista para você no momento? O que você precisa fazer para alcançá-la? ")
    
    # R - Relevante
    relevante = input("Por que essa meta é importante para você? Como ela se encaixa nos seus objetivos maiores? ")
    
    # T - Temporal
    prazo = input("Qual o prazo para atingir essa meta? (ex.: dias, semanas, meses, anos) ")
    
    # Resumo da meta SMART
    print("\nAqui está a sua meta no formato SMART:")
    print(f"Meta: {meta}")
    print(f"Específica: {especifica}")
    print(f"Mensurável: {mensuravel}")
    print(f"Atingível: {atingivel}")
    print(f"Relevante: {relevante}")
    print(f"Temporal: {prazo}")

    print("\nO que achou? Se precisar ajustar, você pode rodar o chatbot novamente!")

# Executar o chatbot
chatbot_smart()
