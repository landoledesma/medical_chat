# Proyecto de Bot de Chat QA

Este proyecto implementa un bot de chat de calidad de pregunta y respuesta (QA) utilizando la biblioteca Langchain junto con las API de OpenAI y FAISS (Facebook AI Similarity Search) para el almacenamiento y recuperación vectorial eficiente.

## Requisitos Previos

- Python 3.6 o superior.
- Credenciales de la API de OpenAI.
- Un entorno virtual de Python (opcional pero recomendado).

## Configuración del Entorno

1. **Clonar el Repositorio**:
```bash
git clone https://github.com/usuario/proyecto-qa-bot.git
cd proyecto-qa-bot
```

2. **Crear y Activar un Entorno Virtual** (opcional pero recomendado):
```bash
python3 -m venv env
source env/bin/activate  # En Windows use: env\Scripts\activate
```

3. **Instalar Dependencias**:
```bash
pip install -r requirements.txt
```

## Configuración de las Credenciales de OpenAI

1. Copie su clave de API de OpenAI en un archivo llamado `token.env` en el directorio raíz del proyecto con el siguiente contenido:

```bash
OPENAI_API_KEY=su-clave-api-aquí
```

## Ejecución del Bot

1. **Inicie el Bot**:
```bash
python main.py
```

## Estructura del Código

El código principal se encuentra en el archivo `main.py`, que incluye las siguientes funciones:

- `custom_prompt()`: Define la plantilla de indicación personalizada para el bot.
- `load_llm()`: Inicializa y carga el modelo de chat de OpenAI.
- `retrival_qa_chain()`: Configura y crea la cadena de recuperación de QA.
- `qa_bot()`: Inicializa las incrustaciones, la base de datos FAISS y la cadena de recuperación de QA.
- `final_result()`: Función principal que se llama con una consulta y devuelve una respuesta del bot.
- `start()`: Función de inicio de Chainlit que inicializa el bot y establece la sesión de usuario.

## Contribuciones

Las contribuciones son bienvenidas! Por favor, haga Fork al proyecto y cree un Pull Request con sus cambios.

## Licencia

Este proyecto está licenciado bajo la Licencia MIT - vea el archivo [LICENSE](LICENSE) para más detalles.

---

Este README proporciona una descripción general del proyecto y las instrucciones básicas para configurar y ejecutar el bot de chat QA. También puede incluir secciones adicionales como `Autores`, `Agradecimientos`, `Cómo Contribuir`, etc., según sea necesario para su proyecto.