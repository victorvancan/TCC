import faust # type: ignore

# Definindo o aplicativo Faust
app = faust.App('anonymization_app', broker='kafka://localhost:9092')

# Definindo o tópico de entrada e saída
input_topic = app.topic('input_topic', value_type=str)
output_topic = app.topic('output_topic', value_type=str)

# Função para anonimizar os dados
@app.agent(input_topic)
async def anonymize(stream):
    async for value in stream:
        # Pseudonimização simples
        fields = value.split(",")
        pseudonym = f"user_{fields[0]}"  # Pseudonimiza o primeiro campo (ID)
        anonymized_value = f"{pseudonym},***,***"
        
        # Enviando o resultado para o tópico de saída
        await output_topic.send(value=anonymized_value)

# Iniciar o aplicativo
if __name__ == '__main__':
    app.main()
