# README in en-US
# AI Content Generation System
The AI Content Generation System is a Python-based application that allows users to collect information from the web, summarize it using ChatGPT, and generate AI-generated content for YouTube ideas and AI news. The system comprises several modules, including data collection, AI agent interactions, summarization, and email communication.

## Features
- Collects user queries and performs a Google search to gather relevant information.
- Uses OpenAI's ChatGPT API for text summarization and restructuring.
- Employs AI agents "Leo13" and "Leo30" for conversation and content generation.
- Provides content for YouTube ideas and AI news.
- Sends generated content via email to a specified recipient.

## Prerequisites
Before running the system, ensure you have the following prerequisites:

- 1. Python 3.10 installed on your system.
- 2. Access to OpenAI's ChatGPT API and an API key.
- 3. OpenAI Python package installed (version used during development: openai==0.27.0).
- 4. An active internet connection to perform Google searches and interact with the ChatGPT API.

## Installation
- 1. Clone this repository to your local machine:
  ```
  git clone https://github.com/your-username/ai-content-generation.git
  ```
- 2. Change into the project directory:
  ```
  cd ai-content-generation
  ```
- 3. Install the required Python dependencies:
  ```
  pip install -r requirements.txt
  ```

## Configuration
To configure the system for your use, follow these steps:

- 1. Open the chatgpt_integration.py file and replace YOUR_OPENAI_API_KEY with your actual ChatGPT API key.
- 2. In the python_hub.py file, configure the AI agents' roles by changing leo13_role and leo30_role variables to either "user" or "system".
- 3. Set up your email server details in the send_email.py file by updating the smtp_server, smtp_port, smtp_username, and smtp_password variables.
- 4. Customize the email subject and recipient email address in the run_python_hub() function in the python_hub.py file.

## Usage
To use the AI Content Generation System:

- 1. Run the main.py script:
  ```
  python main.py
  ```
- 2. Follow the prompts to provide your query for the Google search.
- 3. The system will summarize the search results using ChatGPT.
- 4. AI agents "Leo13" and "Leo30" will engage in a conversation to generate content for YouTube ideas and AI news.
- 5. The generated content will be saved in data/Youtube_idea.txt and data/AI_news.txt.
- 6. The system will send the generated content via email to the specified recipient.

## Contributions
Contributions to the AI Content Generation System are welcome! Here's how you can contribute:

- 1. Fork the repository on GitHub.
- 2. Create a new branch from the main branch with a descriptive name for your feature or fix.
- 3. Implement your changes, ensuring to follow the existing code style and conventions.
- 4. Write unit tests for your code to maintain code quality.
- 5. Open a pull request against the main branch, describing your changes and improvements.
- 6. Your pull request will be reviewed by the maintainers, and upon approval, it will be merged into the main branch.

## License
The AI Content Generation System is open-source software licensed under the MIT License.

## Acknowledgments
Special thanks to OpenAI for providing access to the ChatGPT API and the community for valuable contributions and feedback.

Feel free to reach out to the maintainers with any questions or feedback. We hope you find the AI Content Generation System useful and enjoy contributing to its development!


# README em pt-BR
# Sistema de Geração de Conteúdo com Inteligência Artificial
O Sistema de Geração de Conteúdo com Inteligência Artificial é uma aplicação baseada em Python que permite aos usuários coletar informações da web, resumi-las usando o ChatGPT e gerar conteúdo produzido por IA para ideias de vídeos no YouTube e notícias sobre IA. O sistema é composto por vários módulos, incluindo coleta de dados, interações com o agente de IA, sumarização e comunicação por e-mail.

## Recursos
- Coleta consultas dos usuários e realiza uma busca no Google para obter informações relevantes.
- Utiliza a API do ChatGPT da OpenAI para sumarização e reestruturação de texto.
- Emprega os agentes de IA "Leo13" e "Leo30" para conversação e geração de conteúdo.
- Fornece conteúdo para ideias de vídeos no YouTube e notícias sobre IA.
- Envia o conteúdo gerado por e-mail para um destinatário especificado.

## Pré-requisitos
Antes de executar o sistema, certifique-se de ter os seguintes pré-requisitos:

- 1. Python 3.10 instalado em seu sistema.
- 2. Acesso à API do ChatGPT da OpenAI e uma chave de API.
- 3. Pacote Python da OpenAI instalado (versão utilizada durante o desenvolvimento: openai==0.27.0).
- 4. Uma conexão de internet ativa para realizar buscas no Google e interagir com a API do ChatGPT.

## Instalação
- 1. Clone este repositório em sua máquina local:
  ```
  git clone https://github.com/your-username/ai-content-generation.git
  ```
- 2. Navegue para o diretório do projeto:
  ```
  cd ai-content-generation
  ```
- 3. Instale as dependências Python necessárias:
  ```
  pip install -r requirements.txt
  ```

## Configuração
Para configurar o sistema para o seu uso, siga estes passos:

- 1. Abra o arquivo chatgpt_integration.py e substitua YOUR_OPENAI_API_KEY pela sua chave de API real do ChatGPT.
- 2. No arquivo python_hub.py, configure os papéis dos agentes de IA alterando as variáveis leo13_role e leo30_role para "usuário" ou "sistema".
- 3. Configure os detalhes do servidor de e-mail no arquivo send_email.py atualizando as variáveis smtp_server, smtp_port, smtp_username e smtp_password.
- 4. Personalize o assunto do e-mail e o endereço de e-mail do destinatário na função run_python_hub() no arquivo python_hub.py.

## Uso
Para utilizar o Sistema de Geração de Conteúdo com Inteligência Artificial:

- 1. Execute o script main.py:
  ```
  python main.py
  ```
- 2. Siga as instruções para fornecer sua consulta para a busca no Google.
- 3. O sistema irá resumir os resultados da busca usando o ChatGPT.
- 4. Os agentes de IA "Leo13" e "Leo30" irão se envolver em uma conversa para gerar conteúdo para ideias de vídeos no YouTube e notícias sobre IA.
- 5. O conteúdo gerado será salvo nos arquivos data/Youtube_idea.txt e data/AI_news.txt.
- 6. O sistema enviará o conteúdo gerado por e-mail para o destinatário especificado.

## Contribuições
Contribuições para o Sistema de Geração de Conteúdo com Inteligência Artificial são bem-vindas! Veja como você pode contribuir:

- 1. Faça um fork do repositório no GitHub.
- 2. Crie um novo branch a partir do branch principal com um nome descritivo para a sua funcionalidade ou correção.
- 3. Implemente suas alterações, garantindo que sigam o estilo e as convenções de código existentes.
- 4. Escreva testes unitários para o seu código para manter a qualidade do código.
- 5. Abra um pull request contra o branch principal, descrevendo suas alterações e melhorias.
- 6. Seu pull request será revisado pelos mantenedores e, após a aprovação, será mesclado no branch principal.

## Licença
O Sistema de Geração de Conteúdo com Inteligência Artificial é um software de código aberto licenciado sob a Licença MIT.

## Agradecimentos
Agradecemos à OpenAI por fornecer acesso à API do ChatGPT e à comunidade por suas valiosas contribuições e feedback.

Sinta-se à vontade para entrar em contato com os mantenedores se tiver alguma dúvida ou feedback. Esperamos que você ache o Sistema de Geração de Conteúdo com Inteligência Artificial útil e desfrute de contribuir para o seu desenvolvimento!