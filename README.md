# RPG Manager Online

**RPG Manager Online** é um sistema completo para gerenciamento de campanhas de RPG, criado para jogadores e mestres que desejam praticidade e organização em suas campanhas. Com ele, é possível criar, editar e salvar fichas de personagens, além de acessar um banco de dados integrado com itens, armas, habilidades e muito mais. Tudo de forma rápida e intuitiva, direto no navegador.

## Funcionalidades principais

- 📝 **Criação e edição de fichas de personagem:**
  Construa sua ficha de RPG com atributos, perícias, magias, equipamentos e anotações personalizadas.

- 📚 **Banco de dados integrado:**
  Pesquise e selecione itens, armas, habilidades e magias diretamente na plataforma.

- 💾 **Armazenamento de fichas:**
  Salve as fichas na conta do jogador para acesso fácil em qualquer sessão.

- ⚔️ **Gerenciamento dinâmico durante o jogo:**
  Atualize atributos, registre mudanças no inventário e controle os recursos do personagem em tempo real.

- 📱 **Visualização otimizada:**
  Interface clara e responsiva para facilitar o uso tanto em computadores quanto em dispositivos móveis.

## Tecnologias utilizadas

- 💻 **Frontend:** React.TS + Chakra UI
- ⚙️ **Backend:** FastAPI (Python)
- 🗄️ **Banco de dados:** Firebase.

## Como usar

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/tas48/rpg-manager-online.git
   ```  

2. **Instale as dependências do projeto (Backend e Frontend):**
   ```bash
   cd /server
   pip install -r requirements.txt
   ```
   ```bash
   cd /client
   npm install
   ```

3. **Configure o Firebase:**

   - Crie um projeto no [Firebase Console](https://console.firebase.google.com/).
   - Acesse a seção **Firestore Database** e crie o banco de dados.
   - Vá até **Configurações do Projeto** > **Contas de Serviço** e gere uma chave privada para autenticação com o Firebase.
   - baixe a chave a inclua no projeto.

4. **Configure o ambiente:**

   - Crie um arquivo `.env` na raiz do projeto com as configurações necessárias.
   - Use o arquivo `.env.example` como modelo.
   
   Exemplo de configuração do arquivo `.env`:

   ```env
   GOOGLE_APPLICATION_CREDENTIALS=/caminho/para/seu/firebase_credentials.json
   ```

5. **Execute o servidor FastAPI:**
   ```bash
   uvicorn main:app --reload
   ```
   *(ou o comando específico para rodar o seu backend)*

6. **Acesse no navegador:**
   Abra `http://localhost:8000` para usar a aplicação.

## Contribuição

Contribuições são muito bem-vindas! 🛠️ Sinta-se à vontade para:

- Reportar bugs. 🐛
- Sugerir novas funcionalidades. ✨
- Criar pull requests com melhorias no código. 🚀

Para começar, basta:

1. Fazer um fork do repositório.
2. Criar um branch com sua feature ou correção: `git checkout -b minha-feature`.
3. Commitar as mudanças: `git commit -m 'Minha nova feature'`.
4. Enviar as mudanças: `git push origin minha-feature`.
5. Abrir um pull request.


## Licença

Este projeto é licenciado sob a [MIT License](LICENSE). 📜
