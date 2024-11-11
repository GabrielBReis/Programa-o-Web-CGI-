# Programa-o-Web-CGI-1 e 2
Programação Web (CGI) 1 e 2 - Atividade de FPS

# Serviço Web CGI 1 - Saudação Personalizada

Este projeto é um exemplo de como criar um serviço web simples utilizando CGI (Common Gateway Interface) com um script Bash para processar dados de um formulário HTML. O objetivo é criar uma página que receba o nome de um usuário através de um formulário HTML e exiba uma mensagem personalizada de saudação.

## Passo a Passo

### 1. Clonar o Repositório

Primeiro, clone este repositório para o seu computador. Execute o seguinte comando no terminal:

```bash
git clone https://github.com/seuusuario/nome-do-repositorio.git
```

### 2. Configuração do Servidor Apache

Este projeto utiliza o servidor Apache para servir os scripts CGI. Para configurar o servidor, siga os passos abaixo:

#### 2.1 Instalar o Apache

Se você não tem o Apache instalado, pode instalá-lo usando o seguinte comando, dependendo da sua distribuição do Linux.

- Para distribuições baseadas no Ubuntu/Debian:

```bash
sudo apt update
sudo apt install apache2
```

- Para distribuições baseadas no CentOS/RHEL:

```bash
sudo yum install httpd
```

#### 2.2 Habilitar o CGI no Apache

O Apache vem com suporte a CGI, mas você precisa garantir que a execução de scripts CGI esteja ativada.

1. Abra o arquivo de configuração do Apache para edição:

```bash
sudo nano /etc/apache2/sites-available/000-default.conf
```

2. No arquivo de configuração, dentro da diretiva `<VirtualHost *:80>`, adicione a seguinte linha para habilitar o CGI:

```bash
Options +ExecCGI
```

3. Salve e saia do arquivo.

#### 2.3 Ativar o Módulo CGI

Para garantir que o Apache possa executar scripts CGI, ative o módulo CGI:

```bash
sudo a2enmod cgi
```

#### 2.4 Reiniciar o Apache

Reinicie o servidor Apache para aplicar as mudanças:

```bash
sudo systemctl restart apache2
```

### 3. Configurar o Script CGI

Agora, mova o seu script Bash para o diretório `cgi-bin` do Apache. No Ubuntu/Debian, esse diretório geralmente está localizado em:

```bash
/var/www/cgi-bin/
```

- Copie o script `saudacao.cgi` para esse diretório:

```bash
sudo cp ./saudacao.cgi /var/www/cgi-bin/
```

- Dê permissões de execução para o script:

```bash
sudo chmod +x /var/www/cgi-bin/saudacao.cgi
```

### 4. Criar a Página HTML do Formulário

Crie o arquivo HTML `form.html` em um diretório acessível pelo Apache (por exemplo, `/var/www/html/`):

```bash
sudo nano /var/www/html/form.html
```

Adicione o seguinte código HTML no arquivo `form.html`:

```html
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <title>Formulário de Saudação</title>
</head>
<body>
    <h2>Digite seu nome:</h2>
    <form action="/cgi-bin/saudacao.cgi" method="POST">
        <label for="nome">Nome:</label>
        <input type="text" id="nome" name="nome" required>
        <button type="submit">Enviar</button>
    </form>
</body>
</html>
```

### 5. Testar o Serviço

Agora, você está pronto para testar o serviço web. Siga as etapas abaixo:

#### 5.1 Acesse o Formulário

Abra o navegador e acesse a página HTML que você acabou de criar:

```
http://localhost/form.html
```

#### 5.2 Preencha o Formulário

Digite seu nome no campo de texto e clique no botão "Enviar". O formulário irá enviar os dados para o script CGI.

#### 5.3 Visualizar a Saudação

O script Bash `saudacao.cgi` irá processar os dados e exibir uma página HTML com a saudação personalizada, como no exemplo:

```
Olá, [seu_nome]!
```

### 6. Resumo do Código

O código do script `saudacao.cgi` realiza os seguintes passos:

1. **Exibe o cabeçalho HTTP**: O script começa com `echo "Content-Type: text/html"` para definir o tipo de resposta como HTML.
2. **Lê os dados do formulário**: Usa o comando `read` para capturar a entrada do formulário.
3. **Processa o nome**: A variável `nome` é extraída da entrada do formulário e exibida de forma personalizada.
4. **Gera a resposta HTML**: Exibe uma página HTML com a saudação personalizada.

### 7. Possíveis Erros e Soluções

- **Erro 500 (Internal Server Error)**: Verifique se o script CGI tem permissões de execução e se o servidor Apache está corretamente configurado para executar scripts CGI.
- **Erro 404 (Página não encontrada)**: Certifique-se de que o caminho para o formulário HTML e o script CGI estejam corretos.

---

Se tiver dúvidas ou encontrar problemas, consulte a documentação do Apache ou busque ajuda na comunidade online.
