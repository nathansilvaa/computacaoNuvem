# Usa a imagem oficial do Node.js como base
FROM node:16

# Define o diretório de trabalho dentro do container
WORKDIR /app

# Copia apenas o package.json para instalar dependências antes
COPY package.json ./

# Instala as dependências
RUN npm install

# Copia o restante do código do frontend para o container
COPY . .

# Expõe a porta padrão do React
EXPOSE 3000

# Comando para rodar a aplicação
CMD ["npm", "start"]
